import discord 
from discord.ext import commands
import music
from discord_buttons import Button, ButtonStyle, ButtonContext, ButtonMessage, ButtonClient, ButtonCache


cogs = [music]

client = commands.Bot(commands_prefix='?', intents = discord.Intents.all())

for i in range(len(cogs)):
    cogs[i].setup(client)


#buttons




client.run('')