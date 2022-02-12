import aiomysql #unused atm
import asyncio
import discord
import json
import mariadb # unused atm
import os # unused atm
import pandas as pd
import nacl # unused atm
import random
import sys
from datetime import datetime#, timezone
from discord import Forbidden, HTTPException
from discord.ext import commands
from config import TEST_TOKEN

# print version
print(f"[{datetime.now().strftime('%H:%M:%S')}] running version {sys.version}")

# Discord stuff
client = commands.Bot(command_prefix="josh ")

# logging for analytics
user_log = open("joshing_bot/test_log.json", "r")
read_log = json.load(user_log)

userlist = read_log['users']
write_user = {"users": userlist}

def log_data(message):

    # user data
    u = False
    for users in userlist:
        if users['name'] == f'{message.author}':
            u = True
            user = users
        elif (users['uid'] == message.author.id) and (users['name'] != f'{message.author}'):
            print("[{}] User {} has changed their tag to {}, updating entry in file.".format(message.created_at.strftime('%H:%M:%S'), users['name'], message.author))
            users['name'] = f'{message.author}'
            u = True
            user = users

    if u == True: # update msg count
        user['cnt'] += 1

    else: # log users
        userlist.append({
            'name': f'{message.author}',
            'uid': message.author.id,
            'dnm': 40,
            'cnt': 1})
        print(f"[{message.created_at.strftime('%H:%M:%S')}] Logged new user! {message.author}")

    # write to files
    with open('joshing_bot/test_log.json', 'w') as userfile:
        json.dump(write_user, userfile, indent=2)
    pd.DataFrame(userlist, columns=['name', 'uid', 'dnm', 'cnt']).to_csv('joshing_bot/test_log.csv')

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
    if message.guild.id == 937380112771477564: # test server id 937380112771477564 bad bois server id 579399140769923102
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

@client.command()
async def ping(ctx, url):
    await ctx.author.voice.channel.connect()
    tchannel = client.get_channel(937380112771477567)
    await tchannel.send(f"!play {url}")
    await asyncio.sleep(1.5)
    if discord.voice_client.VoiceClient.is_connected():
        print(True)
        #await discord.voice_client.VoiceClient.disconnect()

# @client.command()
# async def test(ctx, arg1, arg2):
#     await ctx.send('You passed {} and {}'.format(arg1, arg2))

@client.event
async def on_ready():
    print(f"[{datetime.now().strftime('%H:%M:%S')}] fired up on {client.user}!")
    await ps_spam()

@client.event
async def on_message(message):

    if message.author != client.user:

        if message.guild.id == 937380112771477564: # test server id 937380112771477564 bad bois server id 579399140769923102

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

    await client.process_commands(message)

client.run(TEST_TOKEN)