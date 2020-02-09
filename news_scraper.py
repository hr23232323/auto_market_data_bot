import requests
from bs4 import BeautifulSoup
import soupsieve as sv
from datetime import datetime as dt
import pytz
import pandas as pd
eastern = pytz.timezone('US/Eastern')

def main():
    stock_to_pull = "RDFN"
    base_url = "https://seekingalpha.com/symbol/"+stock_to_pull
    res = requests.get(base_url)
    soup = BeautifulSoup(res.text, features="lxml")

    article_list = soup.find("ul", {"id": "symbol-page-latest"})
    articles = sv.select('li', article_list)
    news_df = pd.DataFrame()
    for article in articles:
        news_det = {}
        news_det["headline"] = article.find("div", {"class" : "symbol_article"}).text
        spans = article.find("div", {"class" : "date_on_by"}).findChildren("span", {"class": ""})
        for span in spans:
            
        #news_det["release_dt"] = article.find("div", {"class" : "date_on_by"}).text
        #print(news_det)
        print('\n\n')


if __name__ == "__main__":
    main()
