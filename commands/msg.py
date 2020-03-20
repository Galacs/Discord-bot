import json
import os
from discord.ext import commands
<<<<<<< HEAD
from bot import isBotOwner

servers_settings = {}
langs = {}

for file in os.listdir("./msg/langs/"):
    langs[file[:-5]] = (json.load(open('./msg/langs/'+file)))

for file in os.listdir("./servers/"):
    servers_settings[file[:-5]] = (json.load(open('./servers/'+file)))


def reload_settings(a):
    json.dump(servers_settings, open(f"./servers/{str(a)}.json", "w"))


def getmsg(guild, r1, r2):
    data = json.load(open(f'./msg/custom_commands/{guild.id}.json'))
    try:
        d = data[r1][r2]
    except KeyError:
        d = langs[servers_settings[guild.id]["lang"]][r1][r2]
    return d
=======
def getmsg(guild, msg):
    return json.load(open(f'./servers/{guild.id}.json'))[msg]
>>>>>>> parent of 2d2966c... Created lang files and langs system using ping cmd


class msg(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="listettings")
    @commands.check(isBotOwner)
    async def listlangsCmd(self, ctx):
        await ctx.send(servers_settings)

    @commands.command(name="reloadsettings")
    @commands.check(isBotOwner)
    async def reload_settingsCmd(self, ctx):
        for file in os.listdir("./servers/"):
            servers_settings[int(file[:-5])] = (
                json.load(open('./servers/'+file)))

    @commands.command(name="listlangs")
    @commands.check(isBotOwner)
    async def list_langsCmd(self, ctx):
        await ctx.send(langs)

    @commands.Cog.listener()
    async def on_ready(self):
        if not os.path.exists("servers"):
            os.mkdir("servers")
        for guild in self.bot.guilds:
            try:
                data = json.load(open(f'./servers/{guild.id}.json'))
            except FileNotFoundError:
                data = {}
<<<<<<< HEAD
            try:
                json.load(open(f'./msg/custom_commands/{guild.id}.json'))
            except FileNotFoundError:
                json.dump({}, open(
                    f"./msg/custom_commands/{guild.id}.json", "w"))
=======
>>>>>>> parent of 2d2966c... Created lang files and langs system using ping cmd
            data["server_name"] = guild.name
            try:
                data["mute_channel_configured"]
            except KeyError:
                data["mute_channel_configured"] = False
            try:
                data["muted_role"]
            except KeyError:
                data["muted_role"] = 0
            json.dump(data, open(f"./servers/{guild.id}.json", "w"))
<<<<<<< HEAD
            for file in os.listdir("./servers/"):
                servers_settings[int(file[:-5])] = (
                    json.load(open('./servers/'+file)))
=======
>>>>>>> parent of 2d2966c... Created lang files and langs system using ping cmd

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        try:
            data = json.load(open(f'./servers/{guild.id}.json'))
        except FileNotFoundError:
            pass
        data = {}
        data["server_name"] = guild.name
        json.dump(data, open(f"./servers/{guild.id}.json", "w"))
        servers_settings[guild.id] = (json.load(open(
            './servers/'+f"{str(guild.id)}.json")))

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        try:
            os.remove(f"./servers/{guild.id}.json")
<<<<<<< HEAD
            os.remove(f"./msg/custom_commands/{guild.id}.json")
        except FileNotFoundError:
=======
        except:
>>>>>>> parent of 2d2966c... Created lang files and langs system using ping cmd
            pass
        del servers_settings[guild.id]

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
<<<<<<< HEAD
        data = json.load(open(f'./msg/custom_commands/{ctx.guild.id}.json'))
        try:
            data[r1][r2] = m
        except KeyError:
            data[r1] = {}
            data[r1][r2] = m
        json.dump(data, open(
            f"./msg/custom_commands/{ctx.guild.id}.json", "w"))
        await ctx.send(f"Le message {r1} {r2} a été changé pour {m}")
=======
        data = json.load(open(f'./servers/{ctx.guild.id}.json'))
        data[response] = message
        json.dump(data, open(f"./servers/{ctx.guild.id}.json", "w"))
        await ctx.send(f"Le message {response} a été changé pour {message}")
>>>>>>> parent of 2d2966c... Created lang files and langs system using ping cmd

    @commands.command(name="setdefault")
    @commands.has_permissions(administrator=True)
    async def setdefault(self, ctx, msg):
        await ctx.message.delete()
<<<<<<< HEAD
        data = json.load(open(f'./msg/custom_commands/{ctx.guild.id}.json'))
        if r2 is not None:
            del data[r1][r2]
        else:
            del data[r1]
        json.dump(data, open(
            f"./msg/custom_commands/{ctx.guild.id}.json", "w"))
        await ctx.send(f"Le message {r1} {r2} a étais remis à defaut")

=======
        data = json.load(open(f'./servers/{ctx.guild.id}.json'))
        del data[msg]
        json.dump(data, open(f"./servers/{ctx.guild.id}.json", "w"))
        await ctx.send(f"Le message {msg} a étais remis à defaut")
>>>>>>> parent of 2d2966c... Created lang files and langs system using ping cmd
    @commands.command(name="showallmsg")
    @commands.has_permissions(administrator=True)
    async def showallmsg(self, ctx):
        await ctx.message.delete()
<<<<<<< HEAD
        await ctx.send(json.load(open(
            f'./msg/custom_commands/{ctx.guild.id}.json')))

=======
        await ctx.send(json.load(open(f'./servers/{ctx.guild.id}.json')))
>>>>>>> parent of 2d2966c... Created lang files and langs system using ping cmd

def setup(bot):
    bot.add_cog(msg(bot))
