#
# Copyright (c) 2020 by Alexis LEBEL. Released under MIT License
#
import credential
import datetime
import pronotepy
from pronotepy.ent import ac_reims
import unittest


class PronoteActions():

    def __init__(self):

        return None

    def getHomeworks(self):
        self.client = pronotepy.Client(credential.url, cookies=ac_reims(credential.username, credential.password))
        formattedHomeworks = []
        homeworks = self.client.homework(datetime.date.today(), (datetime.date.today() + datetime.timedelta(days=14)))
        for hw in homeworks:
            formattedHomeworks.append([hw.subject.name + " " + hw.date.strftime('%d - %m - %Y') + " ``` \n" + hw.description + "\n ```", hw.files])
        #print(formattedHomeworks)
        return formattedHomeworks

    def getLessons(self):
         formattedLessons = []
         #self.client = pronotepy.Client(credential.url, cookies=ac_reims(credential.username, credential.password)) # Switch to getLessonsAndReconnect if a day I need that.
         lessons = self.client.lessons(datetime.date.today(), (datetime.date.today() + datetime.timedelta(days=14)))
         #print(lessons)
         for le in lessons:
             try:
                 try:
                     formattedLessons.append([le.start.strftime('%d - %m - %Y') + ' - ' + le.subject.name + '```' + le.content.description + '\n ```', le.content.files])
                 except:
                     #print('no files')
                     formattedLessons.append([le.start.strftime('%d - %m - %Y') + ' - ' + le.subject.name + '```' + le.content.description + '\n ```', None])
             except:
                #print('no desc') # Do not forget to except as lessons can be blank (why ?.... IdK....)
                break

         return formattedLessons

    def reConnect(self):
     self.client = pronotepy.Client(credential.url, cookies=ac_reims(credential.username, credential.password))
     return None

class PronoteTest(unittest.TestCase):

    def testHomeworksFetching(self):
        pronote = PronoteActions()
        self.assertTrue(len(pronote.getHomeworks()) > 0, "no homeworks")

    def testLessonsFetching(self):
        pronote = PronoteActions()
        pronote.reConnect()
        self.assertTrue(len(pronote.getLessons()) > 0, 'no lessons')

if __name__ == '__main__':
    unittest.main()
