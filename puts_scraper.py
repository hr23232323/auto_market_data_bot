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

    put_table = soup.find("table", {"class": "puts"})
    put_date = put_table.parent.parent.previous_sibling.select('span')[4].text
    #print(put_date)
    puts = sv.select('tr:has(> td)', put_table)
    puts_df = pd.DataFrame()
    for put in puts:
        put_det = {}
        put_det["stock_name"] = stock_to_pull
        put_det["expiry_date"] = put_date
        put_det["strike_price"] = put.find("td", {"class" : "data-col2"}).text
        put_det["last_price"] = put.find("td", {"class" : "data-col3"}).text
        put_det["bid_price"] = put.find("td", {"class" : "data-col4"}).text
        put_det["ask_price"] = put.find("td", {"class" : "data-col5"}).text
        put_det["chng_price"] = put.find("td", {"class" : "data-col6"}).text
        put_det["perc_chng"] = put.find("td", {"class" : "data-col7"}).text
        put_det["volume"] = put.find("td", {"class" : "data-col8"}).text
        put_det["opn_int"] = put.find("td", {"class" : "data-col9"}).text
        put_det["imp_vol"] = put.find("td", {"class" : "data-col10"}).text
        if("in-the-money" in put["class"]):
            put_det["itm"] = "Y"
        else:
            put_det["itm"] = "N"
        put_det["curr_time"] = eastern.localize(dt.now()).strftime('%Y-%m-%d %H:%M:%S')
        puts_df = puts_df.append(put_det,ignore_index=True)
    return puts_df
