import os
import discord


from keep_alive import keep_alive
from settings import TOKEN
from utils import (
    get_search_history,
    search
)


client = discord.Client()


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to Discord Bot Server!'
    )


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == 'hi':
        await message.channel.send('hey')

    if message.content.startswith("!google"):
        user_id = message.author.id
        search_text = message.content[8:]
        result = search(search_text, user_id)
        for item in result:
            await message.channel.send(item)

    if message.content.startswith("!recent"):
        user_id = message.author.id
        search_text = message.content[8:]
        result = get_search_history(search_text, user_id)
        await message.channel.send(result)

keep_alive()
client.run(TOKEN)
