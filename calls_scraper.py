import requests
from bs4 import BeautifulSoup
import soupsieve as sv
from datetime import datetime as dt
import pytz
import pandas as pd
eastern = pytz.timezone('US/Eastern')

def scrape(stock_to_pull):
    base_url = "https://finance.yahoo.com/quote/"+stock_to_pull+"/options?p="+stock_to_pull+"&straddle=false"
    res = requests.get(base_url)
    soup = BeautifulSoup(res.text, features="lxml")

    call_table = soup.find("table", {"class": "calls"})
    calls = sv.select('tr:has(> td)', call_table)
    calls_df = pd.DataFrame()
    for call in calls:
        call_det = {}
        call_det["stock_name"] = stock_to_pull
        call_det["strike_price"] = call.find("td", {"class" : "data-col2"}).text
        call_det["last_price"] = call.find("td", {"class" : "data-col3"}).text
        call_det["bid_price"] = call.find("td", {"class" : "data-col4"}).text
        call_det["ask_price"] = call.find("td", {"class" : "data-col5"}).text
        call_det["chng_price"] = call.find("td", {"class" : "data-col6"}).text
        call_det["perc_chng"] = call.find("td", {"class" : "data-col7"}).text
        call_det["volume"] = call.find("td", {"class" : "data-col8"}).text
        call_det["opn_int"] = call.find("td", {"class" : "data-col9"}).text
        call_det["imp_vol"] = call.find("td", {"class" : "data-col10"}).text
        if("in-the-money" in call["class"]):
            call_det["itm"] = "Y"
        else:
            call_det["itm"] = "N"
        call_det["curr_time"] = eastern.localize(dt.now()).strftime('%Y-%m-%d %H:%M:%S')
        calls_df = calls_df.append(call_det,ignore_index=True)

    return calls_df
