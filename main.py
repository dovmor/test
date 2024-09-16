

import requests

def get_bitcoin_price():
    # Define the API endpoint
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    
    # Make a GET request to the API
    response = requests.get(url)
    
    # Parse the JSON response
    data = response.json()
    
    # Extract the Bitcoin price in USD
    bitcoin_price = data['bpi']['USD']['rate']
    
    return bitcoin_price

# Print the current Bitcoin price
print("Current Bitcoin price in USD:", get_bitcoin_price())