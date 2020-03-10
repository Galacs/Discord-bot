import discord, os, sys
from io import StringIO

token = "Njg1MTk3MTA4Mjc3NDExODgz.XmFJug.Pr6_mGENgRGFIDzsk2YSfn27pX8"
GUILD = "ProXy Bot Dev"

client = discord.Client()

standardStdout = sys.stdout

prefix = "%"

try:
    isreloaded = bool(sys.argv[1])
except IndexError:
    isreloaded = False

@client.event
async def on_message(msg):
    msgStr = str(msg.content).split()
    if msg.author == client.user:
        return
    elif msgStr[0][0] != (prefix):
        return
    elif msgStr[0] == prefix + "ping":
        await msg.delete()
        await msg.channel.send("pong !")
        return
    elif msgStr[0] == prefix + "args":
        await msg.delete()
        await msg.channel.send('{} Arguments: {}'.format(len(msgStr), ', '.join(msgStr)))
        return

    elif msgStr[0] == prefix + "clear":
        await msg.delete()
        await msg.channel.purge(limit=int(msgStr[-1]))
        try:
            msgStr[1] = int(msgStr[1])
        except:
            pass
        try:
            if isinstance(msgStr[1], int):
                await msg.channel.send("{0.author.mention} a supprimé ".format(msg)+str(msgStr[1])+" messages.")
        except:
            pass
        if msgStr[1] == "-s":
            pass
        if msgStr[1] == "-a":
            await msg.channel.send(str(msgStr[2])+" messages ont été supprimé.")
        return

    elif msgStr[0] == prefix + "spam":
        await msg.delete()
        m = StringIO()
        sys.stdout = m
        print(*msgStr[2:], sep=" ")
        for _ in range(0, int(msgStr[1])):
            await msg.channel.send(str(m.getvalue()))
        sys.stdout = standardStdout
        return
    
    elif msgStr[0] == prefix + "exit":
        await msg.channel.send("Stoppé")
        await msg.delete()
        await client.logout()
        return
    
    elif msgStr[0] == prefix + "reload":
        await msg.channel.send("Rechargement en cours...")
        channelId = str(msg.channel.id)
        await msg.delete()
        await client.logout()
        os.execl(sys.executable, *["python", "discordBot.py", "True", channelId])
        return
    elif msgStr[0][0] == (prefix):
        await msg.delete()
        return

# init
@client.event
async def on_ready():
    print(f'{client.user} est connecter sur Discord !')
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    print(
        f'{client.user} est connecter sur le serveur suivant:\n'
        f'{guild.name}(id: {guild.id})'
    )
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Membres du serveur:\n - {members}')
    if isreloaded == True:
        await client.get_channel(int(sys.argv[2])).send("Rechargement terminé")
        
# Message de Bienvenue
@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f'{member.name}, Bienvenue sur le serv')
client.run(token)