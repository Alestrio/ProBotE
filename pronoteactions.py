#
# Copyright (c) 2020 by Alexis LEBEL. Released under MIT License
#
import os
import requests
import sys
import credentials
import datetime

class PronoteActions():

    def __init__(self):
        self.isLoggedIn = False
        r = requests.post('http://127.0.0.1:21727/', json={"type": "login", "username": credentials.username, "password": credentials.password, "url": credentials.url, "cas": credentials.cas})
        data = r.json()
        if data['success'] == True:
            print("Succesfully logged in for Pronote")
            self.isLoggedIn = True
        elif data['error'] == "Mauvais identifiants":
            print('Error : wrong credentials')
        return None

    def getHomeworks(self):
        homeworks = []
        if self.isLoggedIn:
            for i in range(len(data['homeworks'])):
                subject = data['homeworks'][i]['subject']
                dueDate = datetime.datetime.fromtimestamp(data['homeworks'][i]['until']).strftime('%d-%m-%Y')
                content = data['homeworks'][i]['content']
                files = data['homeworks'][i]['files']
                homeworks.append([dueDate, subject, content, files])
        return None

    def reconnect(self):
        self.isLoggedIn = False
        r = requests.post('http://127.0.0.1:21727/', json={"type": "login", "username": credentials.username, "password": credentials.password, "url": credentials.url, "cas": credentials.cas})
        data = r.json()
        if data['success'] == True:
            print("Succesfully logged in for Pronote")
            self.isLoggedIn = True
        elif data['error'] == "Mauvais identifiants":
            print('Error : wrong credentials')
        return None
