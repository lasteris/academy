import discord
import asyncio

from constants import *
from discord.ext import commands
from classes.services.sendable import Sender
from classes.cogs.roles import lookup_predefined_roles

class MessagingCog(commands.Cog):
    def __init__(self, bot, db_service):
        self.bot = bot
        self.db_service = db_service
        self.create_func_dict()

    @commands.command()
    async def group(self, ctx, channel: discord.TextChannel, *, message):
        roles = ''.join([role.mention for role in lookup_predefined_roles(ctx)])
        await channel.send("{}. {}".format(roles, message))

    @commands.command(name="rm", aliases=["clear-in"])
    async def delete_messages(self, ctx, *, arg):
        mod = discord.utils.get(ctx.guild.roles, name = "Moderator")

        parts = arg.split(' ', 1)

        try:
            limit = int(parts[0])
            content = parts[1].lower()
            if mod not in ctx.author.roles:
                await ctx.send(NOT_ENOUGH_POWER)
                return

            count = 0
            async for message in ctx.channel.history(limit=100):
                if (content in message.content.lower()):
                    if count == limit:
                        break

                    await message.delete()
                    count+=1

        except ValueError:
            await ctx.send(NOT_VALID_NUMBER)


    @commands.command(name="rmn", aliases=["clear-not-in"])
    async def delete_messages_not(self, ctx, *, arg):
        mod = discord.utils.get(ctx.guild.roles, name = "Moderator")

        if mod not in ctx.author.roles:
            await ctx.send(NOT_ENOUGH_POWER)
            return

        parts = arg.split(' ', 1)

        try:
            limit = int(parts[0])
            content = parts[1].lower()
            count = 0
            async for message in ctx.channel.history(limit=100):
                if (content not in message.content.lower()):
                    if count == limit:
                        break

                    await message.delete()
                    count += 1

        except ValueError:
            await ctx.send(NOT_VALID_NUMBER)


    @commands.command()
    async def dmr(self, ctx, role: discord.Role, *, message):
        mod = discord.utils.get(ctx.guild.roles, name = "Moderator")

        if mod in ctx.author.roles:
            for m in role.members:
                try:
                    await m.send(message)
                except Exception:
                    pass
        else:
            await ctx.send(NO_ACCESS.format(ctx.author))

    @commands.command()
    async def dmp(self, ctx, member: discord.Member, *, message):
        mod = discord.utils.get(ctx.guild.roles, name = "Moderator")

        if mod in ctx.author.roles:
            try:
                await member.send(message)
            except Exception:
                pass
        else:
            await ctx.send(NO_ACCESS.format(ctx.author))

    @commands.command()
    async def repeat(self, ctx, *, arg):
        if not arg:
            await ctx.send(WRONG_BEHAVIOUR)
            return

        if arg.startswith("stop"):
            await self.stop_some(ctx, arg)
        else:
            await self.start_some(ctx, arg)

    @commands.command()
    async def countdown(self, ctx, *, arg):
        """This Function is under hard development right now"""

        parts = arg.split(' ', 1)

        message = await ctx.send(parts[1])

        digits = ''.join([c for c in parts[0] if c.isdigit()])
        letters = ''.join([c for c in parts[0] if c.isalpha()])

        if letters in ["hours", "h", "hrs"]:
            await message.edit(content="{0}\nTime Left: {1} hours".format(parts[1], digits))
        elif letters in ["mins", "m"]:
            for i in range(int(digits), 1, -1):
                await message.edit(content="{0}\nTime Left: {1} minutes".format(parts[1], i))
                await asyncio.sleep(59.7)

            await message.edit(content="{0}\nTime Left: one minute")

            for i in range(59, 0, -1):
                await message.edit(content="{0}\nTime Left: {1} seconds".format(parts[1], i))
                await asyncio.sleep(0.7)

            await message.edit(content="{0}\nCountdown Expired".format(parts[1]))


    def create_func_dict(self):
        self.func_dict = {}
        for warn in self.db_service.get_collection("repeatable_warnings").find({"enabled": True}):
            channel_id = warn["channel"]
            for guild in self.bot.guilds:
                for channel in guild.channels:
                    if channel.id == channel_id:
                        message = MSG_FORMAT.format(warn["name"], warn["message"])
                        self.func_dict[warn["name"]] = Sender(channel, message, warn["interval"])
                        self.func_dict[warn["name"]].start()

    async def start_some(self, ctx, arg):
        """This function is under hard development right now"""

        parts = arg.split(' ', 2)
        marker =  parts[0]
        if marker in self.func_dict:
            await ctx.send(MSG_ALREADY_IN.format(marker))
            return

        minutes = float(parts[1])
        message = MSG_FORMAT.format(marker, parts[2])
        self.func_dict[marker] = Sender(channel=ctx.channel, message=message, interval=minutes)
        self.func_dict[marker].start()

        self.db_service.get_collection("repeatable_warnings").insert_one(
            {
            "channel": ctx.channel.id,
            "interval": minutes,
            "message": parts[2],
            "name": marker,
            "enabled": True
            })

    async def stop_some(self, ctx, arg):
        """This function is under hard development right now"""

        if arg.endswith("all"):
            for value in self.func_dict.values():
                value.stop()

            #clear collection in database and reload from it in next 2 lines
            self.db_service.get_collection("repeatable_warnings").remove({})
            self.create_func_dict()

            await ctx.send(ALL_REPEAT_STOP)
            return

        #try stop particular msg
        parts = arg.split(' ', 1)
        marker = parts[1]
        if marker in self.func_dict:
            #remove warn-task from local dict and database
            self.func_dict[marker].stop()
            del self.func_dict[marker]
            self.db_service.get_collection("repeatable_warnings").remove({"name": marker})

            await ctx.send(MSG_REPEAT_STOP.format(marker))
        else:
            await ctx.send(MSG_NOT_FOUND)