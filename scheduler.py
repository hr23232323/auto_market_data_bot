import datetime
from datetime import datetime as dt
import schedule



def time_is_between(min_time, max_time, to_check_time):
    if(to_check_time > min_time and to_check_time < max_time):
        print("YES")
    else:
        print("NO")

def collect_data():
    print(dt.now())
    print("COLLECTING DATA")

def start_day():
    schedule.every(1).minutes.do(collect_data)

    # when to stop
    market_open = datetime.time(9,30,00)
    market_close = datetime.time(17,00,00)
    while (time_is_between(market_open, market_close, current_time)):
        schedule.run_pending()
        time.sleep(1)
        current_time = dt.now().time()


def main():
    schedule.




if __name__ == "__main__":
    main()
