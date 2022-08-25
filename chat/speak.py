from asyncio import sleep
from discord import Forbidden, HTTPException
from logs.logs import masslist
from random import randint

# josh the message
def josh(message):
    ret = ""
    i = False # capitalize second letter
    for char in message:
        if i:
            ret += char.upper()
        else:
            ret += char.lower()
        if char != ' ':
            i = not i
    return ret

# pseudo-typing for character establishing
async def type_wait(message):
    await message.channel.typing()
    if len(message.content) >= 38:
        await sleep(3)
    elif len(message.content) < 38:
        await sleep(1.5)

# automatically checks for targeted response conditions
async def speak(message):
    for guilds in masslist:
        if guilds['guid'] == message.guild.id:
            for users in guilds['users']:
                if users['uid'] == message.author.id:
                    dnm = users['dnm']

    x = randint(1, dnm)

    if (len(message.content) <= 75) and (x == 1):
        if (message.content.startswith('-')) or (message.content.startswith('!')) or (message.content.startswith(';;')):
            try:
                print(f"[{message.created_at.strftime('%H:%M:%S')}] Invalid message received (bot command)")
            except TypeError: # cant start message with '!'
                print(f"[{message.created_at.strftime('%H:%M:%S')}] TypeError encountered with invalid message (bot command)")
        elif (message.content.startswith('http')) or (message.content.startswith('<@')) or (message.content.startswith('<A:')):
            print(f"[{message.created_at.strftime('%H:%M:%S')}] Invalid message received")
        else:
            try:
                result = josh(message.content) 
                try:
                    await type_wait(message)
                    await message.channel.send(result)
                    print("[{}] Reply sent to {} in {}! Response Chance: {}%".format(message.created_at.strftime('%H:%M:%S'), message.author, message.guild.name, round((100 / dnm), 2)))
                except HTTPException:
                    print(f"[{message.created_at.strftime('%H:%M:%S')}] Invalid message received (empty msg)") # Josh will sometimes try to josh an image
            except Forbidden:
                    print(f"[{message.created_at.strftime('%H:%M:%S')}] Forbidden 403 Encountered")