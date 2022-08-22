from service import drive_service

def CreateFolder(folderName, parentID):
    body = {'name': folderName,
    'mimeType': "application/vnd.google-apps.folder"}
    body['parents'] = [parentID]
    root_folder = drive_service().files().create(supportsTeamDrives=True,
    body = body).execute()
    return root_folder['id']
