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

@bot.command(name="kick")
@commands.has_permissions(kick_members=True)
async def kickCmd (ctx, member: discord.Member=None, arg=""):
    await ctx.message.delete()
    await member.kick()
    if arg == "":
        await ctx.send(f"{ctx.author.mention} a kick {member.mention}")
    elif arg == 's':
        pass
    elif arg == "a":
        await ctx.send(f"{member.mention} a était kick")

@bot.command(name="ban")
@commands.has_permissions(ban_members=True)
async def banCmd (ctx, member: discord.Member=None, arg="", days="5"):
    await ctx.message.delete()
    await member.ban(delete_message_days=days)
    if arg == "":
        await ctx.send(f"{ctx.author.mention} a ban {member.mention}")
    elif arg == 's':
        pass
    elif arg == "a":
        await ctx.send(f"{member.mention} a était ban")

@bot.command(name="spam")
@commands.check(isBotOwner)
async def spamCmd(ctx, count: int, msg):
    await ctx.message.delete()
    for _ in range(0, count):
        await ctx.send(msg)
    return

@bot.command(name="stats")
async def statsCmd(ctx, arg=None):
    await ctx.message.delete()
    async def msg():
        players = 0
        for guild in bot.guilds:
            for _ in guild.members:
                players += 1
        await ctx.send(f"Je sert dans {len(bot.guilds)} serveurs et aide {players} joueurs")

    if isBotOwner(ctx) and arg == "full":
        await ctx.send(f'{bot.user.name} est connecter sur les serveurs suivant:')
        for guild in bot.guilds:
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

@bot.command(name="nbplayers")
async def nbsplayers(ctx):
    await ctx.message.delete()
    await ctx.send(f"Il y a {len(ctx.guild.members)} membres sur le serveur {ctx.guild.name}")


@bot.command(name="timer")
async def countdown(ctx, time: int=10):
    await ctx.message.delete()
    msg = await ctx.send(str(time))
    for i in range(time-1, 0, -1):
        await asyncio.sleep(1)
        await msg.edit(content=str(i))
    await asyncio.sleep(1)
    await msg.edit(content=f"{ctx.message.author} Le Timer de {str(time)} secondes est terminé")

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