import schedule
import time
import datetime

def Display():
    print("jay Ganesh..! ",datetime.datetime.now())  # show current time

def main():
    print("Automation print started")

    schedule.every(10).second.do(Display)

    while True:
        schedule.run_pending()
        time.sleep(1)

    print("End of automation script")
if __name__=="__main__":
    main()
