#
# Copyright (c) 2020 by Alexis LEBEL. Released under MIT License
#

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
        subfolders = self.drive.ListFile({'q': f"'{folderId}' in parents and trashed=false and mimeType=\'application/vnd.google-apps.folder\'"}).GetList()
        return subfolders

    # def createSubfolder(self, name:str):
    #
    #     return None

    # def getFileTitles(self):
    #
    #     return None

    def parseFolderArgument(self, primaryFolder:int, secondaryFolder:int):
        self.updateFolderHierarchy
        try:
            primaryFolderId = self.folderHierarchy['general_folder']['subfolders'][primaryFolder]
        except:
            print('Index out of range')
            primaryFolderId = -1
        if secondaryFolder != None:
            try:
                secondaryFolderId = self.folderHierarchy['general_folder']['subfolders'][primaryFolder]['subfolders'][secondaryFolder]
            except:
                print("Index out of range")
                secondaryFolderId = -1
        else:
            secondaryFolderId = -1
        return (primaryFolderId, secondaryFolderId)

    def updateFolderHierarchy(self):
        self.folderHierarchy = credential.folderHierarchy
        for folder in self.folderHierarchy['general_folder']['subfolders']:
            folderId = folder['id']
            subfolders = self.getSubfolders(folderId)
            for sf in subfolders:
                folder['subfolders'].append({"id" : sf['id'], "displayName" : sf['title']})
        return None
