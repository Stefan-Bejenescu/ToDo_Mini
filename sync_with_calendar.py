import os.path
import datetime as dt

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from flask import Flask, request, jsonify

SCOPES = ['https://www.googleapis.com/auth/calendar']
CREDENTIALS_FILE = 'credentials.json'
TOKEN_FILE = 'token.json'

app = Flask(__name__)

def authenticate_to_google():
    creds = None

    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        
        with open(TOKEN_FILE, "w") as token:
            token.write(creds.to_json())
    
    try:
        service = build("calendar", "v3", credentials=creds)
        return service
    except HttpError as error:
        print("An error occurred: ", error)
        return None

def add_event_to_calendar(service, event):
    event_result = service.events().insert(
        calendarId="primary", body=event).execute()
    
    print(f"Event created: {event_result['htmlLink']}")

def main():
    service = authenticate_to_google()
    add_event_to_calendar(service)

@app.route('/sync', methods=['POST'])
def sync_tasks():
    service = authenticate_to_google()

    tasks = request.get_json().get("tasks")

    if not tasks:
        return jsonify({"error": "No tasks provided to sync."}), 400

    events = []

    for task in tasks:
        task_name = task.get('name')
        due_date = task.get('due_date')

        start_time = f"{due_date}T09:00:00Z"
        end_time = f"{due_date}T10:00:00Z"

        event = {
            "summary": task_name,
            "start": {
                "dateTime": start_time,
                "timeZone": "Europe/Bucharest"
            },
            "end": {
                "dateTime": end_time,
                "timeZone": "Europe/Bucharest"
            }
        }

        events.append(event)

    for event in events:
        events_result = service.events().list(
            calendarId='primary', timeMin=event['start']['dateTime'], timeMax=event['end']['dateTime'],
            q=event["summary"], singleEvents=True, orderBy="startTime"
        ).execute()

        google_events = events_result.get('items', [])
        if not google_events:
            add_event_to_calendar(service, event)
    
    return jsonify({"message": "Tasks synced succesfully to Google Calendar"}), 200

if __name__ == "__main__":
    app.run(port=5000)