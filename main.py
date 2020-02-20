import time
from technicals_scraper import scrape as ts


def main():
    stock_list_txt = open("stock_list.txt", 'r')
    stock_list = []
    with open('stock_list.txt','r') as f:
        for line in f:
            for word in line.rstrip('\n').split(','):
               stock_list.append(word)
    print(stock_list)
    for stock in stock_list:
        print(stock)
        ts(stock)







        time.sleep(1)




if __name__ == "__main__":
    main()
