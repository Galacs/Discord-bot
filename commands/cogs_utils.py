from discord.ext import commands
from bot import isBotOwner


class cogs_utils(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="load")
    @commands.check(isBotOwner)
    async def loadCmd(self, ctx, extension):
        await ctx.message.delete()
        self.bot.load_extension(f'commands.{extension}')
        await ctx.send(f"{str(extension)} a été chargé")

    @commands.command(name="unload")
    @commands.check(isBotOwner)
    async def unloadCmd(self, ctx, extension):
        await ctx.message.delete()
        self.bot.unload_extension(f'commands.{extension}')
        await ctx.send(f"{str(extension)} a été déchargé")

    @commands.command(name="reload")
    @commands.check(isBotOwner)
    async def reloadCmd(self, ctx, extension):
        await ctx.message.delete()
        self.bot.unload_extension(f'commands.{extension}')
        self.bot.load_extension(f'commands.{extension}')
        await ctx.send(f"{str(extension)} a été rechargé")


def setup(bot):
    bot.add_cog(cogs_utils(bot))
