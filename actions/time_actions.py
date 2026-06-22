from datetime import datetime


def get_current_time():

    current = datetime.now()

    return current.strftime(
        "The time is %I:%M %p"
    )