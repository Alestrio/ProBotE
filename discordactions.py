#
# Copyright (c) 2020 by Alexis LEBEL. Released under MIT License
#
import discord
from discord.ext import commands
import logging
import credential
import pronoteactions as pa


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


        return None

    async def on_ready(self):
        print('Succesfully logged in for Discord as {0.user}'.format(bot))

    async def on_message(self, message):
        if message.content.startswith('pro sync'):
            await self.updateChannel(self.pronote.getHomeworks())
        if message.content.startswith('pro introduce'):
            await self.introduceBot()

        return None

    async def updateChannel(self, homeworks):
        self.homework_channel = self.get_channel(credential.homework_channel)
        #self.homework_channel = self.get_channel(558616293134303284)
        await self.homework_channel.send("DEVOIRS :")
        for hw in homeworks:
            formattedMessage = hw[0]
            for file in hw[1]:
                formattedMessage +=  file.url + '\n'
            await self.homework_channel.send(formattedMessage)
            #await channel.send(hw)
        # await self.homework_channel.send("CONTENU DES COURS :")
        # for le in lessons:
        #     await self.homework_channel.send(le)
        return None

    async def introduceBot(self):
        self.homework_channel = self.get_channel(credential.homework_channel)
        await self.homework_channel.send('Bonjour ! \n ' +
        'Je suis un automate qui fait la liaison entre Discord, Pronote, et bientôt Google Drive ! \n' +
        'Voici mes commandes : \n' +
        '-pro sync : permet de récolter les devoirs sur une période de 15 jours, avec les liens des fichiers \n' +
        '-pro introduce : permet d\'afficher ce message \n' +
        'Bon courage ! \n ' +
        'PS : Mon code source est disponible ici : https://github.com/Alestrio/ProBotE')
        return None

bot = DiscordBot()
bot.run(credential.token)
