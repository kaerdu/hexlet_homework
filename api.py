import requests

URL_RATES = "https://api.freecurrencyapi.com/v1/latest?apikey="
URL_DESCRIPTIONS = "https://api.freecurrencyapi.com/v1/currencies?apikey="
KEY = "fca_live_slhPSeCLAqhKTNsXuVbX8f2zhy5kVzSJJdGkVwtk"


def get_currencies_online():
    response = requests.get(URL_RATES + KEY)
    return response.json()["data"]


def get_currency_descriptions():
    response = requests.get(URL_DESCRIPTIONS + KEY)
    return response.json()["data"]
