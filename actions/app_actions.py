import subprocess

from config.app_registry import APPS


def open_application(app_name: str):

    app_name = app_name.lower()

    if app_name not in APPS:
        return f"I don't know the application {app_name}"

    try:
        subprocess.Popen(APPS[app_name])

        return f"Opening {app_name}"

    except Exception as e:
        return f"Failed to open {app_name}"