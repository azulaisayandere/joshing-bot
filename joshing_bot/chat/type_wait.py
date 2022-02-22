import asyncio

# pseudo-typing for character establishing
async def type_wait(message):
    await message.channel.trigger_typing()
    if len(message.content) >= 38:
        await asyncio.sleep(2)
    elif len(message.content) < 38:
        await asyncio.sleep(1)