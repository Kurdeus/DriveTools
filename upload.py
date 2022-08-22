from service import SetType, MediaFileUpload, drive_service


def uploadFile(filename, filepath, folderid):
    mimetype = SetType(filepath)
    file_metadata = {'name': filename,"parents": [folderid]}
    media = MediaFileUpload(filepath,mimetype=mimetype)
    file = drive_service().files().create(supportsTeamDrives=True,
    body=file_metadata,
    media_body=media,fields='id').execute()
    return file
