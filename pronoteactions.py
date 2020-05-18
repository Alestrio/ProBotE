#
# Copyright (c) 2020 by Alexis LEBEL. Released under MIT License
#
import os
import sys
import credential
import datetime
import pronotepy
from pronotepy.ent import ac_reims

class PronoteActions():

    def __init__(self):

        return None

    def getHomeworks(self):
        self.client = pronotepy.Client(credential.url, cookies=ac_reims(credential.username, credential.password))
        formattedHomeworks = []
        homeworks = self.client.homework(datetime.date.today(), (datetime.date.today() + datetime.timedelta(days=14)))
        for hw in homeworks:
            formattedHomeworks.append([hw.subject.name + " " + hw.date.strftime('%d - %m - %Y') + " ``` \n" + hw.description + "\n ```", hw.files])
        return formattedHomeworks

    def getLessons(self):
         formattedLessons = []
         self.client = pronotepy.Client(credential.url, cookies=ac_reims(credential.username, credential.password))
         lessons = self.client.lessons(datetime.date.today())
         print(lessons)
         for le in lessons:
             try:
                 formattedLessons.append(le.start.strftime('%d - %m - %Y') + '```\n' + le.content.description + '\n ```')
             except:
                print('no desc')
         return formattedLessons

    # def reSync(self):
    #
    #     return None
