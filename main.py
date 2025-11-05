from discord.ext import commands
from dotenv import load_dotenv, find_dotenv

import os
import discord
import asyncio

from utils.events import list_events, show_event
from utils.teams import show_team

load_dotenv()
TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix = "?", intents = intents, help_command = None)

@bot.event
async def on_ready():
    print(f'{bot.user} au rapport.')

async def cogs():
    await bot.load_extension("cogs.events")
    #await bot.load_extension("cogs.ctf")
    await bot.load_extension("cogs.teams")

async def main():
    await cogs()
    await bot.start(TOKEN)

asyncio.run(main())
