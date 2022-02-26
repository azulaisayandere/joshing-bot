from asyncio import sleep
from discord import Forbidden
from discord.ext import commands
from json import dump
from logs.logs import userlist, write_user

# Establish client user
client = commands.Bot(command_prefix="josh ")

# i hate rewriting this every time
async def typing(ctx, x):
    await ctx.channel.trigger_typing()
    await sleep(x)

# Discord commands
@client.command()
async def stats(ctx, name):
    try:
        if name == "me":
            for user in userlist:
                if ctx.author.id == user['uid']:
                    await typing(ctx, 2)
                    await ctx.channel.send(f"Josh Stats for {user['name']}, Message Count: {user['cnt']}, Rate: 1/{user['dnm']}")
        else:
            for user in userlist:
                if name == user['name']:
                    await typing(ctx, 2)
                    await ctx.channel.send(f"Josh Stats for {user['name']}, Message Count: {user['cnt']}, Rate: 1/{user['dnm']}")
    except Forbidden:
        print(f"[{ctx.message.created_at.strftime('%H:%M:%S')}] Forbidden 403 Encountered")

@client.command()
async def rate(ctx, user, ndnm):
    try:
        if ctx.author.id == 204366690446737419:
            for victim in userlist:
                if user == victim['name']:
                    victim['dnm'] = int(ndnm)
                    await typing(ctx, 2)
                    with open('user_log.json', 'w') as userfile:
                        dump(write_user, userfile, indent=2)
                    await ctx.channel.send(f"Joshing rate for {victim['name']}: 1/{victim['dnm']}")
        else:
            await typing(ctx, 1)
            await ctx.channel.send("you're not my master fuck off")
    except Forbidden:
        print(f"[{ctx.message.created_at.strftime('%H:%M:%S')}] Forbidden 403 Encountered")

@client.command()
async def play(ctx, url):
    await ctx.author.voice.channel.connect()
    await client.get_channel(939312650318405672).send(f";;play {url}") # bot channel id 579400721640849450
    await sleep(3)
    await ctx.voice_client.disconnect()

@client.command()
async def boom(ctx):
    await client.get_channel(937380112771477568).connect() # main vc id 652287494716653598
    await client.get_channel(939312650318405672).send(f";;play https://www.youtube.com/watch?v=YkGisvljnaI") # bot channel id 579400721640849450
    await sleep(3)
    await ctx.voice_client.disconnect()

