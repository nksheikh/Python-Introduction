from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

# Print datetime subcomponents
def printdetails(currentdatetime):
    print(f"The current date component is: {currentdatetime.date()}")
    print(f"The current date component is: {currentdatetime.year}")
    print(f"The current date component is: {currentdatetime.month}")
    print(f"The current date component is: {currentdatetime.day}")
    print(f"The current date component is: {currentdatetime.tzinfo}")
    
    print(f"The current time component is: {currentdatetime.time()}")
    print(f"The current time component is: {currentdatetime.timetz()}")
    print(f"The current time component is: {currentdatetime.hour}")
    print(f"The current time component is: {currentdatetime.minute}")
    print(f"The current time component is: {currentdatetime.second}")
    print(f"The current time component is: {currentdatetime.microsecond}")
    
# Display past and future dates
def printotherdates(currentdatetime):
    eastern_tz = ZoneInfo("America/New_York")
    currentdatetime = currentdatetime.astimezone(eastern_tz)
    delta = timedelta(weeks = 4)
    print(f"The day past was: {currentdatetime - delta}")
    print(f"The day future is: {currentdatetime + delta}")

if __name__ == "__main__":
    # Get the current time and print it
    currentdatetime = datetime.now()
    print(f"The current datetime is: {currentdatetime}")
    printdetails(currentdatetime)
    printotherdates(currentdatetime)