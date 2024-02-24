import os
import discord
from discord import Intents
from discord.ext import commands
from dotenv import load_dotenv
from services.bot_service import sync_commands
from src.services.gear_service import get_gear_score
from src.services import journal_service


intents = Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)


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


@bot.tree.command(name="create_journal_entry", description="Create a journal entry")
async def create_journal_entry(interaction: discord.Interaction, journal_entry: str,
                               year: int, month: int, day: int) -> None:
    """
    User inputs data to create a journal entry via discord slash command
    :param interaction: This is a discord message interaction
    :param journal_entry: string, user's journal entry
    :param year: integer, journal year
    :param month: integer, journal month
    :param day: integer, journal day
    :return: None
    """
    user = interaction.user.name
    journal_service.create_journal_entry(journal_entry=journal_entry, year=year, month=month, day=day, username=user)
    await interaction.response.send_message(f"Journal has been set", ephemeral=True)


@bot.tree.command(name="read_journal_entry", description="Read a journal entry")
async def read_journal_entry(interaction: discord.Interaction, year: int, month: int, day: int) -> None:
    """
    Displays user's journal entry for entered date
    :param interaction: This is a discord message interaction
    :param year: integer, journal year
    :param month: integer, journal month
    :param day: integer, journal day
    :return: None
    """
    user = interaction.user.name
    journal = journal_service.read_journal_entry(year=year, month=month, day=day, username=user)
    await interaction.response.send_message(f"Journal entry: {journal}", ephemeral=True)


@bot.tree.command(name="update_journal_entry", description="Update a journal entry")
async def update_journal_entry(interaction: discord.Interaction, year: int, month: int, day: int,
                               updated_journal_entry: str) -> None:
    """
    Place
    :param interaction:
    :param year:
    :param month:
    :param day:
    :param updated_journal_entry:
    :return:
    """
    user = interaction.user.name
    response = journal_service.update_journal_entry(year=year, month=month, day=day,
                                                    updated_journal_entry=updated_journal_entry, username=user)
    await interaction.response.send_message(response, ephemeral=True)


@bot.tree.command(name="delete_journal_entry", description="Delete a journal entry")
async def delete_journal_entry(interaction: discord.Interaction, year: int, month: int, day: int) -> None:
    """
    Place
    :param interaction:
    :param year:
    :param month:
    :param day:
    :return:
    """
    user = interaction.user.name
    response = journal_service.delete_journal_entry(year=year, month=month, day=day, username=user)
    await interaction.response.send_message(response, ephemeral=True)


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
