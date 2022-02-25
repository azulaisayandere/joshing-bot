# shoutouts to stackoverflow and charles from which i stole the basis for a lot of this code
# CHANGE FLOOD CHANNEL ID AND COUNTER
# objectives: + done * in progress x not started
# spam every nth message [+]
# target specific users [+]
# log user data [+]
# move logs from json to mariadb [x]
# pedophile slaughterhouse contribution [+]
# log frequency data[+], most active users[+], message times [*] 
# play music with 'josh play __' command [*]
# train language model [x]

from bot_cmds.bot_commands import client
from chat.ps_spam import ps_spam
from chat.speak import speak
from chat.type_wait import type_wait
from config import TEST_TOKEN
from datetime import datetime
from discord import Forbidden
from logs.logs import log_data
from sys import version

# print version
print(f"[{datetime.now().strftime('%H:%M:%S')}] running Python {version}")

# other Discord interactions and funnies
@client.event
async def on_ready():
    print(f"[{datetime.now().strftime('%H:%M:%S')}] fired up on {client.user}!")
    await ps_spam()

@client.event
async def on_message(message):

    if message.author != client.user:

        if message.guild.id == 937380112771477564: # test server id 937380112771477564 bad bois server id 579399140769923102

            await log_data(message)

        print(f"[{message.created_at.strftime('%H:%M:%S')}] Message received from {message.author} in {message.guild.name}")

        if message.content == ':v':
            try:
                print(f"[{message.created_at.strftime('%H:%M:%S')}] quack :v")
                await type_wait(message)
                await message.channel.send("https://cdn.discordapp.com/emojis/697995591921172532.gif?")
            except Forbidden:
                print(f"[{message.created_at.strftime('%H:%M:%S')}] Forbidden 403 Encountered")

        elif (('josh' in message.content) and ('master' in message.content) and (('who') or ('whos') in message.content)):
            try:
                await type_wait(message)
                await message.channel.send("kitty#8073 is my master")
            except Forbidden:
                print(f"[{message.created_at.strftime('%H:%M:%S')}] Forbidden 403 Encountered")
        else:
            await speak(message)

        if (("josh" in message.content) and ("9" in message.content) and ("+" in message.content) and ("10" in message.content)):
            await type_wait(message)
            await message.channel.send("21")
    await client.process_commands(message)

client.run(TEST_TOKEN)