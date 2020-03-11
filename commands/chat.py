import discord
from discord.ext import commands

class chat(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="chatmute")
    @commands.has_permissions(manage_messages=True)
    async def chatMuteCmd(self, ctx, player: discord.Member=None, arg=None):
        await ctx.message.delete()
        isMutedRoledCreated = False
        for role in ctx.guild.roles:
            if role.name == "Proxy Muted":
                isMutedRoledCreated = True
                break
        if not isMutedRoledCreated:
            await ctx.guild.create_role(name="Proxy Muted")
        
        mutedRole = None

        for role in ctx.guild.roles:
            if role.name == "Proxy Muted":
                mutedRole = role
                break

        for channel in ctx.guild.channels:
            await channel.set_permissions(mutedRole, send_messages=False, send_tts_messages=False)
        
        await player.add_roles(mutedRole)
        if arg == None:
            await ctx.send(f"{player.mention} a été chatmute par {ctx.author.mention}")
        elif arg == "a":
            await ctx.send(f"{player.mention} a été chatmute.")
        elif arg == "s":
            return

def setup(bot):
    bot.add_cog(chat(bot))
