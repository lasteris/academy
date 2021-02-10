from constants import *
from discord.ext import commands


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

    @commands.command()
    async def newplayer(self, ctx):
        if ctx.author.guild.id != 717021950387421225: #Academy Main Server
            return

        choose_league_channel = ctx.guild.get_channel(717026493557112963)
        fast_improve_channel = ctx.guild.get_channel(753734930583781437)
        await ctx.send(NEW_PLAYER.format(
        choose_league_channel,
        fast_improve_channel))