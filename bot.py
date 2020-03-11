import discord, asyncio, os
from discord.ext import commands

token = "Njg1MTk3MTA4Mjc3NDExODgz.XmFJug.Pr6_mGENgRGFIDzsk2YSfn27pX8"
GUILD = "ProXy Bot Dev"
prefix = "%"
adminRole = "admin"
botOwnerId = 330718440409137152
bot = commands.Bot(command_prefix=prefix)
# # remove default help command
# bot.remove_command("help")
def isBotOwner(ctx):
    return ctx.message.author.id == botOwnerId
for filename in os.listdir("./commands"):
    if filename.endswith(".py"):
        bot.load_extension(f"commands.{filename[:-3]}")

# init
@bot.event
async def on_ready():
    print(f'{bot.user.name} est connecter sur Discord !')
    print(f'{bot.user.name} est connecter sur les serveurs suivant:')
    for guild in bot.guilds:
        print("\n"+f'{guild.name}(id: {guild.id})')
        members = '\n - '.join([member.name for member in guild.members])
        print(f'Membres du serveur:\n - {members}')
        
# Message de Bienvenue
@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f'{member.name}, Bienvenue sur le serveur {member.guild.name}')

bot.run(token)