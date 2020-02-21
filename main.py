import time
from os import path
from technicals_scraper import scrape as ts
from calls_scraper import scrape as cs
from puts_scraper import scrape as ps
from excel_writer import append_df_to_excel
import random

def main():
    # text stock list to array
    stock_list_txt = open("stock_list.txt", 'r')
    stock_list = []
    with open('stock_list.txt','r') as f:
        for line in f:
            for word in line.rstrip('\n').split(','):
               stock_list.append(word)

    # scrape for each stock
    for stock in stock_list:
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



if __name__ == "__main__":
    main()
