import discord
from discord.ext import commands

class start_message(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.bot.user.name} est connecter sur Discord !')
        print(f'{self.bot.user.name} est connecter sur les serveurs suivant:')
        for guild in self.bot.guilds:
            print("\n"+f'{guild.name}(id: {guild.id})')
            members = '\n - '.join([member.name for member in guild.members])
            print(f'Membres du serveur:\n - {members}')

def setup(bot):
    bot.add_cog(start_message(bot))
