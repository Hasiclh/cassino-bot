import discord
from discord.ext import commands
import random
from dotenv import load_dotenv
import os

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Configurações do bot
TOKEN = os.getenv('DISCORD_TOKEN')

# Configurações do bot
PREFIX = '!'

# Inicializa o bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=PREFIX, intents=intents)

# Emojis para o caça-níquel
emojis = ["🍒", "🍋", "🍊", "🍇", "🔔", "💎", "7️⃣"]

# Comando para jogar o caça-níquel
@bot.command(name='777', help='777h')
async def jogar(ctx):
    # Gera três emojis aleatórios
    resultado = [random.choice(emojis) for _ in range(3)]
    
    # Envia o resultado
    await ctx.send(f"🎰 | {ctx.author.mention} girou o caça-níquel e obteve: {' '.join(resultado)}")
    
    # Verifica se o usuário ganhou
    if resultado[0] == resultado[1] == resultado[2]:
        await ctx.send(f"🎉 Parabéns! Você ganhou! 🎉")
    else:
        await ctx.send("Tente novamente!")
        
# Tratamento de erros para comandos inválidos
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):  # Comando não encontrado
        await ctx.send(f"❌ Comando inválido! Use `{PREFIX}777` para jogar o caça-níquel.")
    else:
        # Outros erros podem ser tratados aqui
        await ctx.send(f"Ocorreu um erro: {error}")
        
# Inicia o bot
try:
    bot.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Erro ao conectar: Token inválido ou incorreto. Verifique o token.")