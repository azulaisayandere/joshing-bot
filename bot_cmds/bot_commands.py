from discord.ext import commands
from chat import type_wait
from logs import logs

# Establish client user
client = commands.Bot(command_prefix="josh ")

# Discord commands
@client.command()
async def stats(ctx):
    for user in logs.userlist:
        if ctx.author.id == user['uid']:
            await type_wait.type_wait(ctx.message)
            await ctx.channel.send(f"Josh Stats for {user['name']}, Message Count: {user['cnt']}, Rate: 1/{user['dnm']}")
