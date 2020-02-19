## Happy path 1

* greet: hi
    - utter_greet
* restaurant_search: can you suggest me some restaurants
    - restaurant_search_form
    - form{"name":"restaurant_search_form"}
    - slot{"requested_slot":"location"}
* form: inform{"location":"ajmer"}
    - slot{"location": "ajmer"}
    - slot{"requested_slot":"cuisine"}
* form: inform{"cuisine":"Chinese"}
    - slot{"cuisine":"Chinese"}
    - slot{"requested_slot":"average_budget"}
* form: restaurant_search{"CARDINAL":"1000","average_budget":"1000"}
    - slot{"average_budget":"More than Rs. 700"}
    - slot{"is_search_results_found":true}
    - form{"name":null}
    - slot{"requested_slot":null}
    - email_send_form
    - form{"name":"email_send_form"}
    - slot{"requested_slot":"send_email"}
* form: affirm{"email_id":"bhardwaj.apoorvs@gmail.com"}
    - slot{"send_email": true}
    - slot{"email_id": "bhardwaj.apoorvs@gmail.com"}
    - form{"name": null}
* goodbye: thank you
    - utter_goodbye
    - action_restart

## Happy path 2

* greet: hi
    - utter_greet
* restaurant_search: can you suggest me some restaurants
    - restaurant_search_form
    - form{"name":"restaurant_search_form"}
    - slot{"requested_slot":"location"}
* form: inform{"location":"ajmer"}
    - slot{"location": "ajmer"}
    - slot{"requested_slot":"cuisine"}
* form: inform{"cuisine":"Chinese"}
    - slot{"cuisine":"Chinese"}
    - slot{"requested_slot":"average_budget"}
* form: restaurant_search{"CARDINAL":"1000","average_budget":"1000"}
    - slot{"average_budget":"More than Rs. 700"}
    - slot{"is_search_results_found":true}
    - form{"name":null}
    - slot{"requested_slot":null}
    - email_send_form
    - form{"name":"email_send_form"}
    - slot{"requested_slot":"send_email"}
* form: affirm
    - slot{"send_email": true}
    - slot{"requested_slot":"email_id"}
* form: inform{"email_id":"apoorv.bhardwaj@centricconsulting.com"}
    - slot{"email_id": "apoorv.bhardwaj@centricconsulting.com"}
    - form{"name": null}
* goodbye: thank you
    - utter_goodbye
    - action_restart

## User rejects sending mail request

* greet: hi
    - utter_greet
* restaurant_search: I am looking for a place to eat in [delhi](location)
    - restaurant_search_form
    - form{"name":"restaurant_search_form"}
    - slot{"location": "delhi"}
    - slot{"requested_slot":"cuisine"}
* form: inform{"cuisine":"Chinese"}
    - slot{"cuisine":"Chinese"}
    - slot{"requested_slot":"average_budget"}
* form: restaurant_search{"CARDINAL":"1000","average_budget":"1000"}
    - slot{"average_budget":"More than Rs. 700"}
    - slot{"is_search_results_found":true}
    - form{"name":null}
    - slot{"requested_slot":null}
    - email_send_form
    - form{"name":"email_send_form"}
    - slot{"requested_slot":"send_email"}
* form: deny
    - slot{"send_email": false}
    - form{"name":null}
    - slot{"requested_slot":null}
    - action_listen
    - utter_goodbye
    - action_restart

## User accepts sending mail request and email id has to be requested

* restaurant_search: I am looking for a place to eat in [delhi](location)
    - restaurant_search_form
    - form{"name":"restaurant_search_form"}
    - slot{"location": "delhi"}
    - slot{"requested_slot":"cuisine"}
* form: inform{"cuisine":"Chinese"}
    - slot{"cuisine":"Chinese"}
    - slot{"requested_slot":"average_budget"}
* form: restaurant_search{"CARDINAL":"1000","average_budget":"1000"}
    - slot{"average_budget":"More than Rs. 700"}
    - slot{"is_search_results_found":true}
    - form{"name":null}
    - slot{"requested_slot":null}
    - email_send_form
    - form{"name":"email_send_form"}
    - slot{"requested_slot":"send_email"}
* form: affirm
    - slot{"send_email": true}
    - slot{"requested_slot":"email_id"}
* form: inform{"email_id":"apoorv.bhardwaj@centricconsulting.com"}
    - slot{"email_id": "apoorv.bhardwaj@centricconsulting.com"}
    - form{"name": null}
* goodbye: thank you
    - utter_goodbye
    - action_restart

## User says bye on asking for sending mail request

* greet: hi
    - utter_greet
* restaurant_search: can you find me [chinese](cuisine:Chinese) restaurant
    - restaurant_search_form
    - form{"name":"restaurant_search_form"}
    - slot{"cuisine":"Chinese"}
    - slot{"requested_slot":"location"}
* form: inform{"location":"jaipur"}
    - slot{"location": "jaipur"}
    - slot{"requested_slot":"average_budget"}
* form: restaurant_search{"CARDINAL":"1000","average_budget":"1000"}
    - slot{"average_budget":"More than Rs. 700"}
    - slot{"is_search_results_found":true}
    - form{"name":null}
    - slot{"requested_slot":null}
    - email_send_form
    - form{"name":"email_send_form"}
    - slot{"requested_slot":"send_email"}
* form: goodbye
    - slot{"send_email": false}
    - form{"name":null}
    - slot{"requested_slot":null}
    - action_listen
    - utter_goodbye
    - action_restart

## User accepts sending mail request and provides email id in affirmation

* greet: hi
    - utter_greet
* restaurant_search: can you find me [chinese](cuisine:Chinese) restaurant
    - restaurant_search_form
    - form{"name":"restaurant_search_form"}
    - slot{"cuisine":"Chinese"}
    - slot{"requested_slot":"location"}
* form: inform{"location":"jaipur"}
    - slot{"location": "jaipur"}
    - slot{"requested_slot":"average_budget"}
* form: restaurant_search{"CARDINAL":"1000","average_budget":"1000"}
    - slot{"average_budget":"More than Rs. 700"}
    - slot{"is_search_results_found":true}
    - form{"name":null}
    - slot{"requested_slot":null}
    - email_send_form
    - form{"name":"email_send_form"}
    - slot{"requested_slot":"send_email"}
* form: affirm{"email_id":"kindresantosh@yahoo.com"}
    - slot{"send_email": true}
    - slot{"email_id": "kindresantosh@yahoo.com"}
    - form{"name": null}
* goodbye: thank you
    - utter_goodbye
    - action_restart

## User requests to stop on asking for sending mail request

* greet: hi
    - utter_greet
* restaurant_search: looking for restaurant for [more than 700](average_budget:More than Rs. 700)
    - restaurant_search_form
    - form{"name":"restaurant_search_form"}
    - slot{"average_budget":"More than Rs. 700"}
    - slot{"requested_slot":"location"}
* form: inform{"location":"chandigarh"}
    - slot{"location": "chandigarh"}
    - slot{"requested_slot":"cuisine"}
* form: inform{"cuisine":"Chinese"}
    - slot{"cuisine":"Chinese"}
    - slot{"is_search_results_found":true}
    - form{"name":null}
    - slot{"requested_slot":null}
    - email_send_form
    - form{"name":"email_send_form"}
    - slot{"requested_slot":"send_email"}
* form: stop
    - slot{"send_email": false}
    - form{"name":null}
    - slot{"requested_slot":null}
    - action_listen
    - utter_goodbye
    - action_restart

## User requests to stop on asking for email id

* restaurant_search: looking for restaurant for [more than 700](average_budget:More than Rs. 700)
    - restaurant_search_form
    - form{"name":"restaurant_search_form"}
    - slot{"average_budget":"More than Rs. 700"}
    - slot{"requested_slot":"location"}
* form: inform{"location":"chandigarh"}
    - slot{"location": "chandigarh"}
    - slot{"requested_slot":"cuisine"}
* form: inform{"cuisine":"Chinese"}
    - slot{"cuisine":"Chinese"}
    - slot{"is_search_results_found":true}
    - form{"name":null}
    - slot{"requested_slot":null}
    - email_send_form
    - form{"name":"email_send_form"}
    - slot{"requested_slot":"send_email"}
* form: affirm
    - slot{"send_email": true}
    - slot{"requested_slot":"email_id"}
* form: stop
    - slot{"email_id": "exit"}
    - form{"name":null}
    - slot{"requested_slot":null}
    - action_listen
    - utter_goodbye
    - action_restart

## No search results found

* greet: hi
    - utter_greet
* restaurant_search: looking for [chinese](cuisine:Chinese) restaurant in [bengaluru](location:bangalore)
    - restaurant_search_form
    - form{"name":"restaurant_search_form"}
    - slot{"location": "bangalore"}
    - slot{"cuisine":"Chinese"}
    - slot{"requested_slot":"average_budget"}
* form: restaurant_search{"CARDINAL":"1000","average_budget":"1000"}
    - slot{"average_budget":"More than Rs. 700"}
    - slot{"is_search_results_found":false}
    - form{"name":null}
    - slot{"requested_slot":null}
    - action_restart

## User requests to stop on asking for average budget

* restaurant_search: show me [south indian](cuisine:South Indian) restaurants in [vadodara](location)
    - restaurant_search_form
    - form{"name":"restaurant_search_form"}
    - slot{"location": "vadodara"}
    - slot{"cuisine":"South Indian"}
    - slot{"requested_slot":"average_budget"}
* form: stop
    - slot{"location":"exit"}
    - slot{"cuisine":"exit"}
    - slot{"average_budget":"exit"}
    - slot{"is_search_stopped":true}
    - form{"name":null}
    - slot{"requested_slot":null}
    - action_restart

## No search results found

* greet: hi
    - utter_greet
* restaurant_search: search for [north indian](cuisine:North Indian) food for [more than 700](average_budget:More than Rs. 700)
    - restaurant_search_form
    - form{"name":"restaurant_search_form"}
    - slot{"cuisine":"North Indian"}
    - slot{"average_budget":"More than Rs. 700"}
    - slot{"requested_slot":"location"}
* form: inform{"location":"ajmer"}
    - slot{"location": "ajmer"}
    - slot{"is_search_results_found":false}
    - form{"name":null}
    - slot{"requested_slot":null}
    - action_restart

## User requests to stop on asking for location

* greet: hi
    - utter_greet
* restaurant_search: looking for [italian](cuisine:Italian) restaurant for [more than 700](average_budget:More than Rs. 700)
    - restaurant_search_form
    - form{"name":"restaurant_search_form"}
    - slot{"cuisine":"Italian"}
    - slot{"average_budget":"More than Rs. 700"}
    - slot{"requested_slot":"location"}
* form: stop
    - slot{"location":"exit"}
    - slot{"cuisine":"exit"}
    - slot{"average_budget":"exit"}
    - slot{"is_search_stopped":true}
    - form{"name":null}
    - slot{"requested_slot":null}
    - action_restart

## No search results found

* greet: hi
    - utter_greet
* restaurant_search: can you find me restaurant in [vasai-virar city](location) for [more than 700](average_budget:More than Rs. 700)
    - restaurant_search_form
    - form{"name":"restaurant_search_form"}
    - slot{"location": "vasai-virar city"}
    - slot{"average_budget":"More than Rs. 700"}
    - slot{"requested_slot":"cuisine"}
* form: inform{"cuisine":"Chinese"}
    - slot{"cuisine":"Chinese"}
    - slot{"is_search_results_found":false}
    - form{"name":null}
    - slot{"requested_slot":null}
    - action_restart

## User requests to stop on asking for cuisine

* greet: hi
    - utter_greet
* restaurant_search: Can you suggest some good cafe in [meerut](location) for [more than 700](average_budget:More than Rs. 700)
    - restaurant_search_form
    - form{"name":"restaurant_search_form"}
    - slot{"location": "goa"}
    - slot{"average_budget":"More than Rs. 700"}
    - slot{"requested_slot":"cuisine"}
* form: stop
    - slot{"location":"exit"}
    - slot{"cuisine":"exit"}
    - slot{"average_budget":"exit"}
    - slot{"is_search_stopped":true}
    - form{"name":null}
    - slot{"requested_slot":null}
    - action_restart