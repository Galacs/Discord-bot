from discord.ext import commands
from commands.msg import getmsg


class ping(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ping")
    async def pingCmd(self, ctx):
        await ctx.message.delete()
        await ctx.send(getmsg(ctx.guild, "ping", "response").format(
            latency=round(int(self.bot.latency*1000), 1)))
        return


def setup(bot):
    bot.add_cog(ping(bot))
