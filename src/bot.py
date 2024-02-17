import os

import discord
from discord import Intents
from discord.ext import commands
from dotenv import load_dotenv

from services.bot_service import sync_commands
from src.services.gear_service import get_gear_score

intents = Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.tree.command(name="hello")
async def hello(interaction: discord.Interaction) -> None:
    """
    Simple test command.
    :param interaction: This is the discord message interaction
    :return: None
    """
    await interaction.response.send_message("Hello world", ephemeral=True)


@bot.tree.command(name="get_gear_score", description="Get your gear score")
async def gear_score(interaction: discord.Interaction, ap: int, awakening_ap: int, dp: int) -> None:
    """
    Takes in the users AP, Awakening AP, and DP and then runs the get_gear_score method found in the gear_service.py
    :param interaction: This is the discord message interaction
    :param ap: Users AP that can be found in the inventory (i) menu
    :param awakening_ap: Users Awakening AP that can be found in the inventory (i) menu
    :param dp: Users DP that can be found in the inventory (i) menu
    :return: None
    """
    gs = get_gear_score(ap=ap, awakening_ap=awakening_ap, dp=dp)
    await interaction.response.send_message(f"Your gear score is {gs}", ephemeral=True)


@bot.event
async def on_ready():
    """
    Ran at the startup of the bot. This will sync the slash commands to the bot.
    :return: None
    """
    print("Bot is ready")
    await sync_commands(bot=bot)


if __name__ == '__main__':
    # This is a main function in python and is what gets ran when you press the run button
    load_dotenv()
    token = os.getenv("TOKEN")
    bot.run(token)
