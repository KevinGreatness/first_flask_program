# -*- coding: utf-8 -*-
"""
Created on Fri May  2 11:03:35 2025

Creates a web server that can output stock information tot he user.

@author: Kevin Grolemund
"""

from flask import Flask, jsonify, request
import pandas as pd

app = Flask('csit257a6_Grolemund.py')

@app.route("/")
def welcome():
    """
    Displays a welcome message on the web server.
  
    Returns
    -------
    str
        A Welcome message to the user.

    """
    return "Welcome to my server!"

@app.route("/info")
def info():
    """
    Displays the server information on the web server.
    Maps to '/info' using the @app.route decorator

    Returns
    -------
    str
        The server information.

    """
    return "This is Kevin Grolemund's web server!!!"

@app.route("/stock", methods=["GET"])
def stock_info():
    """
    Outputs the stock price of the given stock symbol. It responds to HTTP
    GET requests to get the stock symbol. If the stock isn't found, it
    lets the user know.

    Returns
    -------
    str
        The stock symbol's price.

    """
    symbol = str(request.args.get("symbol"))
    symbol = symbol.upper()
    url = "https://raw.githubusercontent.com/gheniabla/datasets/master/CompaniesMarketCap.csv"
    stocks_df = pd.read_csv(url)
    price = 'Not found!'
    for i, row in stocks_df.iterrows():
        sym = row['Symbol']
        if sym == symbol:
            price = row['price (USD)']
            break
    return jsonify(str(f"{symbol}: {price}"))

@app.route("/company", methods=["GET"])
def company_info():
    """
    Outputs the company info of the stock symbol that the user entered.
    This includes stock symbol, price, marketcap, and country. 
    This uses an HTTP GET request and lets the user know if the stock isnt found.

    Returns
    -------
    str
        The stock company's info..

    """
    symbol = str(request.args.get("symbol"))
    symbol = symbol.upper()
    url = "https://raw.githubusercontent.com/gheniabla/datasets/master/CompaniesMarketCap.csv"
    stocks_df = pd.read_csv(url)
    company_found = False
    market_cap = ""
    price = ""
    country = ""
    for i, row in stocks_df.iterrows():
        sym = row['Symbol']
        if sym == symbol:
            price = row['price (USD)']
            market_cap = row['marketcap']
            country = row['country']
            company_found = True
            break
     
    if company_found:
        return jsonify(str(f"Company: {symbol} Symbol: {symbol} MarketCap: {market_cap} "
                        f"Price(USD): {price} Country: {country}"))
    else:
        return jsonify(str(f"{symbol} was not found"))
    

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False) # Default Port is 5000, which we want
    # Did some research on the 404 favicons error
    # Learned it is a minor thing that doesnt affect the program, so i left it