import discord
from discord.ext import commands

class welcome_message(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        await member.create_dm()
        await member.dm_channel.send(f'{member.name}, Bienvenue sur le serveur {member.guild.name}')

def setup(bot):
    bot.add_cog(welcome_message(bot))
