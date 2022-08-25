from asyncio import sleep
from datetime import datetime
from discord import Forbidden, File, Intents
from discord.ext import commands
from json import dump
from logs.logs import masslist, write
from pandas import DataFrame

# Establish client user
intents = Intents.all()
client = commands.Bot(command_prefix="josh ", intents=intents)

# i hate rewriting this every time
async def typing(ctx, x):
    await ctx.channel.typing()
    await sleep(x)

# Discord commands
@client.command()
async def export(ctx, logtype):
    if ctx.author.id == 204366690446737419:
        for guilds in masslist:
            if guilds['guid'] == ctx.guild.id:
                if logtype == 'user':
                    df = DataFrame(guilds['users'], columns=['name', 'cnt'])
                    df.to_csv(f'{ctx.guild.id}_user_log.csv') # export by server via command
                    await typing(ctx, 3)
                    await ctx.channel.send(file=File(f'{ctx.guild.id}_user_log.csv'))
                    print(f"[{datetime.now().strftime('%H:%M:%S')}] Exported message count log for {ctx.guild}!")
                elif logtype == 'time':
                    df = DataFrame(guilds['time'], columns=['time'])
                    df.to_csv(f'{ctx.guild.id}_time_log.csv')
                    await typing(ctx, 3)
                    await ctx.send(file=File(f'{ctx.guild.id}_time_log.csv'))
                    print(f"[{datetime.now().strftime('%H:%M:%S')}] Exported time log for {ctx.guild}!")
                else:
                    await typing(ctx, 2)
                    await ctx.channel.send('invalid argument')
    else:
        try:
            await typing(ctx, 1)
            await ctx.channel.send("you're not my master fuck off")
        except Forbidden:
            print(f"[{ctx.ctx.created_at.strftime('%H:%M:%S')}] Forbidden 403 Encountered")

# did not know help command exists :P
# @client.command()
# async def man(ctx):
#     try:
#         await typing(ctx, 2)
#         await ctx.channel.send("usage: josh ___ \ncommands:\nstats- displays internally logged stats (WIP) e.g. josh stats <discord tag>\nrate- modifies response rate (WIP) e.g. josh rate <discord tag>\nexport- sends a .csv of the data logged for this server\n\nman- sends this manual")
#     except Forbidden:
#         print(f"[{ctx.ctx.created_at.strftime('%H:%M:%S')}] Forbidden 403 Encountered")

@client.command()
async def stats(ctx, name):
    for guilds in masslist:
        if guilds['guid'] == ctx.guild.id:
            try:
                for user in guilds['users']:
                    if name == "me":
                        if ctx.author.id == user['uid']:
                            await typing(ctx, 2)
                            await ctx.channel.send(f"Josh Stats for {user['name']}, Message Count: {user['cnt']}, Rate: {round((100/user['dnm']), 1)}%")
                    else:
                        if (name == user['name']) or (name == f"<@{user['uid']}>"):
                            await typing(ctx, 2)
                            await ctx.channel.send(f"Josh Stats for {user['name']}, Message Count: {user['cnt']}, Rate: {round((100/user['dnm']), 1)}%")
            except Forbidden:
                print(f"[{ctx.ctx.created_at.strftime('%H:%M:%S')}] Forbidden 403 Encountered")

@client.command()
async def rate(ctx, user, ndnm):
    if ctx.author.id == 204366690446737419:
        for guilds in masslist:
            if guilds['guid'] == ctx.guild.id:
                if user == "everyone":
                    for users in guilds['users']:
                        if users['uid'] != 204366690446737419:
                            users['dnm'] = int(ndnm)
                    with open('user_log.json', 'w') as userfile:
                        dump(write, userfile, indent=2)
                    try:
                        await typing(ctx, 2)
                        await ctx.channel.send(f"Joshing rate for everyone: {round((100/int(ndnm)), 1)}%")
                    except Forbidden:
                        print(f"[{ctx.ctx.created_at.strftime('%H:%M:%S')}] Forbidden 403 Encountered")
                else:
                    for victim in guilds['users']:
                        if (user == victim['name']) or (user == f"<@{victim['uid']}>"):
                            victim['dnm'] = int(ndnm)
                            with open('user_log.json', 'w') as file:
                                dump(write, file, indent=2)
                            try:
                                await typing(ctx, 2)
                                await ctx.channel.send(f"Joshing rate for {victim['name']}: {round((100/victim['dnm']), 1)}%")
                            except Forbidden:
                                print(f"[{ctx.ctx.created_at.strftime('%H:%M:%S')}] Forbidden 403 Encountered")
    else:
        await typing(ctx, 1)
        await ctx.channel.send("you're not my master fuck off")

@client.event
async def on_command_error(ctx, error):
    if repr(error).startswith("MissingRequiredArgument"):
        try:
            await typing(ctx, 2)
            await ctx.channel.send("Missing argument(s)")
        except Forbidden:
            print(f"[{ctx.ctx.created_at.strftime('%H:%M:%S')}] Forbidden 403 Encountered")