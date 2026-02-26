import discord
from discord.ext import commands
from datetime import datetime
import os

TOKEN = os.getenv("DISCORD_TOKEN")

CHANNEL_ID = 1452658813537878138  # ID del canal donde avisar

intents = discord.Intents.default()
intents.members = True
intents.presences = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"✅ Bot conectado como {bot.user}")


@bot.event
async def on_presence_update(before, after):
    # Ignorar bots
    if after.bot:
        return

    # Solo avisar si estaba offline y ahora está online
    if before.status == discord.Status.offline and after.status == discord.Status.online:

        channel = bot.get_channel(CHANNEL_ID)

        if channel:
            hora = datetime.now().strftime("%H:%M")
            await channel.send(f"🟢 {after.name} se conectó a las {hora}")


bot.run(TOKEN)