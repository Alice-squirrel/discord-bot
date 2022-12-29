import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    await bot.tree.sync()
    print("Botの起動が完了しました。")

@bot.tree.command()
async def ping(interaction):
    await interaction.response.send_message("pong")

bot.run("Your Token")