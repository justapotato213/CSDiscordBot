from discord.ext import commands

class exampleCog (commands.Cog):
    # initializing cog
    # setup like any class in python
    def __init__(self, bot):
        self.bot = bot
    
    # special stuff
    # more stuff that cogs can do can be found at https://discordpy.readthedocs.io/en/stable/ext/commands/cogs.html
    @commands.command()
    async def cogCommmand(self, ctx):
        await ctx.send("This command was sent from a cog")

def setup(bot):
    bot.add_cog(exampleCog(bot))
