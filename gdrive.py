#
# Copyright (c) 2020 by Alexis LEBEL. Released under MIT License
#

import pydrive
import credential
import json
import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


class GDrive():


    def __init__(self):
        self.folderHierarchy = json.loads(credential.folderHierarchy)
        gauth = GoogleAuth()
        gauth.LocalWebserverAuth()
        self.drive = GoogleDrive(gauth)
        return None

    def uploadFile(self, folderid, title):
        gFile = self.drive.CreateFile({'parents': [{'id': folderid}], 'title': title})
        gFile.SetContentFile('tempfile')
        gFile.Upload()
        os.remove('tempfile')
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
        self.updateFolderHierarchy()
        try:
            primaryFolderId = self.folderHierarchy['general_folder']['subfolders'][primaryFolder]['id']
        except:
            print('Index out of range')
            primaryFolderId = -1
        if secondaryFolder != None:
            try:
                folderId = self.folderHierarchy['general_folder']['subfolders'][primaryFolder]['subfolders'][secondaryFolder]['id']
            except:
                print("Index out of range")
                secondaryFolderId = -1
        else:
            secondaryFolderId = -1
            folderId = primaryFolderId
        return folderId

    def updateFolderHierarchy(self):
        self.folderHierarchy = json.loads(credential.folderHierarchy)
        for folder in self.folderHierarchy['general_folder']['subfolders']:
            folderId = folder['id']
            subfolders = self.getSubfolders(folderId)
            for sf in subfolders:
                folder['subfolders'].append({"id" : sf['id'], "displayName" : sf['title']})
        return None
