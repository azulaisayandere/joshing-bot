# shoutouts to stackoverflow and charles from which i stole the basis for most of this code
# REMOVE DIRECTORIES BEFORE DEPLOYING
# CHANGE FLOOD CHANNEL ID AND COUNTER
# objectives: + done * in progress x not started
# spam every nth message [+]
# target specific users [+]
# log user data [+]
# move logs from json to mariadb [*]
# pedophile slaughterhouse contribution [+]
# log chat frequency data[+], most active users[+], message times [*] 
# play music with 'alexa play __' command [*]
# train language model [x]

import asyncio
import discord
import json
import pandas as pd
import sys
from datetime import datetime
from discord import Forbidden
from config import TEST_TOKEN
from chat import speak
from logs import log_data

# print version
print(f"[{datetime.now().strftime('%H:%M:%S')}] running version {sys.version}")

# Discord stuff
client = discord.Client()

# logging for analytics
user_log = open("user_log.json", "r")
read_users = json.load(user_log)

userlist = read_users['users']
write_user = {"users": userlist}

def log_data(message):

    # user data
    x = False
    for users in userlist:
        if users['name'] == f'{message.author}':
            x = True
            user = users
        elif (users['uid'] == message.author.id) and (users['name'] != f'{message.author}'):
            print("[{}] User {} has changed their tag to {}, updating entry in file.".format(message.created_at.strftime('%H:%M:%S'), users['name'], message.author))
            users['name'] = f'{message.author}'
            x = True
            user = users

    if x == True: # update msg count
        user['cnt'] += 1

    else: # log users
        userlist.append({
            'name': f'{message.author}',
            'uid': message.author.id,
            'dnm': 40,
            'cnt': 1})
        print(f"[{message.created_at.strftime('%H:%M:%S')}] Logged new user! {message.author}")

    # write to files
    with open('user_log.json', 'w') as userfile:
        json.dump(write_user, userfile, indent=2)
    pd.DataFrame(userlist, columns=['name', 'uid', 'dnm', 'cnt']).to_csv('user_log.csv')

# pedophile slaughterhouse flood
async def ps_spam():
    counter = 1
    while True:
        channel = client.get_channel(939312650318405672) # slaughterhouse id 842573792747716618
        if counter == 1:
            await channel.send(file=discord.File(r'spam.png'))
            await channel.send('1 dead pedophile')
        else:
            await channel.send(file=discord.File(r'spam.png'))
            await channel.send(f'{counter} dead pedophiles')
        counter += 1
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Another pedophile fucking died lol")
        await asyncio.sleep(599)

# active Discord interaction

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

client.run(TEST_TOKEN)
