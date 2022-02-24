from asyncio import sleep
from discord.ext import commands
from logs.logs import userlist
import json
import pandas as pd

# Establish client user
client = commands.Bot(command_prefix="josh ")

# Discord commands
@client.command()
async def stats(ctx):
    for user in userlist:
        if ctx.author.id == user['uid']:
            await ctx.channel.trigger_typing()
            await sleep(2)
            await ctx.channel.send(f"Josh Stats for {user['name']}, Message Count: {user['cnt']}, Rate: 1/{user['dnm']}")

@client.command()
async def rate(ctx, user, ndnm):
    if ctx.author.id == 204366690446737419:
        for names in userlist:
            if user == names['name']:
                victim = names
                victim['dnm'] = ndnm
        # await ctx.channel.trigger_typing()
        # await sleep(2)
        await ctx.channel.send(f"Rate for {names['name']} now 1/{names['dnm']} {ndnm}")
    else:
        await ctx.channel.trigger_typing()
        await sleep(1)
        await ctx.channel.send("you're not my master fuck off")
