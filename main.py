import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Préfixe des commandes (optionnel, car on utilise les slash commands)
intents = discord.Intents.default()
intents.message_content = True  # Nécessaire si tu veux aussi des commandes par préfixe
bot = commands.Bot(command_prefix='!', intents=intents)

# Événement déclenché lorsque le bot est prêt
@bot.event
async def on_ready():
    print(f'Connecté en tant que {bot.user}')
    
    # Charger tous les cogs dans le dossier cogs
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')
            print(f'Cog {filename[:-3]} chargé')
    
    # Synchroniser les commandes slash
    try:
        synced = await bot.tree.sync()
        print(f"Commandes slash synchronisées : {len(synced)}")
    except Exception as e:
        print(f"Erreur lors de la synchronisation : {e}")

# Lancer le bot
bot.run(TOKEN)
