from asyncio import sleep
from datetime import datetime
from discord import Forbidden, File
from discord.ext import commands
from json import dump
from logs.logs import masslist, write
import pandas as pd

# Establish client user
client = commands.Bot(command_prefix="josh ")

# i hate rewriting this every time
async def typing(ctx, x):
    await ctx.channel.trigger_typing()
    await sleep(x)

# Discord commands
@client.command()
async def export(ctx):
    if ctx.author.id == 204366690446737419:
        for guilds in masslist:
            if guilds['guid'] == ctx.guild.id:
                userlist = guilds['users']
                pd.DataFrame(userlist, columns=['name', 'uid', 'dnm', 'cnt']).to_csv(f'{ctx.guild.id}_log.csv') # export by server via command
                await typing(ctx, 3)
                await ctx.send(file=File(f'{ctx.guild.id}_log.csv'))
                print(f"[{datetime.now().strftime('%H:%M:%S')}] Exported .csv for {ctx.guild}!")
    else:
        await typing(ctx, 1)
        await ctx.channel.send("you're not my master fuck off")

@client.command()
async def man(ctx):
        try:
            await typing(ctx, 2)
            await ctx.channel.send("usage: josh ___ \ncommands:\nstats- displays stats logged internally (WIP) e.g. josh stats <discord tag>\nrate- modifies response rate (WIP) e.g. josh rate <discord tag>\nman- sends this manual")
        except Forbidden:
            print(f"[{ctx.message.created_at.strftime('%H:%M:%S')}] Forbidden 403 Encountered")

@client.command()
async def stats(ctx, name):
    for guilds in masslist:
        if guilds['guid'] == ctx.guild.id:
            for user in guilds['users']:
                try:
                    if name == "me":
                        if ctx.author.id == user['uid']:
                            await typing(ctx, 2)
                            await ctx.channel.send(f"Josh Stats for {user['name']}, Message Count: {user['cnt']}, Rate: {round((100/user['dnm']), 1)}%")
                    else:
                        for user in masslist:
                            if (name == user['name']) or (name == f"<@{user['uid']}>"):
                                await typing(ctx, 2)
                                await ctx.channel.send(f"Josh Stats for {user['name']}, Message Count: {user['cnt']}, Rate: {round((100/user['dnm']), 1)}%")
                except Forbidden:
                    print(f"[{ctx.message.created_at.strftime('%H:%M:%S')}] Forbidden 403 Encountered")

@client.command()
async def rate(ctx, user, ndnm):
    if ctx.author.id == 204366690446737419:
        for guilds in masslist:
            if guilds['guid'] == ctx.guild.id:
                for victim in guilds['users']:
                    try:
                        if (user == victim['name']) or (user == f"<@{victim['uid']}>"):
                            victim['dnm'] = int(ndnm)
                            await typing(ctx, 2)
                            with open('user_log.json', 'w') as userfile:
                                dump(write, userfile, indent=2)
                            await ctx.channel.send(f"Joshing rate for {victim['name']}: {round((100/victim['dnm']), 1)}%")
                    except Forbidden:
                        print(f"[{ctx.message.created_at.strftime('%H:%M:%S')}] Forbidden 403 Encountered")
                    except commands.errors.MissingRequiredArgument:
                        print(f"[{ctx.message.created_at.strftime('%H:%M:%S')}] Missing argument")
    else:
        await typing(ctx, 1)
        await ctx.channel.send("you're not my master fuck off")