
from turtle import title
import discord
from discord.ext import commands
import random

class usefulCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def diceRoller(self, ctx, numOfSides: int):
        # getting the roll
        roll = random.randint(1, numOfSides)

        # creating the embed
        embed = discord.Embed(title=f'You rolled a {numOfSides} sided dice and got a:')
        embed.add_field(name=f':game_die:', value=roll, inline=False)
        embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
        
        # showing the roll to the user
        await ctx.send(embed=embed)

    @commands.command()
    async def slots(self, ctx):
        emojiList = ["😀", "🍓", "🍒", "7️⃣", "🍑", "💀"]

        emoji1, emoji2, emoji3 = (random.choice(emojiList), random.choice(emojiList), random.choice(emojiList))

        # start making the embed
        embed = discord.Embed(title=f'Slots! (very legal)')

        value = "You lost!"
        # checking if emojis are the same
        if emoji1 == emoji2 and emoji2 == emoji3:
            value = "You won!"
        # creating and setting up the embed
        embed.add_field(name=f'{emoji1}|{emoji2}|{emoji3}', value=value)
        embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)
        
    
def setup(bot):
    bot.add_cog(usefulCog(bot))