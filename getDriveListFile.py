from service import drive_service


def getList(folder_id):
    result = drive_service().files().list(supportsTeamDrives=True,
    includeTeamDriveItems=True,q=f"'{folder_id}' in parents and trashed = false",
    spaces='drive',pageSize=1000,fields='files(id, name, mimeType, size, shortcutDetails)',
    orderBy='folder, name').execute()
    return [c for c in [x for x in [result[i] for i in result][0]]]
