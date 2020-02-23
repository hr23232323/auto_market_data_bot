import datetime
from datetime import datetime as dt
import schedule
import time
from data_collector import collect_data

def time_is_between(min_time, max_time):
    current_time = dt.now().time()
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
    schedule.every(5).minutes.do(collect_data)

    # when to stop
    while (time_is_between(market_open, market_close)):
        schedule.run_pending()
        time.sleep(1)


def main():
    market_open = datetime.time(9,30,00)
    market_close = datetime.time(19,28,00)
    while 1:
        if(is_weekday()):
            if(time_is_between(market_open, market_close)):
                start_day(market_open, market_close)
                time.sleep(86340)
        else:
            # Sleep through the weekend, decrease processing
            time.sleep(86340)
            time.sleep(86340)

        time.sleep(1)


if __name__ == "__main__":
    main()
