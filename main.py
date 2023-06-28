import json
import math
import random

from discord.ext import commands
import asyncio
import discord
import youtube_dl



with open('credentials.json') as credentials:
    credentials = json.loads(credentials.read())

bot = commands.Bot('!', intents=discord.Intents(3276541))

@bot.command(name='ping')
async def test(ctx):
    msg = await ctx.send("Pong!")
    ping = msg.created_at.timestamp() - ctx.message.created_at.timestamp()
    await msg.edit(content=f"Pong! ({math.floor(ping*1000)}ms)")

@bot.event
async def on_ready():
    print(f"All good to go! Logged in as {bot.user.name} ({bot.user.id})")
    await bot.load_extension('sound')

if __name__ == '__main__':
    bot.run(credentials['token'])