#!/usr/bin/env python3
# QUESTION 1:
# Method returns the product of a passed quantity and the closing price of a passed stock (i.e. product)
def current_market_value(quantity,product):
 
  import requests

  url = "https://yh-finance.p.rapidapi.com/stock/v2/get-summary"
  headers = {
    'x-rapidapi-host': "yh-finance.p.rapidapi.com",
    'x-rapidapi-key': "69ba308392mshc248a793b99a70ap17aa69jsna08b7f3c0085"
    }
  
  querystring = {"symbol":product,"region":"US"}

  response = requests.request("GET", url, headers=headers, params=querystring)
  closing_price=response.json().get('price').get('regularMarketPreviousClose').get('raw')
  print("Notional using",quantity," shares using label ",product," with closing price of ",closing_price, " : ", quantity * closing_price)
  return (quantity * closing_price)

# Demo of Method "Current Market Value"
current_market_value(2400,'TSLA')
