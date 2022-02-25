from asyncio import sleep
from datetime import datetime
from bot_cmds.bot_commands import client
import discord

# pedophile slaughterhouse flood
async def ps_spam():
    counter = 1
    while True:
        channel = client.get_channel(939312650318405672) # slaughterhouse id 842573792747716618
        if counter == 1:
            await channel.send(file=discord.File(r'spam.png'))
            await channel.send('1 dead pedophile')
        else:
            await channel.send(file=discord.File(r'spam.png'))
            await channel.send(f'{counter} dead pedophiles')
        counter += 1
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Another pedophile fucking died lol")
        await sleep(599)