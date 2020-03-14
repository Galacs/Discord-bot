import discord, json, os
from discord.ext import commands
def getmsg(guild, msg):
    return json.load(open(f'./servers/{guild.id}.json'))[msg]

class msg(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_ready(self):
        if not os.path.exists("servers"):
            os.mkdir("servers")
        for guild in self.bot.guilds:
            try:
                data = json.load(open(f'./servers/{guild.id}.json'))
            except FileNotFoundError:
                data = {}
            data["server_name"] = guild.name
            json.dump(data, open(f"./servers/{guild.id}.json", "w"))

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        try:
            data = json.load(open(f'./servers/{guild.id}.json'))
        except FileNotFoundError:
            pass
        data = {}
        data["server_name"] = guild.name
        json.dump(data, open(f"./servers/{guild.id}.json", "w"))

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        try:
            os.remove(f"./servers/{guild.id}.json")
        except:
            pass

    @commands.command(name="showmsg")
    @commands.has_permissions(administrator=True)
    async def msgCmd(self, ctx, msg: str):
        await ctx.message.delete()
        data = json.load(open(f'./servers/{ctx.guild.id}.json'))
        try:
            await ctx.send(data[msg])
        except KeyError:
            await ctx.send("Aucun message n'a été defini")
        
    
    @commands.command(name="setmsg")
    @commands.has_permissions(administrator=True)
    async def setmsgCmd(self, ctx, response: str,message: str):
        await ctx.message.delete()
        data = json.load(open(f'./servers/{ctx.guild.id}.json'))
        data[response] = message
        json.dump(data, open(f"./servers/{ctx.guild.id}.json", "w"))
        await ctx.send(f"Le message {response} a été changé pour {message}")

    @commands.command(name="setdefault")
    @commands.has_permissions(administrator=True)
    async def setdefault(self, ctx, msg):
        await ctx.message.delete()
        data = json.load(open(f'./servers/{ctx.guild.id}.json'))
        del data[msg]
        json.dump(data, open(f"./servers/{ctx.guild.id}.json", "w"))
        await ctx.send(f"Le message {msg} a étais remis à defaut")
    @commands.command(name="showallmsg")
    @commands.has_permissions(administrator=True)
    async def showallmsg(self, ctx):
        await ctx.message.delete()
        await ctx.send(json.load(open(f'./servers/{ctx.guild.id}.json')))

def setup(bot):
    bot.add_cog(msg(bot))
