from asyncio import sleep
from discord.ext import commands
from json import dump
from logs.logs import userlist, write_user

# Establish client user
client = commands.Bot(command_prefix="josh ")

# Discord commands
@client.command()
async def stats(ctx, name):
    for user in userlist:
        if ctx.author.id == user['uid']:
            await ctx.channel.trigger_typing()
            await sleep(2)
            await ctx.channel.send(f"Josh Stats for {user['name']}, Message Count: {user['cnt']}, Rate: 1/{user['dnm']}")

@client.command()
async def rate(ctx, user, ndnm):
    if ctx.author.id == 204366690446737419:
        for victim in userlist:
            if user == victim['name']:
                victim['dnm'] = int(ndnm)
                await ctx.channel.trigger_typing()
                await sleep(2)
                await ctx.channel.send(f"Josh Stats for {victim['name']}, Message Count: {victim['cnt']}, Rate: 1/{victim['dnm']}")
                with open('user_log.json', 'w') as userfile:
                    dump(write_user, userfile, indent=2)
    else:
        await ctx.channel.trigger_typing()
        await sleep(1)
        await ctx.channel.send("you're not my master fuck off")
