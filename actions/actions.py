# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

import requests

class ActionChatGPT(Action):
    def name(self):
        return "action_chatgpt"

    def run(self, dispatcher, tracker, domain):
        # Get user's message from Rasa tracker
        print('jayesh action chatchpt k andr')
        user_message = tracker.latest_message.get('text')

        # Call ChatGPT API (replace API_ENDPOINT with the actual ChatGPT API endpoint)
        chatgpt_api_endpoint = "https://api.openai.com/v1/chat/completions"
        response = requests.post(chatgpt_api_endpoint, json={"message": user_message})

        # Extract ChatGPT response
        chatgpt_response = response.json().get("generated_response", "Sorry, I didn't understand that.")

        # Send combined response to user
        dispatcher.utter_message(text=f"{user_message} {chatgpt_response}")

        return []
