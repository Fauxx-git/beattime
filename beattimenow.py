from datetime import datetime, timezone, timedelta
import time

def current_beattime(diff_from_UTC):
        # UTC +1 
        

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

        return f'@{beats:.2f}'


#Output to JSON
if __name__ == "__main__":
    try:
        # Time Zone 
        diff_from_UTC = 1
        beat_time = current_beattime(diff_from_UTC)
        print(f'{{"text": "{beat_time}", "tooltip": "Current beat time"}}')
    except Exception as e:
        # In case of error, output empty JSON to avoid JSON errors in Waybar
        print('{"text": "Error", "tooltip": "Script error"}')