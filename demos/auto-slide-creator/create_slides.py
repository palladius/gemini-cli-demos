
import os
import re
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# Define the scopes
SCOPES = ['https://www.googleapis.com/auth/presentations', 'https://www.googleapis.com/auth/drive.file']

def main():
    """Creates a Google Slides presentation."""
    # Always re-authenticate to ensure correct scopes are used.
    flow = InstalledAppFlow.from_client_secrets_file(
        'credentials.json', SCOPES)
    creds = flow.run_local_server(port=0)

    slides_service = build('slides', 'v1', credentials=creds)
    drive_service = build('drive', 'v3', credentials=creds)

    presentation = slides_service.presentations().create(body={
        'title': 'Gemini CLI Demos'
    }).execute()
    presentation_id = presentation.get('presentationId')
    
    # Delete the initial empty slide
    first_slide_id = presentation.get('slides')[0].get('objectId')
    slides_service.presentations().batchUpdate(presentationId=presentation_id, body={
        'requests': [{'deleteObject': {'objectId': first_slide_id}}]
    }).execute()

    # Add a single slide
    slide_id = "slide_0"
    title_id = "title_0"
    body_id = "body_0"
    placeholder_id_mappings = [
        {'layoutPlaceholder': {'type': 'TITLE'}, 'objectId': title_id},
        {'layoutPlaceholder': {'type': 'BODY'}, 'objectId': body_id}
    ]
    slide_requests = [
        {
            'createSlide': {
                'objectId': slide_id,
                'slideLayoutReference': {'predefinedLayout': 'TITLE_AND_BODY'},
                'placeholderIdMappings': placeholder_id_mappings
            }
        },
        {'insertText': {'objectId': title_id, 'text': 'Repository Intent'}},
        {'insertText': {'objectId': body_id, 'text': 'This repository contains Demos-in-a-box for `gemini-cli`.'}}
    ]

    # Add the logo to the first slide
    image_path = 'logo.png'
    if os.path.exists(image_path):
        file_metadata = {'name': os.path.basename(image_path)}
        media = MediaFileUpload(image_path, mimetype='image/png')
        image = drive_service.files().create(body=file_metadata, media_body=media, fields='id, webContentLink').execute()
        image_url = image.get('webContentLink')

        # Make the image publicly readable
        drive_service.permissions().create(fileId=image.get('id'), body={'type': 'anyone', 'role': 'reader'}).execute()
        
        slide_requests.append({
            'createImage': {
                'url': image_url,
                'elementProperties': {
                    'pageObjectId': slide_id,
                    'size': {
                        'height': {'magnitude': 2000000, 'unit': 'EMU'},
                        'width': {'magnitude': 2000000, 'unit': 'EMU'}
                    },
                    'transform': {
                        'scaleX': 1, 'scaleY': 1,
                        'translateX': 3500000, 'translateY': 1500000,
                        'unit': 'EMU'
                    }
                }
            }
        })

    if slide_requests:
        slides_service.presentations().batchUpdate(presentationId=presentation_id, body={'requests': slide_requests}).execute()

    print(f"Presentation created: https://docs.google.com/presentation/d/{presentation_id}")

if __name__ == '__main__':
    main()
