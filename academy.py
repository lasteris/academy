import discord
import datetime
import utils

from constants import TOKEN, NEW_PLAYER

CHARACTERS_DATA = utils.load_data()

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    message_lowered = message.content.lower()

    if message_lowered.startswith('-'):
        command_line = message_lowered[1:]
        if command_line == "time":
            now_time = datetime.datetime.now(datetime.timezone.utc).strftime("%H:%M:%S")
            await message.channel.send('{0}\n***This is Academy time (GMT)***'.format(now_time))
        elif command_line == "predators":
            await message.channel.send('*2EH9EW*')
        elif command_line == "stars":
            await message.channel.send('*P87X95*')
        elif command_line == "vipers":
            await message.channel.send('*GKETR1*')
        elif command_line == "newplayer":
            inactive = client.get_channel(731571816631369868)
            fast_improve = client.get_channel(753734930583781437)
            choose_league = client.get_channel(717026493557112963)
            await message.channel.send(NEW_PLAYER.format(choose_league, fast_improve, inactive))
        elif command_line == 'batman-son':
            await message.channel.send("Who is daddy ?")
        elif command_line.startswith('passives'):
            splitted_command_line = command_line.split(maxsplit=1)
            character_name  = splitted_command_line[1]
            for c in CHARACTERS_DATA:
                if c["acronym"] == character_name:
                    passives_text = ''
                    for p in c["passives"]:
                        passives_text +=  "**" + p['name'] + "**\n" + p["description"] + "\n"
                        for buff in p['buffs']:
                            passives_text += "*" + buff + "*\n"
                        passives_text += '\n'
                    await message.channel.send(passives_text)
                    break
        elif command_line.startswith('specials'):
            splitted_command_line = command_line.split(maxsplit=1)
            character_name  = splitted_command_line[1]
            for c in CHARACTERS_DATA:
                if c["acronym"] == character_name:
                    specials_text = ''
                    for sp in c["specials"]:
                        specials_text +=  "**" + sp['name'] + "**\n" + sp["description"] + "\n"
                        for buff in sp['buffs']:
                            specials_text += "*" + buff + "*\n"
                        specials_text += '\n'
                    await message.channel.send(specials_text)
                    break
        elif command_line.startswith("supermove"):
            splitted_command_line = command_line.split(maxsplit=1)
            character_name  = splitted_command_line[1]
            for c in CHARACTERS_DATA:
                if c["acronym"] == character_name:
                    sm = c["supermove"]
                    supermove_text =  "**" + sm['name'] + "**\n" + sm["description"] + "\n"
                    for buff in sm['buffs']:
                        supermove_text += "*" + buff + "*\n"
                    supermove_text += '\n'
                    await message.channel.send(supermove_text)
                    break

client.run(TOKEN)