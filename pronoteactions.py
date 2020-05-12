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
        self.client = pronotepy.Client(credential.url, cookies=ac_reims(credential.username, credential.password))
        if self.client.logged_in:
            messages = self.client.messages()
        else:
            print('no login')
        return None

    def getHomeworks(self):
        formattedHomeworks = []
        if self.client.logged_in:
            homeworks = self.client.homework(datetime.date.today(), (datetime.date.today() + datetime.timedelta(days=14)))
            for hw in homeworks:
                formattedHomeworks.append([hw.subject.name + " " + hw.date.strftime('%d - %m - %Y') + " ``` \n" + hw.description + "\n ```", hw.files])
        else:
            self.client = pronotepy.Client(credentials.url, cookies=ac_reims(credentials.username, credentials.password))
            homeworks = self.client.homework(datetime.date.today())
            for hw in homeworks:
                formattedHomeworks.append([hw.subject.name + " " + hw.date.strftime('%d - %m - %Y') + " ``` \n" + hw.description + "\n ```", hw.files])
        return formattedHomeworks

    # def getLessons(self):
    #     formattedLessons = []
    #     if self.client.logged_in:
    #         lessons = self.client.lessons(datetime.date.today())
    #         print(lessons)
    #         if lessons != None:
    #             for le in lessons:
    #                 print(le.id)
    #                 if not le.content == None:
    #                     print(le.start, le.content().description)
    #                      formattedLessons.append(le.start.strftime('%d - %m - %Y') + '```\n' + le.content.description + '\n ```')
    #                  else:
    #                      print(le.start, le.content.title, le.content.descriptif)
    #      else:
    #          self.client = pronotepy.Client(credentials.url, cookies=ac_reims(credentials.username, credentials.password))
    #          lessons = self.client.lessons(datetime.date.today())
    #          print(lessons)
    #          if lessons != None:
    #              for le in lessons:
    #                  if le != None and le.content != None:
    #                      formattedLessons.append(le.start.strftime('%d - %m - %Y') + '```\n' + le.content.description + '\n ```')
    #         return None

    def reSync(self):

        return None
