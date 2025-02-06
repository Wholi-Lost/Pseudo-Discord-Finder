import discord
from discord.ext import commands
import json

TOKEN = ""
intents = discord.Intents.default()
intents.members = True  
bot = commands.Bot(command_prefix="!", intents=intents)


def load_pseudos():
    try:
        with open("pseudos.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_pseudos(data):
    with open("pseudos.json", "w") as f:
        json.dump(data, f, indent=4)

pseudos = load_pseudos()

@bot.event
async def on_ready():
    print(f"Connecté en tant que {bot.user}")

@bot.event
async def on_member_update(before, after):
    if before.nick != after.nick:
        user_id = str(after.id)
        if user_id not in pseudos:
            pseudos[user_id] = []
        if before.nick and before.nick not in pseudos[user_id]:
            pseudos[user_id].append(before.nick)
        save_pseudos(pseudos)

@bot.command()
async def look(ctx):
    
    user_id = str(ctx.author.id)
    member = ctx.guild.get_member(ctx.author.id)
    
    if member:
        if user_id in pseudos and pseudos[user_id]:
            last_nick = pseudos[user_id][-1]  
            await ctx.send(f"Le dernier pseudo de {member.mention} était : {last_nick}")
        else:
            await ctx.send(f"{member.mention} n'a pas d'anciens pseudos enregistrés.")
    else:
        await ctx.send("Utilisateur introuvable sur ce serveur.")

bot.run(TOKEN)
