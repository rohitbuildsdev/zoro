import webbrowser

from config.website_registry import WEBSITES


def open_website(site_name: str):

    site_name = site_name.lower()

    if site_name not in WEBSITES:
        return f"I don't know the website {site_name}"

    webbrowser.open(WEBSITES[site_name])

    return f"Opening {site_name}"