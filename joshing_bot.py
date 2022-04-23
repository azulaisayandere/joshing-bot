# shoutouts to stackoverflow and charles from which i stole the basis for a lot of this code
# objectives: + done * in progress x not started
# spam every nth message [+]
# target specific users [+]
# log user data [+]
# log frequency data[+], most active users[+], message times [*] 
# move logs from json to mariadb [x]
# pedophile slaughterhouse contribution [+] now removed, 37,846 kid diddlers dead :)
# train language model [x]

from asyncio import sleep
from bot_cmds.bot_commands import client
from chat.speak import speak
from config import TEST_TOKEN as TOKEN
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

@client.event
async def on_message(message):
    if message.author != client.user:
        await log_data(message)
        print(f"[{message.created_at.strftime('%H:%M:%S')}] Message received from {message.author} in {message.guild.name}")
        try:
            if message.content == ':v':
                print(f"[{message.created_at.strftime('%H:%M:%S')}] quack :v")
                await message.channel.trigger_typing()
                await sleep(1)
                await message.channel.send("https://cdn.discordapp.com/emojis/697995591921172532.gif?")
            else:
                await speak(message)
        except Forbidden:
            print(f"[{message.created_at.strftime('%H:%M:%S')}] Forbidden 403 Encountered")
    await client.process_commands(message)

client.run(TOKEN)