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

    def createSubfolder(self, name:str, parent):
        folder_metadata = {'title' : name, 'mimeType' : 'application/vnd.google-apps.folder', 'parents': [{'id': parent}]}
        folder = self.drive.CreateFile(folder_metadata)
        folder.Upload()
        return None

    def getFileTitles(self, folderId):
        file_list = self.drive.ListFile({'q': f"'{folderId}' in parents"}).GetList()
        titlesList = ''
        i=0
        for file in file_list:
            titlesList += str(i) + ' - ' + file['title'] + '\n'
            i+=1
        return titlesList

    def parseFolderArgument(self, primaryFolder = -1, secondaryFolder = -1):
        folderId = -1
        self.updateFolderHierarchy()
        try:
            primaryFolderId = self.folderHierarchy['general_folder']['subfolders'][primaryFolder]['id']
            folderId = primaryFolderId
        except IndexError:
            print('Index out of range')
        except:
            print('Autre erreur')
        if secondaryFolder != -1:
            try:
                folderId = self.folderHierarchy['general_folder']['subfolders'][primaryFolder]['subfolders'][secondaryFolder]['id']
            except IndexError:
                print("Index out of range")
            except:
                print("Autre erreur")
        return folderId

    def updateFolderHierarchy(self):
        self.folderHierarchy = json.loads(credential.folderHierarchy)
        for folder in self.folderHierarchy['general_folder']['subfolders']:
            folderId = folder['id']
            subfolders = self.getSubfolders(folderId)
            for sf in subfolders:
                folder['subfolders'].append({"id" : sf['id'], "displayName" : sf['title']})
        return None
