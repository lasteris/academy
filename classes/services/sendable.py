from constants import *
from discord.ext import tasks

class Sender(object):
    def __init__(self, channel, message, interval):
        self.message = message
        self.channel = channel
        self.send.change_interval(minutes=interval)

    @tasks.loop(count=10)
    async def send(self):
        await self.channel.send(self.message)

    def stop(self):
        self.send.cancel()

    def start(self):
        self.send.start()