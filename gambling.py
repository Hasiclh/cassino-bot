import os
import discord
import random

from dotenv import load_dotenv
from discord.ext import commands

from games.jackpot import Jackpot
from economy.wallet import check_balance
from economy.database import create_table

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Cria a tabela wallets no banco de dados (se não existir)
create_table()

# Configurações do bot
TOKEN = os.getenv('DISCORD_TOKEN')

# Configurações do bot
#PREFIX = '!'

# Inicializa o bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", case_insensitive=True, intents=intents)

# Inicializa os jogos
jackpot = Jackpot()

# Comando para jogar o caça-níquel
@bot.command(name='jackpot', aliases=["777"] , help='help-jackpot')
async def play_jackpot(ctx):
    await jackpot.play(ctx)

@bot.command(name='wallet', aliases=["wwl"], help='Verifica o saldo da sua carteira')
async def saldo(ctx):
    balance = check_balance(ctx.author.id)
    await ctx.send(f"💰 | {ctx.author.mention}, seu saldo é **{balance}** PAIZÕES.")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("❌ Comando inválido! Use `!jackpot` ou `!777` para jogar.")
    else:
        await ctx.send(f"Ocorreu um erro: {error}")

# Inicia o bot
try:
    bot.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Erro ao conectar: Token inválido ou incorreto. Verifique o token.")