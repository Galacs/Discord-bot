import discord
from discord.ext import commands

class ban(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ban")
    @commands.has_permissions(ban_members=True)
    async def banCmd (self, ctx, member: discord.Member=None, arg="", days="5"):
        await ctx.message.delete()
        await member.ban(delete_message_days=days, reason=f"Ban par {str(ctx.message.author)}")
        if arg == "":
            await ctx.send(f"{ctx.author.mention} a banni(e) {member.mention}")
        elif arg == 's':
            pass
        elif arg == "a":
            await ctx.send(f"{member.mention} a était banni(e)")


def setup(bot):
    bot.add_cog(ban(bot))
