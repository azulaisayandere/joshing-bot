import aiomysql #unused atm
import asyncio
import discord
import json
import mariadb # unused atm
import os # unused atm
import nacl # unused atm
import random
import sys
from config import TEST_TOKEN
from datetime import datetime#, timezone
from discord import Forbidden
from discord.ext import commands
from chat import speak
from logs import log_data

# print version
print(f"[{datetime.now().strftime('%H:%M:%S')}] running version {sys.version}")

# Discord stuff
client = commands.Bot(command_prefix="josh ")

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

# active Discord interaction

@client.command()
async def ping(ctx, url):
    #await ctx.author.voice.channel.connect()
    voice = discord.voice_client.VoiceClient
    vchannel = client.get_channel(937380112771477568)
    await vchannel.connect()
    tchannel = client.get_channel(937380112771477567)
    await tchannel.send(f"!play {url}")
    await asyncio.sleep(1.5)
    if voice.is_connected:
        print(True)
        await voice.disconnect

@client.command()
async def whats(ctx, arg1, arg2):
    pass

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