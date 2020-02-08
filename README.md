# Algorithmic Trader
An algorithmic trading program capable of collecting market data, training and trading

## About
This project was developed as a way to explore the idea of algorithmic/automated trading. The key workflow behind this project involves collecting extensive market data in batch processes using web scraping; creating a database of historic intraday prices, indicators and news; training a model to utilize historical data and recognize trading patterns/trends; testing trading strategies in new real time using paper trading APIs. Eventually, the goal is to create a completely automated program which collects data, trains and trades without human intervention. 

## Usage
This project is primarily built in python 3.7.1 and involves packages which need to be installed. To make getting started with this project easier, we've created a requirements.txt file which contains all the different python packages needed. You can utilize this file (after cloning this repository) by using the following command:

```
pip install -r requirements.txt
```

Following this step you cna start using the project. We suggest starting with the scraper.py code.
