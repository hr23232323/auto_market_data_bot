from technicals_scraper import scrape as ts


def main():
    stock_list_txt = open("stock_list.txt", 'r')
    stock_list = [line.rstrip('\n').split(',') for line in stock_list_txt.readlines()]
    
    ts("rdfn")



if __name__ == "__main__":
    main()
