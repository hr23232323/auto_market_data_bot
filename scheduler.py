import datetime
from datetime import datetime as dt
import schedule
import time

def time_is_between(min_time, max_time, to_check_time):
    if(to_check_time > min_time and to_check_time < max_time):
        print(to_check_time)
        print("YES")
    else:
        print("NO")

def collect_data():
    print(dt.now())
    print("COLLECTING DATA")

def start_day(market_open, market_close):
    schedule.every(10).seconds.do(collect_data)

    # when to stop
    current_time = dt.now().time()

    while (time_is_between(market_open, market_close, current_time)):
        schedule.run_pending()
        time.sleep(1)
        current_time = dt.now().time()


def main():
    market_open = datetime.time(9,30,00)
    market_close = datetime.time(16,52,00)
    current_time = dt.now().time()
    while 1:
        if(time_is_between(market_open, market_close, current_time)):
            start_day(market_open, market_close)
            time.sleep(180)
        time.sleep(1)
        current_time = dt.now().time()




if __name__ == "__main__":
    main()
