from discord.ext import commands
import random

class gamesCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def roll(self,ctx):
        result = random.randint(1,6)
        await ctx.send(f'{ctx.author.name} lance un dé : {result}')

    @commands.hybrid_command()
    async def pileouface(self, ctx):
        result = random.choice(['pile', 'face'])
        await ctx.send(f'Résultat obtenu : {result}')

async def setup(bot):
    await bot.add_cog(gamesCog(bot))