# Import the requisite packages
import datetime
from dateutil.relativedelta import relativedelta

class GetDates:
    
    # Class constructor
    def __init__(self):
        pass
    
    # Print current date
    def printdates(self):
        naivelocaltime = datetime.now()
        awarelocaltime = datetime.now(tz = datetime.timezone.utc)
        
        dateofinterest = awarelocaltime
        
        print(f"The local time is: {dateofinterest}")
        
        print(f"The date component is: {dateofinterest.date()}")
        print(f"The year is: {dateofinterest.year}")
        print(f"The month is: {dateofinterest.month}")
        print(f"The day is: {dateofinterest.day}")
        
        print(f"The time component without timezone is: {dateofinterest.time()}")
        print(f"The time component with timezone is: {dateofinterest.timetz()}")
        print(f"The hour is: {dateofinterest.hour}")
        print(f"The minute is: {dateofinterest.minute}")
        print(f"The microsecond is: {dateofinterest.microsecond}")
        print(f"The timezone is: {dateofinterest.tzinfo}")
        
    def printdates2(self):
        currentdate = datetime.date(year = 2020, month = 7, day = 30)
        timedeltainterval = datetime.timedelta(weeks = 4)
        relativedeltainterval = relativedelta(months = 1)

        timedeltadate = currentdate - timedeltainterval
        relativedeltadate = currentdate - relativedeltainterval
        
        # Print the date components
        print(f"The current date is: {currentdate} and is type: {type(currentdate)}")
        print(f"The timedelta date is: {timedeltadate} and is type: {type(timedeltadate)}")
        print(f"The relativedelta date is: {relativedeltadate} and is type: {type(relativedeltadate)}")

# Main execution point
if __name__ == "__main__":
    
    # Create date obtainer and print current time in timezones
    dateobtainer = GetDates()
    dateobtainer.printdates2()