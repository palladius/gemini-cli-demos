
import os
import re
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# Define the scopes
SCOPES = ['https://www.googleapis.com/auth/presentations', 'https://www.googleapis.com/auth/drive.file']

def find_image_for_demo(demo_name):
    """Finds an image for a given demo."""
    demo_path = os.path.join('..', demo_name)
    if os.path.isdir(demo_path):
        # Prioritize 'image.png'
        specific_image_path = os.path.join(demo_path, 'image.png')
        if os.path.exists(specific_image_path):
            return specific_image_path
        
        # Look for any other png that is not a logo
        for root, _, files in os.walk(demo_path):
            for file in files:
                if file.endswith(".png") and "logo" not in file:
                    return os.path.join(root, file)

    # Fallback to a logo in the assets directory if it exists
    assets_logo = os.path.join('..', '..', 'assets', 'logo.png')
    if os.path.exists(assets_logo):
        return assets_logo
    return None

def create_formatted_text_requests(object_id, text):
    """
    Creates a list of requests to insert text and apply formatting for
    bullet points and backticks.
    """
    requests = [{'insertText': {'objectId': object_id, 'text': text}}]
    
    formatting_requests = []
    
    # Find all matches for backticks and bullets
    backtick_matches = list(re.finditer(r'`([^`]+)`', text))
    bullet_matches = list(re.finditer(r'^\* (.*)', text, re.MULTILINE))
    
    all_matches = []
    for m in backtick_matches:
        all_matches.append({'type': 'backtick', 'match': m})
    for m in bullet_matches:
        all_matches.append({'type': 'bullet', 'match': m})
        
    all_matches.sort(key=lambda x: x['match'].start(), reverse=True)
    
    for item in all_matches:
        match = item['match']
        start, end = match.span()
        
        if item['type'] == 'backtick':
            # Apply style to the text inside backticks
            formatting_requests.append({
                'updateTextStyle': {
                    'objectId': object_id,
                    'textRange': {'type': 'FIXED_RANGE', 'startIndex': start + 1, 'endIndex': end - 1},
                    'style': {'fontFamily': 'Courier New'},
                    'fields': 'fontFamily'
                }
            })
            # Delete the backticks
            formatting_requests.append({'deleteText': {'objectId': object_id, 'textRange': {'type': 'FIXED_RANGE', 'startIndex': end - 1, 'endIndex': end}}})
            formatting_requests.append({'deleteText': {'objectId': object_id, 'textRange': {'type': 'FIXED_RANGE', 'startIndex': start, 'endIndex': start + 1}}})
        
        elif item['type'] == 'bullet':
            # Create bullets for the paragraph
            formatting_requests.append({
                'createParagraphBullets': {
                    'objectId': object_id,
                    'textRange': {'type': 'FIXED_RANGE', 'startIndex': start, 'endIndex': end},
                    'bulletPreset': 'BULLET_DISC_CIRCLE_SQUARE'
                }
            })
            # Delete the '* ' marker
            formatting_requests.append({'deleteText': {'objectId': object_id, 'textRange': {'type': 'FIXED_RANGE', 'startIndex': start, 'endIndex': start + 2}}})
            
    requests.extend(formatting_requests)
    return requests

def main():
    """Creates a Google Slides presentation."""
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

    slides_data = [
        {
            'objectId': 'intent_slide',
            'layout': 'TITLE_AND_BODY',
            'title': 'Repository Intent',
            'body': 'This repository contains Demos-in-a-box for `gemini-cli`.'
        },
        {
            'objectId': 'auto_slide_creator_slide',
            'layout': 'TITLE_AND_BODY',
            'title': 'Auto Slide Creator',
            'body': 'This demo showcases how `gemini-cli` is able to:\n\n* Create Google Slides\n* Generate E/R schema based on it.'
        },
        {
            'objectId': 'git_investigation_slide',
            'layout': 'TITLE_AND_BODY',
            'title': 'Git Investigation',
            'body': 'This demo will showcase `git` investigation capabilities.'
        },
        {
            'objectId': 'sqlite_investigation_slide',
            'layout': 'TITLE_AND_BODY',
            'title': 'SQLite Investigation',
            'body': 'This demo showcases how `gemini-cli` is able to:\n* read/write/understand a `sqlite3` database.\n* Generate E/R schema based on it.'
        },
        {
            'objectId': 'thank_you_slide',
            'layout': 'TITLE_AND_BODY',
            'title': 'Thank you!',
            'body': 'Generated by `gemini-cli` + `auto-slide-creator`'
        }
    ]

    slide_requests = []
    for i, slide in enumerate(slides_data):
        slide_id = f"slide_{i}"
        title_id = f"title_{i}"
        body_id = f"body_{i}"

        placeholder_id_mappings = [
            {'layoutPlaceholder': {'type': 'TITLE'}, 'objectId': title_id},
            {'layoutPlaceholder': {'type': 'BODY'}, 'objectId': body_id}
        ]

        slide_requests.append({
            'createSlide': {
                'objectId': slide_id,
                'slideLayoutReference': {'predefinedLayout': slide['layout']},
                'placeholderIdMappings': placeholder_id_mappings
            }
        })

        if slide['title']:
            slide_requests.append({'insertText': {'objectId': title_id, 'text': slide['title']}})
        
        if slide['body']:
            slide_requests.extend(create_formatted_text_requests(body_id, slide['body']))

        demo_name = slide['objectId'].replace('_slide', '')
        image_path = find_image_for_demo(demo_name)

        if image_path and os.path.exists(image_path):
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
