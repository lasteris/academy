import asyncio
from classes.database import DatabaseService
import datetime
import logging
import discord

from classes.cogs import *
from discord.ext.commands import CommandNotFound
from discord.ext import commands
from classes.config import get_config
from constants import *

config = get_config('academy.yaml')

logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

intents = discord.Intents.default()
intents.members = True
intents.dm_messages = True

db_service = DatabaseService(config['url'], config['database'])

bot = commands.Bot(command_prefix='-', intents=intents)
bot.remove_command('help')

@bot.event
async def on_command_error(ctx, error):
    debug_channel = bot.get_channel(782610775096164373)
    if isinstance(error, CommandNotFound):
        debug_msg = "{0} sent message '{1}' to {2.mention}.".format(
            ctx.author.display_name,
            ctx.message.content,
            ctx.message.channel)
        logger.info(debug_msg)
        await debug_channel.send(debug_msg)
        return
    raise error

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    bot.add_cog(NamedCog(bot))
    bot.add_cog(LeaguesCog(bot))
    bot.add_cog(CharactersCog(bot, db_service))
    bot.add_cog(RolesCog(bot))
    bot.add_cog(JumpCog(bot, db_service))
    bot.add_cog(UpgradesCog(db_service))
    bot.add_cog(MessagingCog(bot, db_service))


@bot.event
async def on_member_join(member):
    if member.guild.id != 717021950387421225: #Academy Main Server
        return
    welcome = discord.utils.get(member.guild.channels, name='welcome')
    await welcome.send(JOIN_MESSAGE.format(member))


@bot.event
async def on_member_update(old_user_info, new_user_info):
    if new_user_info.guild.id != 717021950387421225: #Academy Main Server
        return

    league_roles = [717029499463794718, 717029493088452688, 717029489124573224, 775433895020855326, 792405449160261672]
    old_roles = [role.id for role in old_user_info.roles]
    new_roles = [role.id for role in new_user_info.roles]

    for role in league_roles:
        if role not in old_roles and role in new_roles:
            try:
                await new_user_info.send(LEAGUE_RAID_WARNING.format(new_user_info, new_user_info.guild.get_role(role)))
                break
            except Exception:
                pass



@bot.command()
async def time(ctx):
    await ctx.send(TIME.format(datetime.datetime.now(datetime.timezone.utc).strftime("%H:%M:%S")))


@bot.command()
async def newplayer(ctx):
    if ctx.author.guild.id != 717021950387421225: #Academy Main Server
        return

    choose_league_channel = ctx.guild.get_channel(717026493557112963)
    fast_improve_channel = ctx.guild.get_channel(753734930583781437)
    await ctx.send(NEW_PLAYER.format(
    choose_league_channel,
    fast_improve_channel))

@bot.command(aliases=["cd", "till-raid"])
async def countdown(ctx,role: discord.Role, *, arg):
    """-cd @Predators 10(mins|hrs|hours) """
    message = await ctx.send("{0.mention} hello".format(role))

    parts = arg.split(' ', 1)
    digits = ''.join([c for c in parts[0] if c.isdigit()])
    letters = ''.join([c for c in parts[0] if c.isalpha()])
    print("'{}'".format(letters))
    if letters in ["hours", "h", "hrs"]:
        print(letters)
        await asyncio.sleep(10)
        await message.edit(content="no no no {} hours".format(digits))
    elif letters in ["mins", "m"]:
        print(letters)
        await asyncio.sleep(10)
        await message.edit(content="no no no {} minutes".format(digits))


@bot.command()
async def help(ctx):
    await ctx.send(HELP)


bot.run(config['token'])
