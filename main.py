import disnake as discord
from disnake.ext import commands
import asyncio
import functools
import itertools
import math
import random
import youtube_dl
from async_timeout import timeout
from discord.ext import commands
 
token = "token"
prefix = "!"
 
bot = commands.Bot(command_prefix=prefix)
bot.remove_command("help")
 
class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=commands.when_mentioned_or("$"))
 
    async def on_ready(self):
        print(f"Logged in as {self.user} (ID: {self.user.id})")
 
 
class testbuttons(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None
    @discord.ui.button(label="One", style=discord.ButtonStyle.green)
    async def one(self, button: discord.ui.Button, interaction: discord.MessageInteraction):
        await interaction.response.send_message("One", ephemeral=True)
        self.value = True
        self.stop()
 
    @discord.ui.button(label="Two", style=discord.ButtonStyle.green)
    async def two(self, button: discord.ui.Button, interaction: discord.MessageInteraction):
        await interaction.response.send_message("Two", ephemeral=True)
        self.value = True
        self.stop()
        
    @discord.ui.button(label="three", style=discord.ButtonStyle.green)
    async def three(self, button: discord.ui.Button, interaction: discord.MessageInteraction):
        await interaction.response.send_message("Three", ephemeral=True)
        self.value = True
        self.stop()
 
 
bot = Bot()
 
@bot.command()
async def ask(ctx: commands.Context):
    view = testbuttons()
 
 
    emb = discord.Embed(color=0x2F3136)
    file = discord.File("Images/image.png", filename="image.png")
    emb.set_image("attachment://image.png")
    a = await ctx.send(embed=emb, file=file, view=view)
    await view.wait()
    await a.delete()
 
