import datetime
from datetime import datetime as dt
import schedule
import time
from data_collector import collect_data

def time_is_between(min_time, max_time):
    to_check_time = dt.now().time()
    if(to_check_time > min_time and to_check_time < max_time):
        return True
    else:
        return False

def is_weekday():
    if(dt.now().isoweekday() in range(1, 6)):
        return True
    else:
        return False


def start_day(market_open, market_close):
    print("MARKET STARTED")
    print(dt.now())
    collect_data()
    schedule.every(5).minutes.do(collect_data)

    # when to stop
    while (time_is_between(market_open, market_close)):
        schedule.run_pending()
        time.sleep(1)


def main():
    market_open = datetime.time(9,00,00)
    market_close = datetime.time(16,00,00)
    while 1:
        if(is_weekday()):
            # If weekend and within market window, start day
            if(time_is_between(market_open, market_close)):
                start_day(market_open, market_close)
                # Sleep till start of market next day, print message
                # in middle to signal the process is running correctly
                time.sleep(40000)
                print("COMPLETED DATE")
                print(dt.now())
                time.sleep(40000)
        else:
            # Sleep through the weekend, decrease processing
            print("Weekend- day 1 sleep")
            time.sleep(82000)
            print("Weekend- day 2 sleep")
            time.sleep(82000)

        time.sleep(1)


if __name__ == "__main__":
    main()
