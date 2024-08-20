from datetime import datetime, timezone, timedelta
import math 
import argparse

def current_beattime(diff_from_UTC):
    # UTC +1 
    #diff_from_UTC = 1

    # Present day, Present time
    timeUTC = datetime.now(timezone.utc)

    # Present day, Present seconds
    present_second = timeUTC.hour * 3600 + timeUTC.minute * 60 + timeUTC.second + (timeUTC.microsecond / 1e6)

    # TimeZone application
    present_second = (present_second + (diff_from_UTC * 3600) + 86400)% 86400

    # Convert to beat
    beats = (present_second / 86400) * 1000

    # Round to 2 decimals
    beats = round(beats,2)

    return print(f'@{beats:.2f}')
current_beattime(1)