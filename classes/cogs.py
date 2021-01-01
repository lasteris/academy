from classes.database import DatabaseService
import discord
from constants import *
from discord.ext import commands, tasks
import asyncio
from datetime import timedelta
import datetime
import json


class LeaguesCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def predators(self, ctx):
        await ctx.send(PREDATORS)

    @commands.command()
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


class NamedCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

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

    @commands.command()
    async def makslays(self, ctx):
        await ctx.send("**The power of the everyone tag**", file=discord.File("gif/macslays.gif"))

    @commands.command()
    async def chrisdroid(self, ctx):
        await ctx.send(file=discord.File("gif/chris.gif"))

    @commands.command()
    async def ramza(self, ctx):
        await ctx.send("**It was me, Barry!**", file=discord.File("gif/ramza.gif"))

    @commands.command()
    async def akpro(self, ctx):
        await ctx.send("**I am ready**", file=discord.File("gif/akpro.gif"))

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


class CharactersCog(commands.Cog):
    def __init__(self, bot, db_service):
        self.bot = bot
        self.db_service = db_service

    @commands.command()
    async def build(self, ctx, arg):
        search = self.db_service.get_collection('builds').find_one({"name": arg})
        if search:
            if search["value"]:
                await ctx.send(search["value"])
            else:
                await ctx.send(BUILD_NOT_EXISTS)
        else:
            await ctx.send(CHARACTER_NOT_RECOGNIZED)

    @commands.command()
    async def passives(self, ctx, arg):
        character = self.db_service.get_collection('characters').find_one(
            {'acronym': arg}, {'passives': 3})

        passives_text = ''
        for p in character["passives"]:
            passives_text += "**" + p['name'] + "**\n" + p["description"] + "\n"
            for buff in p['buffs']:
                passives_text += "*" + buff + "*\n"
            passives_text += '\n'
        await ctx.send(passives_text)

    @commands.command()
    async def specials(self, ctx, arg):
        character = self.db_service.get_collection('characters').find_one(
            {'acronym': arg}, {'specials': 3})

        specials_text = ''
        for sp in character["specials"]:
            specials_text += "**" + sp['name'] + "**\n" + sp["description"] + "\n"
            for buff in sp['buffs']:
                specials_text += "*" + buff + "*\n"
            specials_text += '\n'
        await ctx.send(specials_text)

    @commands.command()
    async def supermove(self, ctx, arg):
        character = self.db_service.get_collection('characters').find_one(
            {'acronym': arg}, {'supermove': 1})

        sm = character['supermove']
        supermove_text = "**" + sm['name'] + "**\n" + sm["description"] + "\n"
        for buff in sm['buffs']:
            supermove_text += "*" + buff + "*\n"
        supermove_text += '\n'
        await ctx.send(supermove_text)

    @commands.command()
    async def name(self, ctx, arg):
        character = self.db_service.get_collection('characters').find_one({'acronym': arg}, {'name': 1})
        if character:
            await ctx.send(character["name"])
        else:
            await ctx.send("Abbreviation not recognized.")


class RolesCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def join(self, ctx, *args):
         #lookup roles by names to male it workable in Any Server with these Roles
        role_predator = discord.utils.get(ctx.guild.roles, name = "Predators")
        role_star = discord.utils.get(ctx.guild.roles, name = "Stars")
        role_viper = discord.utils.get(ctx.guild.roles, name = "Vipers")
        role_jumpers = discord.utils.get(ctx.guild.roles, name = "Jumpers")
        role_eternal = discord.utils.get(ctx.guild.roles, name = "Eternals")

        joined = False

        if len(args) == 1:
            league = args[0].lower()
            if league in ["predators", "vipers", "stars", "jumpers", "eternals"]:
                if league == "predators":
                    if role_predator in ctx.author.roles:
                        joined = True
                    else:
                        await ctx.author.add_roles(role_predator)
                elif league == "vipers":
                    if role_viper in ctx.author.roles:
                        joined = True
                    else:
                        await ctx.author.add_roles(role_viper)
                elif league == "stars":
                    if role_star in ctx.author.roles:
                        joined = True
                    else:
                        await ctx.author.add_roles(role_star)
                elif league == "jumpers":
                    if role_jumpers in ctx.author.roles:
                        joined = True
                    else:
                        await ctx.author.add_roles(role_jumpers)
                elif league == "eternals":
                    if role_eternal in ctx.author.roles:
                        joined = True
                    else:
                        await ctx.author.add_roles(role_eternal)
                if joined:
                    await ctx.send(ROLE_ALREADY_ADDED.format(ctx.author, args[0]))
                else:
                    await ctx.send(ROLE_ADDED_SUCCESSFULLY.format(args[0], ctx.author.mention))
            else:
                await ctx.send(ERROR_ON_ROLES_INTERACTION)
        else:
            await ctx.send(LITTLE_BOY)

    @commands.command()
    async def remove(self, ctx, *args):
        #lookup roles by names to male it workable in Any Server with these Roles
        role_predator = discord.utils.get(ctx.guild.roles, name = "Predators")
        role_star = discord.utils.get(ctx.guild.roles, name = "Stars")
        role_viper = discord.utils.get(ctx.guild.roles, name = "Vipers")
        role_jumpers = discord.utils.get(ctx.guild.roles, name = "Jumpers")
        role_eternal = discord.utils.get(ctx.guild.roles, name = "Eternals")

        removed = False

        if len(args) == 1:
            league = args[0].lower()
            if league in ["predators", "vipers", "stars", "jumpers", "eternals"]:
                if league == "predators":
                    if role_predator not in ctx.author.roles:
                        removed = True
                    else:
                        await ctx.author.remove_roles(role_predator)
                elif league == "vipers":
                    if role_viper not in ctx.author.roles:
                        removed = True
                    else:
                        await ctx.author.remove_roles(role_viper)
                elif league == "stars":
                    if role_star not in ctx.author.roles:
                        removed = True
                    else:
                        await ctx.author.remove_roles(role_star),
                elif league == "jumpers":
                    if role_jumpers not in ctx.author.roles:
                        removed = True
                    else:
                        await ctx.author.remove_roles(role_jumpers)
                elif league == "eternals":
                    if role_eternal not in ctx.author.roles:
                        removed = True
                    else:
                        await ctx.author.remove_roles(role_eternal)
                if removed:
                    await ctx.send(ROLE_ALREADY_REMOVED.format(ctx.author.name, args[0]))
                else:
                    await ctx.send(ROLE_REMOVED_SUCCESSFULLY.format(args[0], ctx.author.mention))
            else:
                await ctx.send(ERROR_ON_ROLES_INTERACTION)
        else:
            await ctx.send(LITTLE_BOY)

    @commands.command()
    async def dm(self, ctx, role: discord.Role, *, message):
        knights_role = ctx.guild.get_role(717032401456332801)

        if knights_role in ctx.author.roles:
            for m in role.members:
                await m.send(message)
        else:
            await ctx.send('sorry, {0.mention}, but you have no access to that feature.'.format(ctx.author))


class JumpCog(commands.Cog):
    def __init__(self, bot, db_service):
        self.bot = bot
        self.db_service = db_service
        self.countdown.start()

    @commands.command(name='jump-cd')
    async def cooldown(self, ctx, *args):
        cur_time = datetime.datetime.now(datetime.timezone.utc)
        end_time = cur_time + timedelta(days=21)

        cds = self.db_service.get_collection('cooldowns')

        jumper_id_str = str(ctx.author.id)
        cur_str = cur_time.strftime(DATE_TIME_FORMAT)
        end_str = end_time.strftime(DATE_TIME_FORMAT)

        if not args:
            cds.update_one(
                filter={'memberId': jumper_id_str},
                update={
                    "$set": {
                        'memberId': jumper_id_str,
                        'start': cur_str,
                        'end': end_str,
                        'name': ctx.author.display_name,
                        'warned': False
                    }
                },
                upsert=True)

            await ctx.send(CD_START_MESSAGE.format(ctx.author, cur_str, end_str))

        elif args[0] == 'status':
            jumper = cds.find_one({'memberId': jumper_id_str})
            if jumper:
                end_time = datetime.datetime.strptime(jumper['end'], DATE_TIME_FORMAT)
                now_time = datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None)
                days_left = (end_time - now_time).days
                if days_left > 0:
                    await ctx.send(CD_STATUS.format(ctx.author, days_left))
                else:
                    await ctx.send(CD_EXPIRED.format(ctx.author))

    @tasks.loop(hours=24)
    async def countdown(self):
        cds = self.db_service.get_collection('cooldowns')
        now_time = datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None)
        for jumper in cds.find({'warned': False}):
            member = await self.bot.fetch_user(int(jumper["memberId"]))
            end_time = datetime.datetime.strptime(jumper['end'], DATE_TIME_FORMAT)
            if end_time <= now_time:
                await member.send("Your jump cooldown has expired.\n**Have fun!**")
                cds.update_one(
                    filter=jumper,
                    update={"$set": {'warned': True}})


class UpgradesCog(commands.Cog):
    def __init__(self):
        # self.db_service = db_service
        self.upgrade_data = self.load_data()

    @commands.command(name='gear-cost')
    async def gear_cost(self, ctx, *args):
        if len(args) == 1:
            try:
                gear_number = int(args[0])

                if 70 >= gear_number >= 1:
                    cost = self.get_cost(gear_number)
                    await ctx.send(GEAR_COST.format(gear_number, cost, cost*5))
                else:
                    await ctx.send(GEAR_COST_OUT_RANGE)
            except ValueError:
                await ctx.send(GEAR_COST_WHOLE_NUM)
        elif len(args) == 2:
            try:
                lower_num = int(args[0])
                upper_num = int(args[1])

                if 70 >= lower_num >= 1 and 70 >= upper_num >= 1:
                    if lower_num < upper_num:
                        cost = self.get_cost(lower_num, upper_num)
                        await ctx.send(GEAR_COST_MULTI.format(lower_num, upper_num, cost, cost*5))
                    else:
                        await ctx.send("First number ({}) cannot be more than or equal to second number ({})".format(lower_num, upper_num))
                else:
                    await ctx.send(GEAR_COST_OUT_RANGE)
            except ValueError:
                await ctx.send(GEAR_COST_WHOLE_NUM)
        else:
            await ctx.send("Invalid number of arguments.")

    def load_data(self):
        text = ''
        with open('./resources/gear_costs.json', 'r') as f:
            text = json.load(f)
        return text

    def get_cost(self, *levels):
        total_cost = 0
        if len(levels) == 1:
            for level in range(1, levels[0]):
                total_cost += self.upgrade_data[str(level)]  # adding on the cost to total_cost
        else:
            for level in range(levels[0], levels[1]):
                if level == 0:
                    continue
                total_cost += self.upgrade_data[str(level)]
        return total_cost
