from constants import *
from discord.ext import commands

class CharactersCog(commands.Cog):
    def __init__(self, bot, db_service):
        self.bot = bot
        self.db_service = db_service

    def formatstr(self, str, type):
        return type.format(str)

    def formatarray(self, arr, type):
        return [type.format(val) for val in arr]

    @commands.command(aliases=["b"])
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