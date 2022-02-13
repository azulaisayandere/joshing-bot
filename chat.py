import asyncio
import random
from discord import Forbidden, HTTPException
from logs import userlist

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
    await message.channel.trigger_typing()
    if len(message.content) >= 38:
        await asyncio.sleep(2)
    elif len(message.content) < 38:
        await asyncio.sleep(1)

async def speak(message):
    if message.guild.id == 937380112771477564: # test server id 937380112771477564 bad bois server id 579399140769923102
        for users in userlist:
            if message.author.id == users['uid']:
                dnm = users['dnm']
    else:
        if message.author.id == 204366690446737419: # blacklist self outside bad bois
            dnm = 200
        else:
            dnm = 40

    x = random.randint(1, dnm)

    if (len(message.content) <= 75) and (x == 1):
        if (message.content.startswith('-')) or (message.content.startswith('!')):
            try:
                print(f"[{message.created_at.strftime('%H:%M:%S')}] Invalid message received (bot command)")
            except TypeError: # cant start message with '!'
                print(f"[{message.created_at.strftime('%H:%M:%S')}] TypeError Encountered with invalid message (bot command)")
        elif (message.content.startswith('http')):
            print(f"[{message.created_at.strftime('%H:%M:%S')}] Invalid message received (external link)")
        elif  (message.content.startswith('<@!')):
            print(f"[{message.created_at.strftime('%H:%M:%S')}] Invalid message received (tagged user)")
        elif (message.content.startswith('<A:')):
            print(f"[{message.created_at.strftime('%H:%M:%S')}] Invalid message received (Nitro emoji)")
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
