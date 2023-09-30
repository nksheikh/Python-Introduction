# Import the requisite package
from datetime import date, datetime, timezone
import zoneinfo

# Create the class
class DatePractice:
    
    # Weeday mappings
    weekdaymappings = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday"
    }
    
    # Construct the class
    def __init__(self):
        self.currentdatetime = datetime.now(timezone.utc)
        self.currentdate = date.today()
        
    # To some datetime manipulation
    def printdatetimeinfo(self, selecteddatetime = None):
        
        # Grab the class attribute currentdatetime if no date is especified
        if selecteddatetime is None:
            selecteddatetime = self.currentdatetime
        
        # Print the date information
        print(f"The date component is: {selecteddatetime.date()}")
        print(f"The year is: {selecteddatetime.year}")
        print(f"The month is: {selecteddatetime.month}")
        print(f"The day is: {selecteddatetime.day}")
        print(f"The weekday number is: {selecteddatetime.weekday()} which is a {self.weekdaymappings[selecteddatetime.weekday()]}")
        
        # Print the time information
        print(f"The time component is: {selecteddatetime.timetz()}")
        print(f"The hour is: {selecteddatetime.hour}")
        print(f"The second is: {selecteddatetime.second}")
        print(f"The microsecond is: {selecteddatetime.microsecond}")
        print(f"The timzone is: {selecteddatetime.tzinfo}")
        
    # Print date in different timezones
    def printdatetimetzs(self, selecteddatetime = None, tzstrlist = None):
        
        # Grab the class attribute currentdatetime if no date is especified
        if selecteddatetime is None:
            selecteddatetime = self.currentdatetime
        
        # If timezones have not been provided, then let's create a default list
        if tzstrlist is None:
            timezones = ["US/Eastern", "Asia/Bishkek"]
            
        # Create and localize the time to the selected times instead
        for tzstr in tzstrlist:
            tz = zoneinfo.ZoneInfo(tzstr)
            print(f"The current datetime is {selecteddatetime} and the modified datetime in the {tzstr} timezone is {selecteddatetime.astimezone(tz)}")
        
    # Parse some strings
    def parsestr(self, strdates = None):
        
        # Ensure that dates is not mutated
        if strdates is None:
            strdates = []
        
        # Parse each date
        for datestr in strdates:
            print(f"The parse string is: {datetime.strptime(datestr, '%Y-%m-%d').date()}")
            
# Create the user entry class
class UserEntry:
    
    # Create the constructor
    def __init__(self, specialphrase = "Special Phrase"):
        self.specialphrase = specialphrase
        
    # Prompt until valid response acheived
    def prompt():
        
        # 
        entryvalid = False
        
        # 
        
        return 0
    
    # Validate use entry
    def getnumber(self):
        
        # Ask user for input and parse for validity
        try:
            
            # Get th e number from the user
            num = input("Please type in your first number: ")
            
            # Check if response is special phrase, otherwise treat as a number
            if num == self.specialphrase:
                print("You entered the special phrase! No addition needed.")
                return None
            else:
                return float(num)
                
        except Exception as e:
            print(f"ERROR MESSAGE: {str(e)}.")
        
        # If all fails then an error must have occured.
        return ""
        

# Main execution point
if __name__ == "__main__":
    
    # Instantiate the DatePractice class and print the details
    try:
        # Date practice
        datepractice = DatePractice()
        datepractice.printdatetimeinfo()
        datepractice.printdatetimetzs(tzstrlist = ["US/Eastern", "Asia/Bishkek"])
        datepractice.parsestr(["2023-09-30", "2023-10-01"])
        
        # User entry
        userentry = UserEntry()
        userentry.prompt()
        
    except Exception as e:
        print(f"ERROR MESSAGE: {str(e)}")
        