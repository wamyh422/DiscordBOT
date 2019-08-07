import discord
from discord.ext import commands
import json
import random

with open('setting.json','r',encoding='utf-8') as jFile:
    jdata = json.load(jFile)

bot = commands.Bot(command_prefix='$')
@bot.event
async def on_ready():
    print(">> Bot is online <<")
    print("Bot name: " + bot.user.name)
    print("Bot id: " + str(bot.user.id))
    print("Discord api version: " + discord.__version__)
    print('---------------------------')

@bot.command()
async def grab(ctx):

    pic_type = random.choice(['.gif','.jpg','.png'])
    pic_num = '0'
    if pic_type == '.gif':
        pic_num = '1'
    elif pic_type =='.jpg':
        pic_num ='2'
    elif pic_type =='.png':
        pic_num ='3'
    number = '1'
    if pic_num == '1':
        number = str(random.randrange(1,int(jdata['gif_size'])))
    elif pic_num =='2':
        number = str(random.randrange(1,int(jdata['jpg_size'])))
    elif pic_num =='3':
        number =str(random.randrange(1,int(jdata['png_size'])))
    
    pic = discord.File(jdata['pic_path']+pic_num+" ("+number+")"+pic_type)
    await ctx.send(file=pic)

@bot.command()
async def hello (ctx, a):
    await ctx.send(f"{a} hello!!")

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)}ms')

bot.remove_command('help')
@bot.command()
async def help(ctx):
    embed = discord.Embed(title='Pancake',description="A very good bot.List of commands are: ",color=0xeee657)

    embed.add_field(name='$grab', value='grab a picture', inline=False)
    embed.add_field(name='$ping', value='print robot\'s ping',inline=False)
    embed.add_field(name='$hello {message}', value='print {message} Hello!!',inline=False)
    await ctx.send(embed=embed)


bot.run(jdata['TOKEN'])