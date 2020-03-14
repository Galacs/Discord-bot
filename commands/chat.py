import discord, json
from discord.ext import commands

class chat(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="chatmute")
    @commands.has_permissions(manage_messages=True)
    async def chatMuteCmd(self, ctx, player: discord.Member=None, arg=None):
        await ctx.message.delete()
        data = json.load(open(f'./servers/{ctx.guild.id}.json'))
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
                data["muted_role"] = role.id
                break
        if data["mute_channel_configured"] == False:
            for channel in ctx.guild.channels:
                await channel.set_permissions(mutedRole, send_messages=False, send_tts_messages=False)
            
        data["mute_channel_configured"] = True
        json.dump(data, open(f"./servers/{ctx.guild.id}.json", "w"))
        await player.add_roles(mutedRole)
        if arg == None:
            await ctx.send(f"{player.mention} a été chatmute par {ctx.author.mention}")
        elif arg == "a":
            await ctx.send(f"{player.mention} a été chatmute.")
        elif arg == "s":
            return

    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel):
        await channel.set_permissions(channel.guild.get_role(json.load(open(f'./servers/{channel.guild.id}.json'))["muted_role"]), send_messages=False, send_tts_messages=False)

def setup(bot):
    bot.add_cog(chat(bot))
