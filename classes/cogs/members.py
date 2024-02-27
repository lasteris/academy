import discord
from constants import *
from discord.ext import commands

class MemberCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        if member.guild.id != 717021950387421225: #Academy Main Server
            return

        welcome = await self.bot.fetch_channel(717863274909139055)
        await welcome.send(JOIN_MESSAGE.format(member))

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        if member.guild.id != 717021950387421225: #Academy Main Server
            return

        channel = await self.bot.fetch_channel(807957905235247124)
        await channel.send(LEFT_SERVER.format(member))


    @commands.Cog.listener()
    async def on_member_update(self, old_user_info, new_user_info):
        if new_user_info.guild.id != 717021950387421225: #Academy Main Server
            return

        league_roles = [717029499463794718, 717029493088452688, 717029489124573224, 775433895020855326, 792405449160261672, 799230903377199135]
        old_roles = [role.id for role in old_user_info.roles]
        new_roles = [role.id for role in new_user_info.roles]

        for role in league_roles:
            if role not in old_roles and role in new_roles:
                try:
                    await new_user_info.send(LEAGUE_RAID_WARNING.format(new_user_info, new_user_info.guild.get_role(role)))
                    break
                except Exception:
                    pass

class NamedCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def haibito(self, ctx):
        await ctx.send("**The real haitodo**", file=discord.File("gif/haibito.gif"))

    @commands.command()
    async def adotam(self, ctx):
        await ctx.send(file=discord.File("gif/adotam.gif"))

    @commands.command()
    async def batman(self, ctx):
        await ctx.send("**Who am i ?**", file=discord.File("gif/batmanson2.gif"))

    @commands.command()
    async def lasteris(self, ctx):
        await ctx.send(file=discord.File("gif/lasteris.gif"))

    @commands.command()
    async def kirito(self, ctx):
        await ctx.send("**All hail to The King**", file=discord.File("gif/kirito.gif"))

    @commands.command()
    async def imqrx(self, ctx):
        await ctx.send("**Don’t Vex Me, Mortal**", file=discord.File("gif/imqrx.gif"))

    @commands.command()
    async def blackwolf(self, ctx):
        await ctx.send("**King's knight**", file=discord.File("gif/blackwolf.gif"))

    @commands.command()
    async def thera(self, ctx):
        await ctx.send(file=discord.File("gif/cap.gif"))

    @commands.command()
    async def myee(self, ctx):
        await ctx.send("**Bring ur hot Bootylicious ESF  mammy  out.**", file=discord.File("emoji/myee.jpg"))

    @commands.command()
    async def dx2(self, ctx):
        await ctx.send("**The Courageous knight for the people**")

    @commands.command(aliases=['makoslays', 'slay'])
    async def mako(self, ctx):
        await ctx.send("**\"for the world is  the batten and death the  prize, and life the game, shed no tears for the absent, nor the fallen, for death is an inexorable ballad that plays upon your end, I MAKO HAVE COME TO APPORTION YOUR SONG, WITH MY HEART THE INSTRUMENT WHICH I EMPLOY TO SLAY**\"", file=discord.File("gif/mako.gif"))

    @commands.command()
    async def chrisdroid(self, ctx):
        await ctx.send(file=discord.File("gif/chris.gif"))

    @commands.command()
    async def ramza(self, ctx):
        await ctx.send("**It was me, Barry!**", file=discord.File("gif/ramza.gif"))

    @commands.command()
    async def akpro(self, ctx):
        await ctx.send("**I am faster than you**", file=discord.File("gif/akpro.gif"))

    @commands.command()
    async def misty(self, ctx):
        await ctx.send("I am the night!", file=discord.File("gif/misty.gif"))

    @commands.command()
    async def nyryon(self, ctx):
        await ctx.send("**South Italy Nyry-Don**", file=discord.File("emoji/4407.png"))

    @commands.command()
    async def spyeedy(self, ctx):
        await ctx.send("**do ur work properly ss boy ? or no salary for u**", file=discord.File("gif/spyeedy.gif"))

    @commands.command()
    async def tony(self, ctx):
        await ctx.send("**The Boot Legend**")

    @commands.command()
    async def haitodo(self, ctx):
        await ctx.send("Relax Alex", file=discord.File("gif/haitodo.gif"))

    @commands.command()
    async def sensei(self, ctx):
        await ctx.send("**I have arrived.**", file=discord.File("gif/sensei.gif"))

    @commands.command()
    async def lunar(self, ctx):
        await ctx.send(file=discord.File("gif/lunar.gif"))

    @commands.command()
    async def blue(self, ctx):
        await ctx.send(file=discord.File("gif/blue.gif"))