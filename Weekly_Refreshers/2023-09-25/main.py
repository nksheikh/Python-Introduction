# Import the requisite packages
from datetime import datetime, timezone
from modules import GetDates

# Main execution point
if __name__ == "__main__":
    
    # Create date obtainer and print current time in timezones
    dateobtainer = GetDates()
    dateobtainer.printdates(timezones = [timezone.utc])