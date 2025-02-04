from .database import add_money, get_balance

# Adiciona dinheiro à carteira de um usuário
def add_to_wallet(user_id, amount):
    add_money(user_id, amount)

# Verifica o saldo de um usuário
def check_balance(user_id):
    return get_balance(user_id)