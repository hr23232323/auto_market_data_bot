# Automatic Market Data Bot
An automated python-based bot capable of collecting intraday market data. Currently supports: technicals, call options, put options.

## About
This project was developed as a way to explore the idea of automated intraday market data collection. Most 3rd parties charge for such data which is why this project was ideated in the first place. The key workflow behind this project involves collecting extensive market data in batch processes using web scraping and building a database of historic intraday market data. Eventually, the goal is to create a completely automated ETL program which can extract data from multiple online resources, transform said data into useful heuristics and load all the data into a NoSQL MongoDB database on AWS. 

## Usage
This project is primarily built in python 3.7.1 and involves packages which need to be installed. To make getting started with this project easier, we've created a requirements.txt file which contains all the different python packages needed. You can utilize this file (after cloning this repository) by using the following command:

```
pip install -r requirements.txt
```

Following this step you can start using the project. We suggest starting with the main.py code.
