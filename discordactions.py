#
# Copyright (c) 2020 by Alexis LEBEL. Released under MIT License
#
import discord
from discord.ext import commands
import logging
import credentials
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

        self.homework_channel = self.get_channel(credentials.homework_channel)
        self.lessons_channel = 0
        self.pronote = pa.PronoteActions()


        return None

    async def on_ready(self):
        print('Succesfully logged in for Discord as {0.user}'.format(bot))

    async def on_message(self, message):
        print(message.content)
        if message.content.startswith('pro sync'):
            await self.updateChannel(self.pronote.getLessons(), self.pronote.getHomeworks(), message.channel)

        return None

    async def updateChannel(self, lessons, homeworks, channel):
        print('abcdef')
        for hw in homeworks:
            #self.homework_channel.send(hw)
            await channel.send(hw)
        #for le in lessons:
        #    await self.lessons_channel.send(le)
        return None

bot = DiscordBot()
bot.run(credentials.token)
