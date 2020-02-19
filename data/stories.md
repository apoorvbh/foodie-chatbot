## happy path
* greet
    - utter_greet
* restaurant_search
    - restaurant_search_form
    - form{"name": "restaurant_search_form"}
    - form{"name": null}
    - slot{"is_search_results_found": true}
    - email_send_form
    - form{"name": "email_send_form"}
    - form{"name": null}
* goodbye OR stop
    - utter_goodbye
    - action_restart

## happy path without greet
* restaurant_search
    - restaurant_search_form
    - form{"name": "restaurant_search_form"}
    - form{"name": null}
    - slot{"is_search_results_found": true}
    - email_send_form
    - form{"name": "email_send_form"}
    - form{"name": null}
* goodbye OR stop
    - utter_goodbye
    - action_restart

## unhappy path 1
* greet
    - utter_greet
* restaurant_search
    - restaurant_search_form
    - form{"name": "restaurant_search_form"}
    - form{"name": null}
    - slot{"is_search_results_found": false}
    - action_restart

## unhappy path 1 without greet
* restaurant_search
    - restaurant_search_form
    - form{"name": "restaurant_search_form"}
    - form{"name": null}
    - slot{"is_search_results_found": false}
    - action_restart

## unhappy path 2
* greet
    - utter_greet
* restaurant_search
    - restaurant_search_form
    - form{"name": "restaurant_search_form"}
    - slot{"is_search_stopped": true}
    - action_restart

## unhappy path 2 without greet
* restaurant_search
    - restaurant_search_form
    - form{"name": "restaurant_search_form"}
    - slot{"is_search_stopped": true}
    - action_restart