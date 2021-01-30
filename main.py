import discord

from keep_alive import keep_alive
from settings import TOKEN
from utils import get_search_history, search


client = discord.Client()


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "hi":
        await message.channel.send("hey")

    if message.content.startswith("!google"):
        user_id = message.author.id
        search_text = message.content[8:]
        if not search_text:
            await message.channel.send("Please provide a search term.")
        else:
            result = search(search_text, user_id)
            if not result:
                await message.channel.send("Oops, we could't find anything!")
            else:
                for item in result:
                    await message.channel.send(item)

    if message.content.startswith("!recent"):
        user_id = message.author.id
        search_text = message.content[8:]
        if not search_text:
            await message.channel.send(
                "Please provide a search term to fetch recent history."
            )
        else:
            result = get_search_history(search_text, user_id)
            if not result:
                await message.channel.send("Oops, we could't find anything!")
            else:
                await message.channel.send(result)

keep_alive()
client.run(TOKEN)
