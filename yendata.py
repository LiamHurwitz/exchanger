import requests
import json

"""
First we:
    -Grab the updated currency conversion rates from the free API (once when the application begins)
    -Then we save that data to a json so we don't request too often
    -Then we parse that data to find the USD-JPY conversion rate

    -Then we export this file to a TUI

The TUI's job is to:
    -Initialize an empty window
    -Grab the conversion rates we just calculated
    -Prompt either:
        -USD -> JPY
        -JPY -> USD
    - Use data to show converted currency
    -Prompt the user to refresh the program

"""

def initialRequest():
    url = "https://v6.exchangerate-api.com/v6/3420cb14e546955c837e27b5/latest/USD"
    response = requests.get(url)
    data = response.json()

    print(data)

    # We save the json data so we don't have to call the API too much
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def currencyParse():
    with open('data.json', 'r') as f:
        data = json.load(f)

    conversion_rate = data["conversion_rates"]["JPY"]
    return conversion_rate



