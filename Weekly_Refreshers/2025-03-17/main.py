# Import the requisite packages
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
import requests
import json

def manipulatetz():
    # Get the aware timezone
    etz = ZoneInfo("America/New_York")
    currentdatetime = datetime.now(tz = etz)

    # Print the current datetime
    print(f"The current datetime is: {currentdatetime}")

    # Print everything about the datetime
    print(f"The current year is: {currentdatetime.year}")
    print(f"The current month is: {currentdatetime.month}")
    print(f"The current day is: {currentdatetime.day}")
    print(f"The current weekday is: {currentdatetime.weekday}")
    print(f"The current hour is: {currentdatetime.hour}")
    print(f"The current minute is: {currentdatetime.minute}")
    print(f"The current second is: {currentdatetime.second}")
    print(f"The current microsecond is: {currentdatetime.microsecond}")
    print(f"The current timezone is: {currentdatetime.tzinfo}")
