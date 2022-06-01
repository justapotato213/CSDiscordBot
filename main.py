import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

# prefix used to interact with the bot
prefix =["?"] 

bot = commands.Bot(command_prefix=prefix, intents = discord.Intents.all())  

@bot.event
# runs when the bot is 
async def on_ready():
    channel = bot.get_channel(738892516790763554)
    await channel.send("Online")
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
    embed.add_field(name="Inline Embed 2", value="Value", inline=True)
    # sending the embed
    await ctx.send(embed=embed)

@bot.command()
async def commandWithArg(ctx, arg1):
    # checking the argument 
    if arg1 == "argument":
        await ctx.send("Sent an argument")
    # send the argument back
    else:
        await ctx.send(f'{arg1}')

# sample use for bot
@bot.event
async def on_message(message):
    # checking if message content contains something
    if message.content == "aritro":
        # deletes the message
        await message.delete()
    # required when using on_messsage in order to process both commands as well as this event
    await bot.process_commands(message)

# loading cogs
if __name__ == "__main__":
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py") and filename != "__init__.py":
            print(f"loaded: {filename}")
            bot.load_extension(f'cogs.{filename[:-3]}')

load_dotenv()

token = os.getenv("TOKEN")
bot.run(token)