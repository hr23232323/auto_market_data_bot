import time
from os import path
from technicals_scraper import scrape as ts
from calls_scraper import scrape as cs
from puts_scraper import scrape as ps
from excel_writer import append_df_to_excel
import random
from datetime import datetime as dt

def collect_data():
    # text stock list to array
    print("COLLECTING DATA")
    print(dt.now())
    test = False
    stock_list_txt = open("stock_list.txt", 'r')
    stock_list = []
    with open('stock_list.txt','r') as f:
        for line in f:
            for word in line.rstrip('\n').split(','):
               stock_list.append(word)

    # scrape for each stock
    if(test):
        stock_list = ['RDFN']
    for stock in stock_list:
        try:
            technicals_df = ts(stock)
            time.sleep(random.uniform(0.5, 1.5))
            puts_df = ps(stock)
            time.sleep(random.uniform(0.5, 1.5))
            calls_df = cs(stock)
            time.sleep(random.uniform(0.5, 1.5))

            # write to CSV/DB. Only write headers if first time
            append_df_to_excel('database_text.xlsx', technicals_df, sheet_name=stock + '_technicals', index=False)
            append_df_to_excel('database_text.xlsx', puts_df, sheet_name=stock + '_puts', index=False)
            append_df_to_excel('database_text.xlsx', calls_df, sheet_name=stock + '_calls', index=False)
        except:
            print("Stock FAILED-")
            print(stock)
            print("Time-")
            print(dt.now())
            continue
