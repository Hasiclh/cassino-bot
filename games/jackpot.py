import random

from economy.wallet import add_to_wallet

class Jackpot:
    def __init__(self):
# Emojis para o caça-níquel
        self.emojis = ["🍒", "🍋", "🍊", "🍇", "🔔", "💎", "7️⃣"]
        self.jackpot_emoji = "💎"
        self.jackpot_reward = 1000
        self.normal_reward = 100
        
    async def play(self, ctx):
        # Gera três emojis aleatórios
        result = [random.choice(self.emojis) for _ in range(3)]
    
        if result[0] == result[1] == result[2] == self.jackpot_emoji:
            reward = self.jackpot_reward
            mensagem_vitoria = f"🎉 **JACKPOT!** Você ganhou {reward} PAIZÕES! 🎉"
        elif result[0] == result[1] == result[2]:
            reward = self.normal_reward
            mensagem_vitoria = f"🎉 Parabéns! Você ganhou {reward} PAIZÕES! 🎉"
        else:
            reward = 0
            mensagem_vitoria = "Tente novamente!"
            
        # Adiciona a recompensa à carteira do usuário
        if reward > 0:
            add_to_wallet(ctx.author.id, reward)

        # Envia o resultado com uma quebra de linha
        await ctx.send(
            f"🎰 **Jackpot** 🎰\n"
            f"{ctx.author.mention} girou o caça-níquel e obteve:\n\n"
            f"{' '.join(result)}\n\n"
            f"---------------------------------\n"
        )
        # Envia o resultado
        await ctx.send(mensagem_vitoria)