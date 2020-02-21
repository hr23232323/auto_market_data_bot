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
        if(path.exists("database_text.xlsx")):
            append_df_to_excel('database_text.xlsx', technicals_df, sheet_name='technicals' + stock, index=False, header=False)
            append_df_to_excel('database_text.xlsx', puts_df, sheet_name='puts' + stock, index=False, header=False)
            append_df_to_excel('database_text.xlsx', calls_df, sheet_name='calls' + stock, index=False, header=False)
        else:
            append_df_to_excel('database_text.xlsx', technicals_df, sheet_name='technicals' + stock, index=False)
            append_df_to_excel('database_text.xlsx', puts_df, sheet_name='puts' + stock, index=False)
            append_df_to_excel('database_text.xlsx', calls_df, sheet_name='calls' + stock, index=False)

        break


if __name__ == "__main__":
    main()
