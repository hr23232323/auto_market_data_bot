import requests
from bs4 import BeautifulSoup
import soupsieve as sv
from datetime import datetime as dt
import pytz
import pandas as pd
eastern = pytz.timezone('US/Eastern')

def main():
    stock_to_pull = "RDFN"
    base_url = "https://finance.yahoo.com/quote/"+stock_to_pull
    res = requests.get(base_url)
    soup = BeautifulSoup(res.text, features="lxml")

    technical_table = soup.find("div", {"id": "quote-summary"})
    technicals_df = pd.DataFrame()
    technical_dets = {}
    technical_dets["curr_price"] = soup.find("div", {"id": "quote-header-info"}).findAll("span")[1].text
    technical_dets["price_cng"] = soup.find("div", {"id": "quote-header-info"}).findAll("span")[2].text.split(" ")[0]
    technical_dets["percent_cng"] = soup.find("div", {"id": "quote-header-info"}).findAll("span")[2].text.split(" ")[1].replace("(", "").replace(")", "")
    technical_dets["prev_close"] = technical_table.find("td", {"data-test": "PREV_CLOSE-value"}).text
    technical_dets["open"] = technical_table.find("td", {"data-test": "OPEN-value"}).text
    technical_dets["bid_val"] = technical_table.find("td", {"data-test": "BID-value"}).text.split(" x ")[0]
    technical_dets["bid_quant"] = technical_table.find("td", {"data-test": "BID-value"}).text.split(" x ")[1]
    technical_dets["ask_val"] = technical_table.find("td", {"data-test": "ASK-value"}).text.split(" x ")[0]
    technical_dets["ask_quant"] = technical_table.find("td", {"data-test": "ASK-value"}).text.split(" x ")[1]
    technical_dets["day_low"] = technical_table.find("td", {"data-test": "DAYS_RANGE-value"}).text.split(" - ")[0]
    technical_dets["day_high"] = technical_table.find("td", {"data-test": "DAYS_RANGE-value"}).text.split(" - ")[1]
    technical_dets["52_week_low"] = technical_table.find("td", {"data-test": "FIFTY_TWO_WK_RANGE-value"}).text.split(" - ")[0]
    technical_dets["52_week_high"] = technical_table.find("td", {"data-test": "FIFTY_TWO_WK_RANGE-value"}).text.split(" - ")[1]
    technical_dets["volume"] = technical_table.find("td", {"data-test": "TD_VOLUME-value"}).text
    technical_dets["3m_avg_volume"] = technical_table.find("td", {"data-test": "AVERAGE_VOLUME_3MONTH-value"}).text
    technical_dets["market_cap"] = technical_table.find("td", {"data-test": "MARKET_CAP-value"}).text
    technical_dets["5y_m_beta"] = technical_table.find("td", {"data-test": "BETA_5Y-value"}).text
    technical_dets["pe_ratio"] = technical_table.find("td", {"data-test": "PE_RATIO-value"}).text
    technical_dets["eps"] = technical_table.find("td", {"data-test": "EPS_RATIO-value"}).text
    technical_dets["earnings_dt"] = technical_table.find("td", {"data-test": "EARNINGS_DATE-value"}).text
    technical_dets["1y_target_est"] = technical_table.find("td", {"data-test": "ONE_YEAR_TARGET_PRICE-value"}).text
    technical_dets["curr_time"] = eastern.localize(dt.now()).strftime('%Y-%m-%d %H:%M:%S')
    technicals_df = technicals_df.append(technical_dets,ignore_index=True)

    print(technicals_df)

if __name__ == "__main__":
    main()
