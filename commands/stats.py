import discord
from discord.ext import commands
from bot import isBotOwner

class stats(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="stats")
    async def statsCmd(self, ctx, arg=None):
        await ctx.message.delete()
        async def msg():
            players = 0
            for guild in self.bot.guilds:
                for _ in guild.members:
                    players += 1
            await ctx.send(f"Je sert dans {len(self.bot.guilds)} serveurs et aide {players} joueurs")

        if isBotOwner(ctx) and arg == "full":
            await ctx.send(f'{self.bot.user.name} est connecter sur les serveurs suivant:')
            for guild in self.bot.guilds:
                members = '\n - '.join([member.name for member in guild.members])            
                await ctx.send("\n"+f'{guild.name}(id: {guild.id})\nMembres du serveur:\n - {members}')
            await ctx.send("Fin de la liste")
        if isBotOwner(ctx) and arg == "server" or not isBotOwner(ctx) and arg == "server":
            members = '\n - '.join([member.name for member in ctx.guild.members])       
            await ctx.send("\n"+f'{ctx.guild.name}(id: {ctx.guild.id})\nMembres du serveur:\n - {members}')
            await ctx.send(f"Il y a {len(ctx.guild.members)} membres sur le serveur {ctx.guild.name}")
        if isBotOwner(ctx) and arg == None:
            await msg()
        
        elif not isBotOwner(ctx):
            await msg()

    @commands.command(name="nbplayers")
    async def nbsplayers(self, ctx):
        await ctx.message.delete()
        await ctx.send(f"Il y a {len(ctx.guild.members)} membres sur le serveur {ctx.guild.name}")

def setup(bot):
    bot.add_cog(stats(bot))
