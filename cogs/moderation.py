import discord 
from discord.ext import commands

class moderationCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True) #le bot regarde si il a le droit de bannir des gens
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'{member.name} a été exclu(e).')

async def setup(bot):
    await bot.add_cog(moderationCog(bot))