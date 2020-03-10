import discord
from discord.ext import commands

token = "Njg1MTk3MTA4Mjc3NDExODgz.XmFJug.Pr6_mGENgRGFIDzsk2YSfn27pX8"
GUILD = "ProXy Bot Dev"

prefix = "%"

adminRole = "admin"

botOwnerId = 330718440409137152

bot = commands.Bot(command_prefix=prefix)

def isBotOwner(ctx):
    return ctx.message.author.id == botOwnerId

@bot.command(name="ping")
async def pingCmd(ctx):
    await ctx.message.delete()
    await ctx.send('Pong! {0}'.format(round(bot.latency, 1)))
    return

@bot.command(name="args")
@commands.check(isBotOwner)
async def argsCmd(ctx, *args):
        await ctx.message.delete()
        await ctx.send('{} Arguments: {}'.format(len(args), ', '.join(args)))
        return

@bot.command(name="clear")
@commands.has_role(adminRole)
async def clearCmd(ctx, count: int=50, arg = None):
    await ctx.message.delete()
    await ctx.channel.purge(limit=count)
    try:
        if arg == None:
            await ctx.send("{0.author.mention} a supprimé ".format(ctx)+str(count)+" messages.")
    except:
        pass
    if arg == "s":
        pass
    if arg == "a":
        await ctx.send(str(count)+" messages ont été supprimé.")
    return

@bot.command(name="kick")
@commands.has_role(adminRole)
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
@commands.has_role(adminRole)
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
    async def msg():
        players = 0
        for guild in bot.guilds:
            for _ in guild.members:
                players += 1
        await ctx.send(f"Je sert dans {len(bot.guilds)} serveurs et aide {players} joueurs")

    if ctx.message.author.id == botOwnerId and arg == "full":
        await ctx.send(f'{bot.user.name} est connecter sur les serveurs suivant:')
        for guild in bot.guilds:
            members = '\n - '.join([member.name for member in guild.members])            
            await ctx.send("\n"+f'{guild.name}(id: {guild.id})\nMembres du serveur:\n - {members}')
        await ctx.send("Fin de la liste")
    if ctx.message.author.id == botOwnerId and arg == None:
        await msg()
    
    elif ctx.message.author.id != botOwnerId:
        await msg()

@bot.command(name="nbplayers")
async def nbsplayers(ctx):
    ctx.message.delete()
    await ctx.send(f"Il y a {len(ctx.guild.members)} membres sur le serveur {ctx.guild.name}")

# @bot.command(name="chatmute")
# @commands.has_role(adminRole)
# async def chatMuteCmd(ctx, player: discord.member=None, arg=None):
#     isMutedRoledCreated = False
#     for role in ctx.guild.roles:
#         if role.name == "Muted":
#             isMutedRoledCreated = True
#             break
    


@bot.command(name="hack")
@commands.check(isBotOwner)
async def hackCmd(ctx, id: int, player: discord.Member=None):
    await ctx.message.delete()
    await player.add_roles(ctx.guild.get_role(role_id=id))
    # 684092680703049767

@bot.command(name="exit")
@commands.check(isBotOwner)
async def exitCmd(ctx):
    await ctx.send("Stoppé")
    await ctx.message.delete()
    await bot.logout()
    return
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
    if member.id == 556577574189269016:
        await member.kick()
        print("supra kicked")
        return
    await member.create_dm()
    await member.dm_channel.send(f'{member.name}, Bienvenue sur le serveur')

bot.run(token)