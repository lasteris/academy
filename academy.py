
import discord
from discord.errors import Forbidden

from classes.services.database import DatabaseService
from classes.services.config import get_config
from classes.services.logging import config_logger
from classes.cogs.members import NamedCog, MemberCog
from classes.cogs.characters import CharactersCog
from classes.cogs.leagues import LeaguesCog, RaidCog
from classes.cogs.messaging import MessagingCog
from classes.cogs.roles import RolesCog
from classes.cogs.gears import UpgradesCog
from classes.cogs.jumps import JumpCog
from discord.ext.commands import CommandNotFound
from discord.ext import commands
from datetime import datetime
from datetime import timezone

from constants import *

config = get_config('academy.yaml')
logger = config_logger()
db_service = DatabaseService(config['url'], config['database'])

intents = discord.Intents.default()
intents.members = True
intents.dm_messages = True

bot = commands.Bot(command_prefix='-', intents=intents)
bot.remove_command('help')

def register_cogs():
    bot.add_cog(NamedCog(bot))
    bot.add_cog(LeaguesCog(bot))
    bot.add_cog(CharactersCog(bot, db_service))
    bot.add_cog(RolesCog(bot))
    bot.add_cog(JumpCog(bot, db_service))
    bot.add_cog(UpgradesCog(db_service))
    bot.add_cog(MessagingCog(bot, db_service))
    bot.add_cog(MemberCog(bot))
    bot.add_cog(RaidCog(bot, db_service))

@bot.event
async def on_command_error(ctx, error):
    debug_channel = bot.get_channel(782610775096164373)
    if isinstance(error, CommandNotFound):
        debug_msg = DEBUG_MESSAGE.format(
            ctx.author,
            ctx.message,
            ctx.message.channel)
        logger.info(debug_msg)
        await debug_channel.send(debug_msg)
        return
    raise error

@bot.event
async def on_ready():
    print(LOGGED.format(bot.user.id, bot.user.name))
    register_cogs()

@bot.command()
async def time(ctx):
    await ctx.send(TIME.format(datetime.now(timezone.utc).strftime(HOURS_FORMAT)))

@bot.command()
async def help(ctx):
    try:
        await ctx.author.send(HELP)
    except Forbidden as e:
        logger.debug(e)


bot.run(config['token'])