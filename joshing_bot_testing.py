import aiomysql
import asyncio
import discord
import json
import mariadb
import pandas as pd
import random
import sys
from datetime import datetime#, timezone
from discord import Forbidden, HTTPException
#from discord.ext import commands
from config import TEST_TOKEN

# print version
print(f"[{datetime.now().strftime('%H:%M:%S')}] running version {sys.version}")

# Discord stuff
client = discord.Client()
#bot = commands.Bot(command_prefix="$")

# logging for analytics
user_log = open("joshing_bot/test_log.json", "r")
read_log = json.load(user_log)

# time_log = open("joshing_bot/time_log.json", "r")
# read_times = json.load(time_log)

# serverlist = read_log['servers']
# write_server = {"servers": serverlist}

userlist = read_log['users']
write_user = {"users": userlist}

# timelist = read_times['times']
# write_time = {"times": timelist}

def log_data(message):

    pass
    # # server data
    # foo = False
    # for servers in serverlist:
    #     if servers['guild'] == message.guild.id:
    #         foo = True
    #         server = servers


    # if foo == False:
    #     serverlist.append({'server': [{f'{message.guild}'},],
    #                         })



    # # user data
    # u = False
    # for users in userlist:
    #     if users['name'] == f'{message.author}':
    #         u = True
    #         user = users
    #     elif (users['uid'] == message.author.id) and (users['name'] != f'{message.author}'):
    #         print("[{}] User {} has changed their tag to {}, updating entry in file.".format(message.created_at.strftime('%H:%M:%S'), users['name'], message.author))
    #         users['name'] = f'{message.author}'
    #         u = True
    #         user = users

    # if u == True: # update msg count
    #     user['cnt'] += 1

    # else: # log users
    #     userlist.append({
    #         'name': f'{message.author}',
    #         'uid': message.author.id,
    #         'dnm': 40,
    #         'cnt': 1})
    #     print(f"[{message.created_at.strftime('%H:%M:%S')}] Logged new user! {message.author}")

    # write to files
    # with open('joshing_bot/test_log.json', 'w') as userfile:
    #     json.dump(write_user, userfile, indent=2)
    # pd.DataFrame(userlist, columns=['name', 'uid', 'dnm', 'cnt']).to_csv('joshing_bot/test_log.csv')

# pseudo-typing for character establishing
async def type_wait(message):
    await message.channel.trigger_typing()
    if len(message.content) >= 38:
        await asyncio.sleep(2)
    elif len(message.content) < 38:
        await asyncio.sleep(1)

# pedophile slaughterhouse flood
async def ps_spam():
    counter = 1
    while True:
        channel = client.get_channel(939312650318405672) # slaughterhouse id 842573792747716618
        if counter == 1:
            await channel.send(file=discord.File(r'/home/kitten/Pictures/spam.png'))
            await channel.send('1 dead pedophile')
        else:
            await channel.send(file=discord.File(r'/home/kitten/Pictures/spam.png'))
            await channel.send(f'{counter} dead pedophiles')
        counter += 1
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Another pedophile fucking died lol")
        await asyncio.sleep(599)

# josh the message
def josh(message):
    ret = ""
    i = False # capitalize second letter
    for char in message:
        if i:
            ret += char.upper()
        else:
            ret += char.lower()
        if char != ' ':
            i = not i
    return ret

# automatically checks for targeted response conditions
async def speak(message):
    if message.guild.id == 845142029766754315: # test server id 845142029766754315 bad bois server id 579399140769923102
        for users in userlist:
            if message.author.id == users['uid']:
                dnm = users['dnm']
    else:
        if message.author.id == 204366690446737419: # blacklist self outside bad bois
            dnm = 200
        else:
            dnm = 40

    x = random.randint(1, dnm)

    if (len(message.content) <= 75) and (x == 1):
        if (message.content.startswith('-')) or (message.content.startswith('!')):
            try:
                print(f"[{message.created_at.strftime('%H:%M:%S')}] Invalid message received (bot command)")
            except TypeError: # cant start message with '!'
                print(f"[{message.created_at.strftime('%H:%M:%S')}] TypeError Encountered with invalid message (bot command)")
        elif (message.content.startswith('http')):
            print(f"[{message.created_at.strftime('%H:%M:%S')}] Invalid message received (external link)")
        elif  (message.content.startswith('<@!')):
            print(f"[{message.created_at.strftime('%H:%M:%S')}] Invalid message received (tagged user)")
        elif (message.content.startswith('<A:')):
            print(f"[{message.created_at.strftime('%H:%M:%S')}] Invalid message received (Nitro emoji)")
        else:
            try:
                result = josh(message.content)
                try:
                    await type_wait(message)
                    await message.channel.send(result)
                    print("[{}] Reply sent to {} in {}! Response Chance: {}%".format(message.created_at.strftime('%H:%M:%S'), message.author, message.guild.name, round((100 / dnm), 2)))
                except HTTPException:
                    print(f"[{message.created_at.strftime('%H:%M:%S')}] Invalid message received (empty msg)") # Josh will sometimes try to josh an image
            except Forbidden:
                    print(f"[{message.created_at.strftime('%H:%M:%S')}] Forbidden 403 Encountered")

# active Discord interaction

# @bot.command()
# async def ping(ctx):
#     print('pong')
#     await ctx.channel.send('pong')

# @bot.command()
# async def test(ctx, arg1, arg2):
#     await ctx.send('You passed {} and {}'.format(arg1, arg2))

# @bot.command
# async def play(ctx, url):
#     voiceChannel = ctx.author.voice.channel
#     voice = discord.utils.get(ctx.guild.voice_channels, name='General')
#     if not voice.is_connected():
#         await voiceChannel.connect()
#         channel = client.get_channel(845142029766754318)
#         channel.send(f"!play {url}")
#         await asyncio.sleep(1.5)
#         await voiceChannel.disconnect()

@client.event
async def on_ready():
    print(f"[{datetime.now().strftime('%H:%M:%S')}] fired up on {client.user}!")
    await ps_spam()

async def on_message(message):

    if message.author != client.user:

        if message.guild.id == 845142029766754315: # test server id 845142029766754315 bad bois server id 579399140769923102

            log_data(message)

        print(f"[{message.created_at.strftime('%H:%M:%S')}] Message received from {message.author} in {message.guild.name}")

        if (message.content == 'quack') or (message.content == 'i am a duck') or (message.content == ':v'):
            try:
                print(f"[{message.created_at.strftime('%H:%M:%S')}] quack :v")
                await message.channel.trigger_typing()
                await asyncio.sleep(2)
                await message.channel.send("https://cdn.discordapp.com/emojis/697995591921172532.gif?")
            except Forbidden:
                print(f"[{message.created_at.strftime('%H:%M:%S')}] Forbidden 403 Encountered")

        elif (('josh' in message.content) and ('master' in message.content) and (('who') or ('whos') in message.content)):
            try:
                await message.channel.trigger_typing()
                await asyncio.sleep(1)
                await message.channel.send("kitty#8073 is my master")
            except Forbidden:
                print(f"[{message.created_at.strftime('%H:%M:%S')}] Forbidden 403 Encountered")
        else:
            await speak(message)
        
        if (("josh" in message.content) and ("9" in message.content) and ("10" in message.content)):
            await message.channel.trigger_typing()
            await asyncio.sleep(1)
            await message.channel.send("21")

    # await bot.process_commands(message)

client.run(TEST_TOKEN)