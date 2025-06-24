

import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Define the scopes
SCOPES = ['https://www.googleapis.com/auth/presentations']

def main():
    """Creates a Google Slides presentation."""
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('slides', 'v1', credentials=creds)

    # Create the presentation
    presentation = service.presentations().create(body={
        'title': 'Gemini CLI Demos'
    }).execute()

    presentation_id = presentation.get('presentationId')

    # Add slides
    requests = [
        {
            'createSlide': {
                'objectId': 'title_slide',
                'slideLayoutReference': {
                    'predefinedLayout': 'TITLE'
                }
            }
        },
        {
            'insertText': {
                'objectId': 'title_slide',
                'text': 'Gemini CLI Demos',
                'insertionIndex': 0
            }
        },
        {
            'createSlide': {
                'objectId': 'intent_slide',
                'slideLayoutReference': {
                    'predefinedLayout': 'TITLE_AND_BODY'
                }
            }
        },
        {
            'insertText': {
                'objectId': 'intent_slide',
                'text': 'Repository Intent',
                'insertionIndex': 0
            }
        },
        {
            'insertText': {
                'objectId': 'intent_slide',
                'text': 'This repository contains Demos-in-a-box for Gemini CLI.',
                'insertionIndex': 1
            }
        },
        {
            'createSlide': {
                'objectId': 'auto_slide_creator_slide',
                'slideLayoutReference': {
                    'predefinedLayout': 'TITLE_AND_BODY'
                }
            }
        },
        {
            'insertText': {
                'objectId': 'auto_slide_creator_slide',
                'text': 'Auto Slide Creator',
                'insertionIndex': 0
            }
        },
        {
            'insertText': {
                'objectId': 'auto_slide_creator_slide',
                'text': 'This demo showcases how `gemini-cli` is able to:\n\n* Create Google Slides\n* Generate E/R schema based on it.',
                'insertionIndex': 1
            }
        },
        {
            'createSlide': {
                'objectId': 'git_investigation_slide',
                'slideLayoutReference': {
                    'predefinedLayout': 'TITLE_AND_BODY'
                }
            }
        },
        {
            'insertText': {
                'objectId': 'git_investigation_slide',
                'text': 'Git Investigation',
                'insertionIndex': 0
            }
        },
        {
            'insertText': {
                'objectId': 'git_investigation_slide',
                'text': 'This demo will showcase git investigation capabilities.',
                'insertionIndex': 1
            }
        },
        {
            'createSlide': {
                'objectId': 'sqlite_investigation_slide',
                'slideLayoutReference': {
                    'predefinedLayout': 'TITLE_AND_BODY'
                }
            }
        },
        {
            'insertText': {
                'objectId': 'sqlite_investigation_slide',
                'text': 'SQLite Investigation',
                'insertionIndex': 0
            }
        },
        {
            'insertText': {
                'objectId': 'sqlite_investigation_slide',
                'text': 'This demo showcases how `gemini-cli` is able to:\n* read/write/understand a sqlite3.\n* Generate E/R schema based on it.',
                'insertionIndex': 1
            }
        }
    ]

    body = {
        'requests': requests
    }
    response = service.presentations().batchUpdate(
        presentationId=presentation_id, body=body).execute()
    print(f"Created presentation with ID: {presentation_id}")

if __name__ == '__main__':
    main()

