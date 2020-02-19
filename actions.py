from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

import json
import re

import zomatopy
import sent_email
import check_city_tier

from read_yml_file import read_yml
from zomato_search_result import ZomotoSearchResult

from rasa_sdk import Action
from rasa_sdk import Tracker
from rasa_sdk.events import SlotSet, FollowupAction, Restarted, ConversationPaused, UserUtteranceReverted
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

from typing import Dict, Text, Any, List, Union, Optional

def read_secrets():
    secrets_config = read_yml('./secrets.yml')
    return secrets_config

def send_email(email_id, location, cuisine, average_budget):
    secrets_config = read_secrets()
    config = secrets_config['smtp']
    smtp = sent_email.initialize_app(config)
        
    results = restaurant_search(location, cuisine, average_budget, 10)
    return smtp.sent_email(email_id, location, cuisine, average_budget, results)

def restaurant_search(location, cuisine, average_budget, limit = 5):
    secrets_config = read_secrets()
    config= secrets_config['zomato']
    zomato = zomatopy.initialize_app(config)
    location_detail=zomato.get_location(location, 1)
    d1 = json.loads(location_detail)
    lat=d1["location_suggestions"][0]["latitude"]
    lon=d1["location_suggestions"][0]["longitude"]
    cuisines_dict={'Chinese':25, 'Mexican':73,'Italian':55,'American':1,'North Indian':50,'South Indian':85}
    results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 20)
    d = json.loads(results)
    output = []
    if d['results_found'] != 0:
        output =[ZomotoSearchResult(restaurant['restaurant']['name'], restaurant['restaurant']['location']['address'],
        restaurant['restaurant']['average_cost_for_two'],restaurant['restaurant']['user_rating']['aggregate_rating']) 
            for restaurant in d['restaurants']]
    filtered_result = filter_by_average_budget(output, average_budget)
    return filtered_result[:limit]

def filter_by_average_budget(search_results, average_budget):
    output = []
    price_for_two = average_budget.lower()
    
    for search_result in search_results:
        if price_for_two == 'lesser than rs. 300' and search_result.avg_budget_for_two < 300:
            output.append(search_result)
        elif price_for_two == 'rs. 300 to 700' and (search_result.avg_budget_for_two >= 300 and search_result.avg_budget_for_two <= 700):
            output.append(search_result)
        elif price_for_two == 'more than rs. 700' and search_result.avg_budget_for_two > 700:
            output.append(search_result)
    return output

def assign_average_budget(average_budget):
    try:
        average_budget = int(average_budget)
        if average_budget < 300:
            return "Lesser than Rs. 300"
        elif average_budget >= 300 and average_budget <= 700:
            return "Rs. 300 to 700"
        else:
            return "More than Rs. 700"
    except:
        return average_budget

class RestaurantSearchForm(FormAction):
    def name(self) -> Text:
        return "restaurant_search_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["location", "cuisine", "average_budget"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "location": [
                self.from_entity(entity = "location", intent = ["inform", "restaurant_search"]),
                self.from_entity(entity = "GPE", intent = ["inform", "restaurant_search"]),
                self.from_entity(entity = "LOC", intent = ["inform", "restaurant_search"]),
                self.from_intent(value = "exit", intent = ["stop", "goodbye"])
                ],
            "cuisine": [
                self.from_entity(entity = "cuisine", intent = ["inform", "restaurant_search"]),
                self.from_entity(entity = "PRODUCT", intent = ["inform", "restaurant_search"]),
                self.from_intent(value = "exit", intent = ["stop", "goodbye"])
                ],
            "average_budget": [
                self.from_entity(entity = "average_budget", intent = ["inform", "restaurant_search"]),
                self.from_entity(entity = "MONEY", intent = ["inform", "restaurant_search"]),
                self.from_entity(entity = "CARDINAL", intent = ["inform", "restaurant_search"]),
                self.from_intent(value = "exit", intent = ["stop", "goodbye"])
                ]
        }

    @staticmethod
    def cuisine_db() -> List[Text]:
        return ["chinese", "italian", "mexican", "american", "north indian", "south indian"]

    @staticmethod
    def average_budget_db() -> List[Text]:
        return ["lesser than rs. 300", "rs. 300 to 700", "more than rs. 700"]

    def validate_location(self, value: Text, dispatcher: CollectingDispatcher, tracker: Tracker, 
    domain: Dict[Text, Any]) -> Dict[Text, Any]:
        """Validate num_people value."""

        if value == "exit":
            return {"location":"exit", "cuisine":"exit", "average_budget":"exit"}

        try:
            check_location = check_city_tier.initialize_app()
            if value and check_location.check_city_tier(value):
                # validation succeeded, set the value of the "location" slot to value
                return {"location": value}
            else:
                dispatcher.utter_message(template="utter_location_not_served")
                # validation failed, set slot to None
                return {"location": None}
        except:
            return {"location": None}

    def validate_cuisine(self, value: Text, dispatcher: CollectingDispatcher, tracker: Tracker, 
    domain: Dict[Text, Any]) -> Dict[Text, Any]:
        """Validate cuisine value."""

        if value == "exit":
            return {"location":"exit", "cuisine":"exit", "average_budget":"exit"}

        try:
            if value and value.lower() in self.cuisine_db():
                # validation succeeded, set the value of the "cuisine" slot to value
                return {"cuisine": value}
            else:
                dispatcher.utter_message(template="utter_option_not_available")
                # validation failed, set this slot to None, meaning the
                # user will be asked for the slot again
                return {"cuisine": None}
        except:
            return {"cuisine": None}

    def validate_average_budget(self, value: Text, dispatcher: CollectingDispatcher, tracker: Tracker, 
    domain: Dict[Text, Any]) -> Dict[Text, Any]:
        """Validate average budget value."""

        if value == "exit":
            return {"location":"exit", "cuisine":"exit", "average_budget":"exit"}

        try:
            if value:
                value = assign_average_budget(value)

            if value and value.lower() in self.average_budget_db():
                # validation succeeded, set the value of the "average_budget" slot to value
                return {"average_budget": value}
            else:
                dispatcher.utter_message(template="utter_option_not_available")
                # validation failed, set this slot to None, meaning the
                # user will be asked for the slot again
                return {"average_budget": None}
        except:
            return {"average_budget": None}

    def submit(self,dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""
        try:
            location = tracker.get_slot('location')
            cuisine = tracker.get_slot('cuisine')
            average_budget = tracker.get_slot('average_budget')

            if (location == "exit") and (cuisine == "exit") and (average_budget == "exit"):
                dispatcher.utter_message(template = "utter_goodbye")
                return[SlotSet("is_search_stoppped", True)]

            results = restaurant_search(location, cuisine, average_budget)
            response = "Here are your {} restaurants in {} for {} budget:\n".format(cuisine, location.title(), average_budget)
            
            for index, result in enumerate(results):
                output = '{}) {} in {} has been rated {}'.format((index + 1), result.restaurant_name, result.restaurant_address, 
                result.user_rating)
                response = response + output +"\n"

            dispatcher.utter_message(template="utter_slots_values", location = location, 
            cuisine = cuisine, average_budget = average_budget)

            if len(results) > 0:
                dispatcher.utter_message(response)
                return [SlotSet("is_search_results_found", True)]
            else:
                dispatcher.utter_message(template = "utter_search_results_not_found")
                return [SlotSet("is_search_results_found", False)]
        except:
            dispatcher.utter_message(template = "utter_unable_to_search")
            return [SlotSet("is_search_results_found", False)]


class EmailSendForm(FormAction):
    def name(self) -> Text:
        return "email_send_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        if tracker.get_slot('send_email'):
            return ["send_email", "email_id"]
        else:
            return ["send_email"]
        
    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "send_email": [
                self.from_intent(intent = "affirm", value = True),
                self.from_intent(intent = ["deny", "stop", "goodbye"], value = False)
            ],
            "email_id": [
                self.from_entity(entity = "email_id", intent = ["inform", "affirm"]),
                self.from_text(intent = "inform"),
                self.from_intent(value = "exit", intent = ["stop", "goodbye"])
            ]
        }

    def validate_email_id(self, value: Text, dispatcher: CollectingDispatcher, tracker: Tracker, 
    domain: Dict[Text, Any]) -> Dict[Text, Any]:
        """Validate email_id value."""

        if value == "exit":
            return {"email_id":"exit"}

        try:
            regex = r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
            if(re.search(regex, value)):
                # validation succeeded, set the value of the "email_id" slot to value
                return {"email_id": value}
            else:
                dispatcher.utter_message(template="utter_email_id_not_valid")
                # validation failed, set this slot to None, meaning the
                # user will be asked for the slot again
                return {"email_id": None}
        except:
            return {"email_id": None}

    def submit(self,dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""
        try:
            is_send_email = tracker.get_slot('send_email')
            email_id = tracker.get_slot('email_id')
 
            if is_send_email and (email_id != "exit"):
                location = tracker.get_slot('location')
                cuisine = tracker.get_slot('cuisine')
                average_budget = tracker.get_slot('average_budget')

                result = send_email(email_id, location, cuisine, average_budget)

                if result:
                    dispatcher.utter_message(template = "utter_mail_sent", email_id = email_id)
                else:
                    dispatcher.utter_message(template = "utter_mail_not_sent")
               
                return []
            else:
                dispatcher.utter_message(template = "utter_goodbye")
                return[Restarted()]

        except:
            dispatcher.utter_message(template = "utter_mail_not_sent")
            return []
            
        