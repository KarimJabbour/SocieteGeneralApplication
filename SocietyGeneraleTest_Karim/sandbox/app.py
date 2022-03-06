from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def index():
  return 'URL should include two parameters as such /quantity_integer/label_stock'

@app.route('/<int:quantity>/<label>')
def current_market_value(quantity,label):
  url = "https://yh-finance.p.rapidapi.com/stock/v2/get-summary"
  headers = {
    'x-rapidapi-host': "yh-finance.p.rapidapi.com",
    'x-rapidapi-key': "69ba308392mshc248a793b99a70ap17aa69jsna08b7f3c0085"
    }

  querystring = {"symbol":label,"region":"US"}
  print (label)
  response = requests.request("GET", url, headers=headers, params=querystring)
  closing_price=response.json().get('price').get('regularMarketPreviousClose').get('raw')
  # ("Notional using",quantity," shares using label ",product," with closing price of ",closing_price, " : ", quantity * closing_price)
  r = {'Notional':  (quantity*closing_price)}
  return r

