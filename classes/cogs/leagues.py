from classes.cogs.roles import lookup_predefined_roles
from constants import *
from discord.ext import commands
from datetime import timedelta
import datetime


class LeaguesCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['rebels'])
    async def rebel(self, ctx):
        await ctx.send(REBEL)

    @commands.command()
    async def predators(self, ctx):
        await ctx.send(PREDATORS)

    @commands.command(aliases=["eternals"])
    async def eternal(self, ctx):
        await ctx.send(ETERNAL)

    @commands.command()
    async def tower(self, ctx):
        await ctx.send(TOWER)

    @commands.command()
    async def knights(self, ctx):
        await ctx.send(KNIGHTS)

    @commands.command()
    async def reverse(self, ctx):
        await ctx.send(REVERSE)

    @commands.command()
    async def vipers(self, ctx):
        await ctx.send(VIPERS)

    @commands.command()
    async def stars(self, ctx):
        await ctx.send(STARS)

    @commands.command()
    async def leagues(self, ctx):
        await ctx.send(LEAGUES)

    @commands.command(aliases=['arthur', 'arthur-fleck'])
    async def fleck(self, ctx):
        await ctx.send(FLECK)

    @commands.command(aliases=['mvm2'])
    async def mvm(self, ctx):
        await ctx.send(MVM2)

    @commands.command(aliases=['harley-squints', 'squints'])
    async def harley(self, ctx):
        await ctx.send(SQUINTS)

    @commands.command(aliases=['immortal'])
    async def immortals(self, ctx):
        await ctx.send(IMMORTAL)

    @commands.command()
    async def newplayer(self, ctx):
        if ctx.author.guild.id != 717021950387421225: #Academy Main Server
            return

        choose_league_channel = ctx.guild.get_channel(717026493557112963)
        fast_improve_channel = ctx.guild.get_channel(753734930583781437)
        await ctx.send(NEW_PLAYER.format(
        choose_league_channel,
        fast_improve_channel))


class RaidCog(commands.Cog):
    def __init__(self, bot, db_service):
        self.bot = bot
        self.db_service = db_service
        self.raid_plan_channels = {
            'stars': 725346088642412695,
            'predators': 739169851465269278,
            'vipers': 756608666471235615,
            'eternals': 810124653318242364,
            'rebels': 810126020409163776,
            'TestRole': 790983451108179969
            }

    def to_lower(self, content):
        return content.lower()

    @commands.command(aliases=['raid-open', 'raid', 'raid-start'])
    async def raidopen(self, ctx, league):
        #if ctx.author.guild.id != 717021950387421225: #Academy Main Server
            #return

        channel_id = self.raid_plan_channels[league]

        if not channel_id:
            await ctx.send('league with such name was not found.')
            return

        leagues = lookup_predefined_roles(ctx)

        raids = self.db_service.get_collection("raids")

        if not raids:
            await ctx.send("unable to start raid, please contact the administrator.")

        raid_plan_channel = await self.bot.fetch_channel(channel_id)

        for role in leagues:
            if role.name.lower() == league.lower():
                raid_role = role

        await raid_plan_channel.send('{0.mention}, raid started.'.format(raid_role))

        cur_time = datetime.datetime.now(datetime.timezone.utc)
        end_time = cur_time + timedelta(days=3)
        cur_str = cur_time.strftime(DATE_TIME_FORMAT)
        end_str = end_time.strftime(DATE_TIME_FORMAT)

        raids.update_one(
            filter={'league': league},
                update={
                    "$set": {
                        'launcherId': ctx.author.id,
                        'launcherName': ctx.author.display_name,
                        'league': league,
                        'start_date': cur_str,
                        'end_date': end_str,
                        'expired': False
                    }
                },
                upsert=True)

    @commands.command(aliases=['raid-status'])
    async def raidstatus(self, ctx, *league):
        if not league:
            raids = self.db_service.get_collection("raids").find({})
        else:
            raids = self.db_service.get_collection('raids').find({'league': league[0]})

        if not raids:
            await ctx.send('No raid records.')
            return

        out_list = []
        for raid in raids:
            if raid['expired'] == True:
                out_list.append('last {} raid expired at {}'.format(raid['league'], raid['end_date']))
            else:
                day = self.determine_day(raid)
                if day:
                    out_list.append('{} raid is in progress. {}'.format(raid['league'], day))
                else:
                    raids.update_one(
                        filter=raid,
                        update={'$set': {'expired': True}})

        await ctx.send('\n'.join(out_list))


    def determine_day(self, raid):
        day = ''
        end_date = datetime.datetime.strptime(raid['end_date'], DATE_TIME_FORMAT)
        now_time = datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None)

        left = ((end_date - now_time).days * 24) + (end_date - now_time).seconds // 3600
        if 0 < left <= 24:
            day = 'Day 3'
        elif 24 < left <= 48:
            day = 'Day 2'
        elif 48 < left <= 72:
            day = 'Day 1'

        return day