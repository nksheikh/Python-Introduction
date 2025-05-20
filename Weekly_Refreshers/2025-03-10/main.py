# Import the requisite packages
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

# Create the class
class DateTimeDemo:
    def __init__(self, currentdatetime = datetime.now()):
        self.currentdatetime = currentdatetime
        
    def printcurrentdatetime(self):
        
        # Print the full datetime
        print(f"The current datetime is : {self.currentdatetime}")
        
        # Print the current date information
        print(f"The current date is : {self.currentdatetime.date()}")
        print(f"The current timezone is : {self.currentdatetime.tzinfo}")
        print(f"The current year is : {self.currentdatetime.year}")
        print(f"The current month is : {self.currentdatetime.month}")
        print(f"The current day is : {self.currentdatetime.day}")
        
        # Print the time components
        print(f"The current hour is : {self.currentdatetime.hour}")
        print(f"The current minute is : {self.currentdatetime.minute}")
        print(f"The current second is : {self.currentdatetime.second}")
        print(f"The current microsecond is : {self.currentdatetime.microsecond}")
        
    def modifytime(self):
        modifieddatetime = self.currentdatetime.astimezone(ZoneInfo("America/New_York"))
        utcdatetime = self.currentdatetime.astimezone(ZoneInfo("UTC"))
        print(f"The current datetime adjusted for timezone is: {modifieddatetime}")
        print(f"The datetime 28 days from now is: {modifieddatetime - timedelta(days = 28)}")
        print(f"The UTC time is: {utcdatetime}")
                      
if __name__ == "__main__":
    dtd = DateTimeDemo()
    dtd.modifytime()