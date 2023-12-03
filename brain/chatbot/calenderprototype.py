import datetime
import time
from speak import speak2
# Sample event scheduling and reminder system
events = []

def schedule_event(event_name, event_date_time):
    event = {
        "name": event_name,
        "datetime": event_date_time,
    }
    events.append(event)
    print(f"Event '{event_name}' scheduled for {event_date_time}")

def send_reminder(event):
    current_time = datetime.datetime.now()
    event_time = event["datetime"]
    time_difference = event_time - current_time
    seconds_until_event = time_difference.total_seconds()
    
    if seconds_until_event <= 0:
        print(f"It's time for '{event['name']}'!")
    elif seconds_until_event <= 3600:  # Remind 1 hour before
        print(f"Reminder: '{event['name']}' in {int(seconds_until_event/60)} minutes")

# Example usage
schedule_event("Meeting with Client", datetime.datetime(2023, 9, 23, 14, 30))
schedule_event("Conference Call", datetime.datetime(2023, 9, 25, 10, 0))

while True:
    for event in events:
        send_reminder(event)
    time.sleep(60)  # Check for reminders every minute
