import discord
from discord.ext import commands

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
    await ctx.send("grab grab grab")

@bot.command()
async def hello (ctx, a):
    await ctx.send(f"{a} hello!!")

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)}ms')

bot.remove_command('help')
@bot.command()
async def help(ctx):
    embed = discord.Embed(title='Pancake',description="A very good Album.List of commands are: ",color=0xeee657)

    embed.add_field(name='$grab', value='print "grab grab grab"', inline=False)
    embed.add_field(name='$ping', value='print robot\'s ping',inline=False)
    embed.add_field(name='$hello {message}', value='print {message} Hello!!',inline=False)
    await ctx.send(embed=embed)

TOKEN = "NjA3NTUzNzY0NzQzOTcwODMx.XUgnbw.kFw6_sd_e9Jph-9Cq-EX9HNWUE8"
bot.run(TOKEN)