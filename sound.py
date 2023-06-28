import asyncio
import json
import random

import discord
from discord.ext import commands

with open('config.json') as config:
    config = json.loads(config.read())

class Sound(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    session_token = 0 # This is used to identify when it has been stopped and restarted. 0 = not playing

    @commands.command(name='start')
    async def start(self, ctx):
        # Join the voice channel
        if not ctx.guild.voice_client:
            try:
                channel = ctx.author.voice.channel
            except:
                await ctx.send("You're not in a voice channel! Join a voice channel and I'll join you")
                return
            await channel.connect()

        # Store that we have started
        session_token = random.randint(1, 2**16)
        self.session_token = session_token

        # Output that we've started
        await ctx.send("Started workout messages")

        # Start playing the messages
        while True:
            if session_token != self.session_token or not ctx.guild.voice_client:
                break # it has been cancelled
            ctx.guild.voice_client.play(discord.FFmpegPCMAudio(source=config['audio_file'], executable=config['ffmpeg_path']))
            await asyncio.sleep(config['delay_in_minutes']*60)

    @commands.command(name='stop')
    async def stop(self, ctx):
        # Leave the voice channel
        if ctx.guild.voice_client:
            await ctx.guild.voice_client.disconnect()

        # Stop trying to play the message
        self.session_token = 0

        # Output
        await ctx.send("Stopped workout messages")


async def setup(bot):
    await bot.add_cog(Sound(bot))