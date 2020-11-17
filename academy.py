import datetime
import utils
import discord
from discord.ext import commands
from constants import BUILDS_JSON_PATH, BUILD_NOT_EXISTS, CHARACTERS_JSON_PATH, JOIN_MESSAGE, PREDATORS, STARS, TIME, NEW_PLAYER, TOKEN, VIPERS

CHARACTERS = utils.load_dict(CHARACTERS_JSON_PATH)
BUILDS = utils.load_dict(BUILDS_JSON_PATH)


bot = commands.Bot(command_prefix='-')


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)

@bot.event
async def on_member_join(member):
    welcome = bot.get_channel(717863274909139055)
    await welcome.send(JOIN_MESSAGE.format(member))

@bot.command()
async def time(ctx):
    await ctx.send(TIME.format(datetime.datetime.now(datetime.timezone.utc).strftime("%H:%M:%S")))

@bot.command()
async def build(ctx, arg):
    build = BUILDS[arg]
    if build:
        await ctx.send(build)
    else:
        await ctx.send(BUILD_NOT_EXISTS)

@bot.command()
async def passives(ctx, arg):
    for c in CHARACTERS:
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
    for c in CHARACTERS:
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
    for c in CHARACTERS:
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
    for c in CHARACTERS:
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
    await ctx.send("**Who is your daddy ?**", file=discord.File("gif/batmanson.gif"))

@bot.command()
async def kirito(ctx):
    await ctx.send("**All hail to The King**")

@bot.command()
async def imqrx(ctx):
    await ctx.send("**Meet The Big Boss**", file=discord.File("gif/imqrx.gif"))

@bot.command()
async def blackwolf(ctx):
    await ctx.send("**King's knight**")

@bot.command()
async def thera(ctx):
    await ctx.send(file=discord.File("gif/cap.gif"))

@bot.command()
async def myee(ctx):
    await ctx.send("**Bring ur hot Bootylicious ESF  mammy  out.**", file=discord.File("emoji/myee.jpg"))

@bot.command()
async def dx2(ctx):
    await ctx.send("**The Courageous knight for the people**")

@bot.command()
async def makslays(ctx):
    await ctx.send(file=discord.File("emoji/mac.jpeg"))

@bot.command()
async def ramza(ctx):
    await ctx.send("**It was me, Barry!**", file=discord.File("gif/ramza.gif"))

@bot.command()
async def nyryon(ctx):
    await ctx.send("**South Italy Nyry-Don**", file=discord.File("emoji/4407.png"))

@bot.command()
async def speedy(ctx):
    await ctx.send("**do ur work properly ss boy ? or no salary for u**", file=discord.File("emoji/c3po.png"))

@bot.command()
async def tony(ctx):
    tony_member = await ctx.guild.fetch_member(552431423165038628)
    await ctx.send("**The Boot Legend** - {0.mention}".format(
        tony_member
    ))

@bot.command()
async def haitodo(ctx):
    haitodo_member = await ctx.guild.fetch_member(355445149393879040)
    await ctx.send("Relax Alex {0.mention}".format(
        haitodo_member
        ))

@bot.command()
async def newplayer(ctx):
    choose_league_channel = ctx.guild.get_channel(717026493557112963)
    fast_improve_channel = ctx.guild.get_channel(753734930583781437)
    await ctx.send(NEW_PLAYER.format(
    choose_league_channel,
    fast_improve_channel))

bot.run(TOKEN)
