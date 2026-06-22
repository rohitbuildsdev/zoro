from actions.app_actions import open_application
from actions.web_actions import open_website
from actions.time_actions import get_current_time
from actions.system_actions import shutdown_zoro

class Router:

    def route(self, intent_data):

        intent = intent_data["intent"]

        if intent == "OPEN_APP":
            return open_application(
                intent_data["target"]
            )

        if intent == "OPEN_WEBSITE":
            return open_website(
                intent_data["target"]
            )

        if intent == "GET_TIME":
            return get_current_time()

        if intent == "SHUTDOWN":
            return shutdown_zoro()

        return "Sorry, I didn't understand."