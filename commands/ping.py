from discord.ext import commands
from commands.msg import getmsg


class ping(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ping")
    async def pingCmd(self, ctx):
        await ctx.message.delete()
<<<<<<< HEAD
        await ctx.send(getmsg(ctx.guild, "ping", "response").format(
            latency=round(int(self.bot.latency*1000), 1)))
=======
        try:
            await ctx.send(getmsg(ctx.guild, "ping").format(latency=round(int(self.bot.latency*1000), 1)))
        except KeyError:
            await ctx.send('Pong! Mon ping est de {0}ms'.format(round(int(self.bot.latency*1000), 1)))
>>>>>>> parent of 2d2966c... Created lang files and langs system using ping cmd
        return


def setup(bot):
    bot.add_cog(ping(bot))
