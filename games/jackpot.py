import random

class Jackpot:
    def __init__(self):
# Emojis para o caça-níquel
        self.emojis = ["🍒", "🍋", "🍊", "🍇", "🔔", "💎", "7️⃣"]

    async def play(self, ctx):
        # Gera três emojis aleatórios
        result = [random.choice(self.emojis) for _ in range(3)]
    
        # Envia o resultado
        await ctx.send(f"🎰 | {ctx.author.mention} girou o caça-níquel e obteve: {' '.join(result)}")
    
        # Verifica se o usuário ganhou
        if result[0] == result[1] == result[2]:
            await ctx.send(f"🎉 Parabéns! Você ganhou! 🎉")
        else:
            await ctx.send("Tente novamente!")
        