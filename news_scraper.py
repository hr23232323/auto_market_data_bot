import requests
from bs4 import BeautifulSoup
import soupsieve as sv
from datetime import datetime as dt
import pytz
import pandas as pd
eastern = pytz.timezone('US/Eastern')

def main():
    stock_to_pull = "RDFN"
    base_url = "https://www.tiingo.com/"+stock_to_pull+"/overview"
    res = requests.get(base_url)
    soup = BeautifulSoup(res.text, features="lxml")
    print(res)


if __name__ == "__main__":
    main()
