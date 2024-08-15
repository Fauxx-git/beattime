from datetime import datetime, timezone, timedelta
import math 
import argparse


def current_beattime(diff_from_UTC):
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

    return beats

def beat_to_UTC(beats):
 
    # Beats to seconds
    time_seconds = (beats / 1000) * 86400
 
    # Use seconds to make hours
    beat_hours = math.floor(time_seconds / 3600)

    # Remove hours from second using mod (Thanks Punp)
    beat_minutes = math.floor((time_seconds % 3600) / 60)

    # Another mod to remove minutes from seconds
    beat_seconds = math.floor(time_seconds % 60)

    # Modify hours to the timezone  (here you instert your timezone mine is UTC+1)
    beat_hours = (beat_hours + 24 + 1) % 24

    return f"Hours:{beat_hours},Minutes:{beat_minutes},Seconds:{beat_seconds}"


# All of this is for running it in the terminal with options
# Argument parser setup
parser = argparse.ArgumentParser(description="Beat time teller and Converter")
parser.add_argument("-b", "--beats", type=float, help="Convert beats to UTC time.")
parser.add_argument("-tz", "--timezone", type=int, default=1, help="Timezone difference from UTC. Default is UTC+1.")

args = parser.parse_args()

if args.beats is not None:
    # If the user provides beats, convert it to UTC
    result = beat_to_UTC(args.beats)
    print(result)
else:
    # Otherwise, print the current beat time
    result = current_beattime(args.timezone)
    print(f'@{result:.2f}')



