import discord 
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

#COMMANDES EN FONCITON D'UN AUTRE SIGNE (ici : !)
@bot.hybrid_command()
async def ping(ctx):
    await ctx.send("pong")


@bot.hybrid_command()
async def difference(ctx, a:int, b:int):
    await ctx.send(f"{a}-{b} = {a - b}")

@bot.event
async def on_ready(): #async permet de déclencher la fonction en meme temps que d'autres
    print("bot allumé !")
    
    #synchroniser les commandes/ gestion des erreurs
    try:
        synced = await bot.tree.sync()
        print(f"commande slash synchronisée : {len(synced)}")
    except Exception as e:
        print(e)

bot.run(token)