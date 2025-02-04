import os
import discord
import random

from dotenv import load_dotenv
from discord.ext import commands

from games.jackpot import Jackpot

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Configurações do bot
TOKEN = os.getenv('DISCORD_TOKEN')

# Configurações do bot
#PREFIX = '!'

# Inicializa o bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Inicializa os jogos
jackpot = Jackpot()

# Comando para jogar o caça-níquel
@bot.command(name='jackpot', help='help-jackpot')
async def play_jackpot(ctx):
    await jackpot.play(ctx)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("❌ Comando inválido! Use `!caça-níquel` ou `!craps` para jogar.")
    else:
        await ctx.send(f"Ocorreu um erro: {error}")

# Inicia o bot
try:
    bot.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Erro ao conectar: Token inválido ou incorreto. Verifique o token.")