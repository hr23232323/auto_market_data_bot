import requests
from bs4 import BeautifulSoup
import soupsieve as sv
from datetime import datetime as dt
import pytz
import pandas as pd
eastern = pytz.timezone('US/Eastern')

def main():
    stock_to_pull = "RDFN"
    base_url = "https://finance.yahoo.com/quote/"+stock_to_pull+"/options?p="+stock_to_pull+"&straddle=false"
    res = requests.get(base_url)
    soup = BeautifulSoup(res.text, features="lxml")


if __name__ == "__main__":
    main()
