"""
Contains helper methods for the bot.py file. These commands directly relate to the bot and do not do anything else.
"""
from discord.ext.commands import Bot


async def sync_commands(bot: Bot):
    """
    Syncs the tree commands. Tree commands for reference are the "slash" commands that allow you to use the "/" in
    discord. This can take up to an hour to correctly sync the commands so give it time.
    :param bot: Bot that was initialized within the bot.py
    """
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)
