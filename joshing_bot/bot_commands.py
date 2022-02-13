from discord.ext import commands
client = commands.Bot(command_prefix="josh ")

@client.command()
async def ping(ctx):
    await ctx.channel.send("pong")