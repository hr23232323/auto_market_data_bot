import requests
from bs4 import BeautifulSoup
import soupsieve as sv
from datetime import datetime as dt
import pytz
import pandas as pd
eastern = pytz.timezone('US/Eastern')

def main():
    stock_to_pull = "RDFN"
    base_url = "https://finance.yahoo.com/quote/"+stock_to_pull
    res = requests.get(base_url)
    soup = BeautifulSoup(res.text, features="lxml")

    technical_table = soup.find("div", {"id": "quote-summary"})
    technical_dets = {}
    technical_dets["prev_close"] = technical_table.find("td", {"data-test": "PREV_CLOSE-value"}).text


    print(technical_dets)

    #for indicator in technicals:
#        print(indicator.find("td", {"data-test": "OPEN-value"}))
#        print('\n\n')

if __name__ == "__main__":
    main()
