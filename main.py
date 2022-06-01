
import discord, os
from discord.ext import commands

# prefix used to interact with the bot
prefix =["?"] 

bot = commands.Bot(command_prefix=prefix, intents = discord.Intents.all())  

@bot.event
# runs when the bot is 
async def on_ready():
    print("Connnected")
    # changing the status of the bot
    await bot.change_presence(activity=discord.Streaming(name="potatoes", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")), 

@bot.command()
async def helloWorld(ctx):
    # sending a basic message
    await ctx.send("Hello World")

@bot.command()
async def embedTest(ctx):
    # setting up the embed
    embed = discord.Embed(title="Test Embed")
    embed.add_field(name="Field I", value="Value", inline=False)
    embed.add_field(name="Inline Embed", value="Value", inline=True)
    # sending the embed
    await ctx.send(embed)

@bot.command()
async def commandWithArg(ctx, arg1):
    # checking the argument 
    if arg1 == "argument":
        await ctx.send("Sent an argument")
    # send the argument back
    else:
        await ctx.send(f'{arg1}')

token = os.getenv("DISCORD_TOKEN")
bot.run(token)