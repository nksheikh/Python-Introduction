# Import requisitive packages
from datetime import datetime, timezone

class GetDates:
    
    # Class constructor
    def __init__(self):
        pass
    
    # Print current date
    def printdates(self, timezones):
        
        # Loop through all desired timezones and print the current time in each timezone
        for tz in timezones:
            
            # Obtain and print the current time in the timezone
            currentdatetime = datetime.now(tz = tz)
            print(currentdatetime)