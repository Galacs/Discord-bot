import json
import os
from discord.ext import commands
from bot import isBotOwner


class langs_utils(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.langs = {}

    @commands.Cog.listener()
    async def on_ready(self):
        for file in os.listdir("./msg/langs/"):
            self.langs[file[:-5]] = (json.load(open('./msg/langs/'+file)))

    @commands.command(name="listlangs1")
    @commands.check(isBotOwner)
    async def listlangsCmd(self, ctx):
        await ctx.send(self.langs)

    def get_langs(self):
        return self.langs


def setup(bot):
    bot.add_cog(langs_utils(bot))
