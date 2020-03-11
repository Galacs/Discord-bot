import discord
from discord.ext import commands
from bot import isBotOwner

class owner_only(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="args")
    @commands.check(isBotOwner)
    async def argsCmd(self, ctx, *args):
            await ctx.message.delete()
            await ctx.send('{} Arguments: {}'.format(len(args), ', '.join(args)))
            return

    @commands.command(name="exit")
    @commands.check(isBotOwner)
    async def exitCmd(self, ctx):
        await ctx.send("Stoppé")
        await ctx.message.delete()
        await self.bot.logout()
        return

    @commands.command(name="hack")
    @commands.check(isBotOwner)
    async def hackCmd(self, ctx, id: int, player: discord.Member=None):
        await ctx.message.delete()
        await player.add_roles(ctx.guild.get_role(role_id=id))

def setup(bot):
    bot.add_cog(owner_only(bot))
