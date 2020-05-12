import pydrive
import credential
import json
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


class GDrive():


    def __init__(self):
        self.folderHierarchy = json.loads(credential.folderHierarchy)
        gauth = GoogleAuth()
        gauth.LocalWebserverAuth()
        self.drive = GoogleDrive(gauth)
        return None

    def uploadFile(self, file, folderid):
        gFile = self.drive.CreateFile({'parents': [{'id': folderid}]})
        gFile.setContentFile(file)
        gFile.upload()
        return None

    def getSubfolders(self, folderId):
        kwargs = {"q" : "",
                "parents" : [{"id": folderId}]}
        subfolders = self.drive.ListFile({'q': f"'{folderId}' in parents and trashed=false and mimeType=\'application/vnd.google-apps.folder\'"}).GetList()
        return subfolders

    def createSubfolder(self, name:str):

        return None

    def parseFolderArgument(self, primaryFolder:str, secondaryFolder:str):

        return None

    def updateFolderHierarchy(self):
        ## TODO clear before updating
        for folder in self.folderHierarchy['general_folder']['subfolders']:
            print(folder['displayName'])
            folderId = folder['id']
            subfolders = self.getSubfolders(folderId)
            for sf in subfolders:
                print("""{"id" : "%s", "displayName" : "%s"}""" % (sf['id'], sf['title']))
                print(sf['title'])
                folder['subfolders'].append({"id" : sf['id'], "displayName" : sf['title']})
        return None
