from discord.ext import commands

# Establish client user
client = commands.Bot(command_prefix="josh ")

# Discord commands
@client.command()
async def ping(ctx):
    await ctx.channel.send("pong")