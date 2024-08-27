import discord
from discord.ext import commands
from IA import get_class
import os
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
    

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_url = attachment.url
            file_name = attachment.filename
            await attachment.save(f"./{attachment.filename}") 
            await ctx.send(get_class(image_path=f'./ {attachment.filename}', model_path=f'./keras_model.h5'), labels_path=f'./labels.txt')
    else:
        await ctx.send("no hay imagenes")
        

bot.run("MTI3MzA3MDQ5Mjk2NTkzMzE0Nw.GwwC9L.YwlGnFlsQpfUXSVL356-MuyrLJtxnMWTfaEVIo")

