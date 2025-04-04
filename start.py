import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from keep_alive import keep_alive

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

class monBot(commands.Bot):
    async def setup_hook(self):
        for extension in ['games', 'moderation']:
            await self.load_extension(f'cogs.{extension}')
        await self.tree.sync() #important car sinon je ne vois pas les commandes /

intents = discord.Intents.all()
bot = monBot(command_prefix='!', intents=intents)

keep_alive()
bot.run(token)
