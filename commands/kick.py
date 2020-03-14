import discord
from discord.ext import commands

class kick(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="kick")
    @commands.has_permissions(kick_members=True)
    async def kickCmd (self, ctx, member: discord.Member=None, arg=""):
        await ctx.message.delete()
        await member.kick(reason=f"Kick par {str(ctx.message.author)}")
        if arg == "":
            await ctx.send(f"{ctx.author.mention} a kick {member.mention}")
        elif arg == 's':
            pass
        elif arg == "a":
            await ctx.send(f"{member.mention} a était kick")


def setup(bot):
    bot.add_cog(kick(bot))
