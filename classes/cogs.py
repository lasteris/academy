import discord
from constants import *
from discord.ext import commands, tasks
from datetime import timedelta
import datetime

class LeaguesCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['reaper'])
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

    def formatstr(self, str, type):
        return type.format(str)

    def formatarray(self, arr, type):
        return [type.format(val) for val in arr]

    @commands.command()
    async def build(self, ctx, arg):
        search = self.db_service.get_collection('builds').find_one({"name": arg.lower()})
        if search:
            if search["value"]:
                await ctx.send(search["value"])
            else:
                await ctx.send(BUILD_NOT_EXISTS)
        else:
            await ctx.send(CHARACTER_NOT_RECOGNIZED)

    @commands.command(aliases=["p"])
    async def passives(self, ctx, arg):
        character = self.db_service.get_collection('characters').find_one(
            {'acronym': arg.lower()}, {'passives': 3})

        if character:
            out_list = []
            for sp in character["passives"]:
                out_list.append(self.formatstr(sp['name'], BOLD))
                out_list.append(self.formatstr(sp['description'], ITALIC))
                out_list.extend(self.formatarray(sp['buffs'], ITALIC))

            out = '\n'
            await ctx.send(out.join(out_list))
        else:
            await ctx.send(ABBR_NOT_RECOGNIZED)

    @commands.command(aliases=["sp"])
    async def specials(self, ctx, arg):
        character = self.db_service.get_collection('characters').find_one(
            {'acronym': arg.lower()}, {'specials': 3})

        if character:
            out_list = []
            for sp in character["specials"]:
                out_list.append(self.formatstr(sp['name'], BOLD))
                out_list.append(self.formatstr(sp['description'], ITALIC))
                out_list.extend(self.formatarray(sp['buffs'], ITALIC))

            out = '\n'
            await ctx.send(out.join(out_list))
        else:
            await ctx.send(ABBR_NOT_RECOGNIZED)

    @commands.command(aliases=["sm", "ult", "ultimate"])
    async def supermove(self, ctx, arg):
        character = self.db_service.get_collection('characters').find_one(
            {'acronym': arg.lower()}, {'supermove': 1})

        if character:
            out_list = []
            out_list.append(self.formatstr(character['supermove']['name'], BOLD))
            out_list.append(self.formatstr(character['supermove']['description'], ITALIC))
            out_list.extend(self.formatarray(character['supermove']['buffs'], ITALIC))

            out = "\n"
            await ctx.send(out.join(out_list))
        else:
            await ctx.send(ABBR_NOT_RECOGNIZED)

    @commands.command()
    async def name(self, ctx, arg):
        characters = self.db_service.get_collection('characters')
        lines = []
        out = '\n'
        if "list" == arg:
            for character in characters.find():
                lines.append(LINE_FORMAT.format(character["acronym"], character["name"]))

            for lines_splitted in [lines[i:i + 50] for i in range(0, len(lines), 50)]:
                await ctx.send(self.formatstr(out.join(lines_splitted), CHUNKED))
        else:
            character = characters.find_one({'acronym': arg.lower()}, {'name': 1})
            if character:
                await ctx.send(character["name"])
            else:
                await ctx.send(ABBR_NOT_RECOGNIZED)


class RolesCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def lookup_role(self, ctx, name):
        return discord.utils.get(ctx.guild.roles, name = name)

    def lookup_predefined_roles(self, ctx):
       return [role for role in [self.lookup_role(ctx, name) for name in ["Predators", "Stars", "Vipers", "Jumpers", "Eternals", "Among"]] if role]

    @commands.command()
    async def join(self, ctx, *, arg):
        roles = self.lookup_predefined_roles(ctx)

        found = False

        league = arg.lower()

        for role in roles:
            if role.name.lower() in league:
                found = True
                if role not in ctx.author.roles:
                    await ctx.author.add_roles(role)
                    await ctx.send(ROLE_ADDED_SUCCESSFULLY.format(ctx.author, role))
                else:
                    await ctx.send(ROLE_ALREADY_ADDED.format(ctx.author, role))

        if not found:
            await ctx.send(ERROR_ON_ROLES_INTERACTION)

    @commands.command()
    async def remove(self, ctx, *, arg):
        roles = self.lookup_predefined_roles(ctx)

        found = False

        league = arg.lower()

        for role in roles:
            if role.name.lower() in league:
                found = True
                if role in ctx.author.roles:
                    await ctx.author.remove_roles(role)
                    await ctx.send(ROLE_REMOVED_SUCCESSFULLY.format(ctx.author, role))
                else:
                    await ctx.send(ROLE_ALREADY_REMOVED.format(ctx.author, role))

        if not found:
            await ctx.send(ERROR_ON_ROLES_INTERACTION)

class JumpCog(commands.Cog):
    def __init__(self, bot, db_service):
        self.bot = bot
        self.db_service = db_service
        self.countdown.start()

    @commands.command(name='jump-watch')
    async def start_watching(self, ctx, *args):
        if not args or len(args) > 1:
            await ctx.send(JUMP_WATCH_USAGE)
            return

        if(args[0] == "status"):
            if(self.countdown.is_running()):
                await ctx.send(NEXT_WATCH_CHECK_AT
                .format(self.countdown.next_iteration.strftime("%d %B %Y %H:%M:%S")))
            else:
                await ctx.send(WATCH_INACTIVE)
        elif(args[0] == "start"):
            self.countdown.start()
            await ctx.send(WATCH_STARTED)
        elif(args[0] == "stop"):
            self.countdown.cancel()
            await ctx.send(WATCH_CANCELLED)
        else:
            await ctx.send(PARAMETER_NOT_RECOGNIZED)


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
                try:
                    await member.send("Your jump cooldown has expired.\n**Have fun!**")
                except Exception:
                    pass
                cds.update_one(
                    filter=jumper,
                    update={"$set": {'warned': True}})


class UpgradesCog(commands.Cog):
    def __init__(self, db_service):
        self.db_service = db_service

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


    def get_cost(self, *levels):
        dict_gc = self.db_service.get_collection("dict_gc")
        total_cost = 0
        if len(levels) == 1:
            rows = dict_gc.find(
                {"level": {"$lt": levels[0]}})
            for row in rows:
                total_cost += row['cost']  # adding on the cost to total_cost
        else:
            rows = dict_gc.find(
                {"level": {"$gte": levels[0], "$lt": levels[1]}})
            for row in rows:
                total_cost += row['cost']
        return total_cost


class MessagingCog(commands.Cog):
    def __init__(self, bot, db_service):
        self.bot = bot
        self.db_service = db_service
        self.create_func_dict()


    @commands.command(name="rm")
    async def delete_messages(self, ctx, *, arg):
        async for message in ctx.channel.history(limit=100):
            if arg.lower() in message.content.lower():
               await message.delete()

    @commands.command(name="rmn")
    async def delete_messages_not(self, ctx, *, arg):
        async for message in ctx.channel.history(limit=100):
            if arg.lower() not in message.content.lower():
               await message.delete()

    @commands.command()
    async def dmr(self, ctx, role: discord.Role, *, message):
        random = discord.utils.get(ctx.guild.roles, name = "random")

        if random in ctx.author.roles:
            for m in role.members:
                try:
                    await m.send(message)
                except Exception:
                    pass
        else:
            await ctx.send(NO_ACCESS.format(ctx.author))

    @commands.command()
    async def dmp(self, ctx, member: discord.Member, *, message):
        random = discord.utils.get(ctx.guild.roles, name = "random")

        if random in ctx.author.roles:
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
