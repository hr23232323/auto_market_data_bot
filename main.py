import time
from technicals_scraper import scrape as ts
from calls_scraper import scrape as cs
from puts_scraper import scrape as ps
from excel_writer import append_df_to_excel

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
        print(stock)
        technicals_df = ts(stock)
        time.sleep(1)
        puts_df = ps(stock)
        time.sleep(1)
        calls_df = cs(stock)
        time.sleep(1)

        break

    # read csv/DB
    append_df_to_excel('database_text.xlsx', technicals_df, sheet_name='technicals', index=False, header=False)


if __name__ == "__main__":
    main()
