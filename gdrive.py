import pydrive


class GDrive():
    drive = 0

    def __init__(self):
        gauth = pydrive.auth.GoogleAuth()
        gauth.LocalWebServerAuth()
        drive = pydrive.drive.GoogleDrive(gauth)
        return None

    def uploadFile(self, file, folderid):
        gFile = drive.CreateFile({'parents': [{'id': folderid}]})
        gFile.setContentFile(file)
        gFile.upload()
        return None

    def getSubfolders(self):

        return None

    def createSubfolder(self, name:str):

        return None
