from __future__ import print_function
import datetime
import os.path

from speak import speak2  # Assuming this is your text-to-speech module
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.auth.transport.requests import Request

# Define the scopes for Google Calendar API
SCOPES = ['https://www.googleapis.com/auth/calendar']

def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            # If no credentials, or they are not valid, prompt the user to authorize the application.
            flow = InstalledAppFlow.from_client_secrets_file('brain/chatbot/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    
    try:
        # Build the Google Calendar service
        service = build('calendar', 'v3', credentials=creds)
    
        # Get the current time in ISO format
        now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        
        # Retrieve a list of upcoming events (maxResults=10)
        events_result = service.events().list(calendarId='primary', timeMin=now, maxResults=10, singleEvents=True, orderBy='startTime').execute()
        events = events_result.get('items', [])
        
        if not events:
            speak2("You have no upcoming events, Sir!")
            return
        
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            speak = (start, event['summary'])
            speak2(speak)
    except HttpError as error:
        print("An error occurred:", error)

if __name__ == "__main__":
    main()
