# Import the requisitive packages
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

# Create the DateTime practicing class
class DateTimePractice:
    
    # Main entry point
    def __init__(self, currentdatetime = None):
        
        # Initialize the current datetime
        if currentdatetime is None:
            self.currentdatetime = datetime.now(tz = timezone.utc)
        else:
            self.currentdatetime = currentdatetime
    
    # Print the datetime info
    def printdatetimeinfo(self):
        
        # Print the date component
        print(f"The date component is: {self.currentdatetime.date()}")
        print(f"The year is: {self.currentdatetime.year}")
        print(f"The month is: {self.currentdatetime.month}")
        print(f"The day is: {self.currentdatetime.day}")
        
        # Print the time component
        print(f"The time component is: {self.currentdatetime.time()}")
        print(f"The time component (with timezone) is: {self.currentdatetime.timetz()}")
        print(f"The hour is: {self.currentdatetime.hour}")
        print(f"The minute is: {self.currentdatetime.minute}")
        print(f"The second is: {self.currentdatetime.second}")
        print(f"The microsecond is: {self.currentdatetime.microsecond}")
        print(f"The timezone is: {self.currentdatetime.tzinfo}")
        
        # Localize the time to EDT and print the previous and future dates
        edt_tz = ZoneInfo("US/Eastern")
        currentdatetime_edt = self.currentdatetime.astimezone(edt_tz)
        timedeltainterval = timedelta(weeks = 4)
        futuredatetime = currentdatetime_edt + timedeltainterval
        previousdatetime = currentdatetime_edt - timedeltainterval
        print(f"Four weeks ago EDT was: {previousdatetime}")
        print(f"Four weeks ago EDT will be : {futuredatetime}")
        


# Main Execution Point
if __name__ == "__main__":
    dtp = DateTimePractice()
    dtp.printdatetimeinfo()
    
    