from config.app_registry import APPS
from config.website_registry import WEBSITES


OPEN_WORDS = [
    "open",
    "launch",
    "start",
    "run"
]


TIME_PHRASES = [
    "what time is it",
    "tell me the time",
    "current time",
    "time now"
]


SHUTDOWN_PHRASES = [
    "shutdown zoro",
    "exit",
    "quit",
    "stop listening"
]

def parse(command: str):

    command = command.lower().strip()

    # Time Intent
    for phrase in TIME_PHRASES:
        if phrase in command:
            return {
                "intent": "GET_TIME"
            }

    # Shutdown Intent
    for phrase in SHUTDOWN_PHRASES:
        if phrase in command:
            return {
                "intent": "SHUTDOWN"
            }

    # Open App Intent
    for word in OPEN_WORDS:

        if word in command:

            for app in APPS:

                if app in command:

                    return {
                        "intent": "OPEN_APP",
                        "target": app
                    }

    # Open Website Intent
    for word in OPEN_WORDS:

        if word in command:

            for site in WEBSITES:

                if site in command:

                    return {
                        "intent": "OPEN_WEBSITE",
                        "target": site
                    }

    return {
        "intent": "UNKNOWN"
    }