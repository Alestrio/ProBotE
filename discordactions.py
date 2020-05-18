#
# Copyright (c) 2020 by Alexis LEBEL. Released under MIT License
#
import discord
from discord.ext import commands
import logging
import credential
import pronoteactions as pa
import gdrive


class DiscordBot(commands.Bot):


    def __init__(self, *args, **kwargs):
        super().__init__(command_prefix='?',*args, **kwargs)
        logging.basicConfig(level=logging.ERROR)
        logger = logging.getLogger('discord')
        logger.setLevel(logging.ERROR)
        handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
        handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
        logger.addHandler(handler)

        self.homework_channel = self.get_channel(credential.homework_channel)
        self.lessons_channel = 0
        self.pronote = pa.PronoteActions()
        self.drive = gdrive.GDrive()

        return None

    async def on_ready(self):
        print('Succesfully logged in for Discord as {0.user}'.format(bot))

    async def on_message(self, message):
        if message.content.startswith('pro sync'):
            await self.updateChannel(self.pronote.getHomeworks(), self.pronote.getLessons())
        if message.content.startswith('pro introduce'):
            await self.introduceBot()
        if message.content.startswith('pro dossiers'):
            await self.sendFolderHierarchy()
        if message.content.startswith('pro upload'):
            splittedMsg = message.content.split(' ')
            if len(splittedMsg) > 4:
                self.sendUploadCommandErrorMsg()
            else:
                att = message.attachments[0]
                await att.save('tempfile')
                title = att.filename
                if len(splittedMsg) == 3:
                    folderId = self.drive.parseFolderArgument(splittedMsg[2], -1)
                    if folderId != None:
                        self.drive.uploadFile(folderID, title)
                        await self.sendUploadOkMsg()
                    else:
                        self.sendUploadCommandErrorMsg()
                elif len(splittedMsg) == 2:
                    self.drive.uploadFile(file, credential.general_folder)
                    await self.sendUploadOkMsg()
                else:
                    folderId = self.drive.parseFolderArgument(int(splittedMsg[2]), int(splittedMsg[3]))
                    print(folderId)
                    if folderId != None:
                        self.drive.uploadFile(folderId, title)
                        await self.sendUploadOkMsg()
                    else:
                        self.sendUploadCommandErrorMsg()

        return None


    async def updateChannel(self, homeworks, lessons):
        self.homework_channel = self.get_channel(credential.homework_channel)
        await self.homework_channel.send("DEVOIRS :")
        for hw in homeworks:
            formattedMessage = hw[0]
            for file in hw[1]:
                formattedMessage +=  file.url + '\n'
            await self.homework_channel.send(formattedMessage)
        await self.homework_channel.send("CONTENU DES COURS :")
        for le in lessons:
             formattedMessage = le[0]
             if le[1] != None:
                 for file in le[1]:
                     formattedMessage +=  file.url + '\n'
             #print(formattedMessage)
             await self.homework_channel.send(formattedMessage)
        return None

    async def introduceBot(self):
        self.homework_channel = self.get_channel(credential.homework_channel)
        await self.homework_channel.send('Bonjour ! \n ' +
        'Je suis un automate qui fait la liaison entre Discord, Pronote, et Google Drive ! \n' +
        'Voici mes commandes : \n' +
        '-pro sync : permet de récolter les devoirs sur une période de 15 jours, avec les liens des fichiers \n' +
        '-pro introduce : permet d\'afficher ce message \n' +
        '-pro dossiers : permet d\'afficher la liste des dossiers sous forme d\'arbre \n' +
        '-pro upload : permet de téléverser un fichier vers google drive (usage : pro upload [dossier matière] [sous dossier]) \n' +
        'Bon courage ! \n ' +
        'PS : Mon code source est disponible ici : https://github.com/Alestrio/ProBotE')
        return None

    async def sendUploadCommandErrorMsg(self):
        homework_channel = self.get_channel(credential.homework_channel)
        await homework_channel.send('Oups, il semblerait qu\'il y ait un problème avec votre commande ! :/ \n'+
                                    'Voici la structure des dossiers, peut être que vous pourrez corriger votre commande grâce à elle !')
        await self.sendFolderHierarchy()
        return None

    async def sendUploadOkMsg(self):
        homework_channel = self.get_channel(credential.homework_channel)
        await homework_channel.send('Fichier envoyé !')
        return None

    async def sendFolderHierarchy(self):
        self.homework_channel = self.get_channel(credential.homework_channel)
        self.drive.updateFolderHierarchy()
        fh = self.drive.folderHierarchy
        message = 'Voici l\'arbre des dossiers du Drive : \n'
        i = 0
        for folder in fh['general_folder']['subfolders']:
            message += str(i) + ' - ' + folder['displayName'] + '\n'
            i += 1
            j = 0
            for subf in folder['subfolders']:
                message += '    ' + str(j) + ' - ' + "".join(subf["displayName"]) + '\n'
                j += 1
        await self.homework_channel.send(message)
        return None

bot = DiscordBot()
bot.run(credential.token)
