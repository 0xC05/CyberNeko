import discord
from discord.ext import commands
import base64
import asyncio
import os
import json
import urllib.request

bot = commands.Bot(command_prefix='!')
dirname = os.path.dirname(__file__)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)

@bot.command()
async def b64dec(ctx, b64str: str):
    await ctx.send('The decoded string is - ' + "```" + str(base64.b64decode(b64str), 'utf-8') + "```")

@bot.command()
async def b64enc(ctx, b64str: str):
    await ctx.send('The encoded string is - ' + "```" + str(base64.b64encode(bytes(b64str, 'utf-8')), 'utf-8') + "```")

@bot.command()
async def hello(ctx):
    await ctx.send('Hello! My name is CyberNeko and I am gonna break your nico nico kneecaps!')

@bot.command()
async def listofcommands(ctx):
    helpstr = '```Hello! My name is CyberNeko and here are the commands that you can use!\n\n!listofcommands - List of commands and how they work.\n!b64enc - Encode a string in Base64. Input the string in quotes if your string has spaces in it. [eg - !b64enc "test string"]\n!b64dec - Decode a string encoded in Base64. [eg - !base64 <base64-string>]\n\nNew commands are being implimented! Please tell SYN to wake the fuck up!```'
    await ctx.send(helpstr)

@bot.command()
async def crisishelp(ctx, country: str):
    churl = 'https://0xc05.pw/crisishelp/' + country + '.json'
    chdata = urllib.request.urlopen(churl)
    chjsondata = json.load(chdata)

    await ctx.send('```' + chjsondata[0]['crisishelp'] + '```')

@bot.command()
async def fuckyou(ctx):
    voice = await ctx.message.author.voice.channel.connect()
    fuckyoump3 = os.path.join(dirname, 'fuckyou.mp3')
    voice.play(discord.FFmpegPCMAudio(fuckyoump3))
    await asyncio.sleep(3)
    await ctx.voice_client.disconnect()

bot.run('token')
