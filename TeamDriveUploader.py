import pickle, email, os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.http import MediaFileUpload


def SetType(filepath):
    mimetype = email.message_from_bytes(open(filepath, "rb").read()).get_content_type()
    return mimetype


def drive_service():
    creds = None
    try:
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    except:
        pass
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', 
            ['https://www.googleapis.com/auth/drive.metadata.readonly','https://www.googleapis.com/auth/drive.file'])
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    return build('drive', 'v3', credentials=creds)


def uploadFile(filename, filepath, folderid):
    mimetype = SetType(filepath)
    file_metadata = {'name': filename,"parents": [folderid]}
    media = MediaFileUpload(filepath,mimetype=mimetype)
    file = drive_service().files().create(supportsTeamDrives=True,
    body=file_metadata,
    media_body=media,fields='id').execute()
    return file



uploadFile('filename', 'filepath', 'folderid')
