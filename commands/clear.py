import discord
from discord.ext import commands

class clear(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="clear")
    @commands.has_permissions(manage_messages=True)
    async def clearCmd(self, ctx, count: int=50, arg = None):
        await ctx.message.delete()
        await ctx.channel.purge(limit=count)
        try:
            if arg == None:
                await ctx.send("{0.author.mention} a supprimé ".format(ctx)+str(count)+" messages.")
        except:
            pass
        if arg == "s":
            pass
        if arg == "a":
            await ctx.send(str(count)+" messages ont été supprimé.")
        return

def setup(bot):
    bot.add_cog(clear(bot))
