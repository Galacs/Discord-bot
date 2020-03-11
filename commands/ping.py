import discord
from discord.ext import commands

class ping(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ping")
    async def pingCmd(self, ctx):
        await ctx.message.delete()
        await ctx.send('Pong! Mon ping est de {0}ms'.format(round(int(self.bot.latency*1000), 1)))
        return

def setup(bot):
    bot.add_cog(ping(bot))
