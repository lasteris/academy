import datetime
import utils
import discord
from discord.ext import commands
from constants import PREDATORS, STARS, TIME, NEW_PLAYER, TOKEN, VIPERS

CHARACTERS_DATA = utils.load_data()

bot = commands.Bot(command_prefix='-')


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)

@bot.command()
async def time(ctx):
    await ctx.send(TIME.format(datetime.datetime.now(datetime.timezone.utc).strftime("%H:%M:%S")))

@bot.command()
async def passives(ctx, arg):
    for c in CHARACTERS_DATA:
        if c["acronym"] == arg:
            passives_text = ''
            for p in c["passives"]:
                passives_text +=  "**" + p['name'] + "**\n" + p["description"] + "\n"
                for buff in p['buffs']:
                    passives_text += "*" + buff + "*\n"
                passives_text += '\n'
            await ctx.send(passives_text)
            break

@bot.command()
async def specials(ctx, arg):
    for c in CHARACTERS_DATA:
        if c["acronym"] == arg:
            specials_text = ''
            for sp in c["specials"]:
                specials_text +=  "**" + sp['name'] + "**\n" + sp["description"] + "\n"
                for buff in sp['buffs']:
                    specials_text += "*" + buff + "*\n"
                specials_text += '\n'
            await ctx.send(specials_text)
            break

@bot.command()
async def supermove(ctx, arg):
    for c in CHARACTERS_DATA:
        if c["acronym"] == arg:
            sm = c["supermove"]
            supermove_text =  "**" + sm['name'] + "**\n" + sm["description"] + "\n"
            for buff in sm['buffs']:
                supermove_text += "*" + buff + "*\n"
            supermove_text += '\n'
            await ctx.send(supermove_text)
            break

@bot.command()
async def name(ctx, arg):
    for c in CHARACTERS_DATA:
        if c["acronym"] == arg:
            await ctx.send(c["name"])
            break

@bot.command()
async def predators(ctx):
    await ctx.send(PREDATORS)

@bot.command()
async def vipers(ctx):
    await ctx.send(VIPERS)

@bot.command()
async def stars(ctx):
    await ctx.send(STARS)

@bot.command()
async def batmanson(ctx):
    await ctx.send("Who is your daddy ?")

@bot.command()
async def kirito(ctx):
    await ctx.send("All hail to The King")

@bot.command()
async def blackwolf(ctx):
    await ctx.send("King's knight")

@bot.command()
async def haitodo(ctx):
    haitodo_member = await ctx.guild.fetch_member(355445149393879040)
    await ctx.send("Relax Alex {0.mention}".format(
        haitodo_member
        ))

@bot.command()
async def newplayer(ctx):
    choose_league_channel = await ctx.guild.get_channel(717026493557112963)
    fast_improve_channel = await ctx.guild.get_channel(753734930583781437)
    await ctx.send(NEW_PLAYER.format(
    choose_league_channel,
    fast_improve_channel))

bot.run(TOKEN)
