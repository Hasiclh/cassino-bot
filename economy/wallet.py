from sqlite3 import Error
from datetime import datetime

from .database import add_money, get_balance, create_connection

# Adiciona dinheiro à carteira de um usuário
def add_to_wallet(user_id, amount):
    add_money(user_id, amount)

# Verifica o saldo de um usuário
def check_balance(user_id):
    return get_balance(user_id)


# Verifica se o usuário já usou o daily hoje
def can_use_daily(user_id):
    conn = create_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute('SELECT last_daily FROM wallets WHERE user_id = ?', (user_id,))
            result = cursor.fetchone()
            if result and result[0]:
                last_daily = datetime.fromisoformat(result[0])
                return last_daily.date() < datetime.utcnow().date()
            return True  # Se não houver registro, o usuário pode usar o daily
        except Error as e:
            print(e)
        finally:
            conn.close()
    return False

# Atualiza a data do último daily e adiciona o dinheiro
def use_daily(user_id, amount):
    conn = create_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO wallets (user_id, balance, last_daily)
                VALUES (?, ?, ?)
                ON CONFLICT(user_id) DO UPDATE SET
                    balance = balance + ?,
                    last_daily = ?
            ''', (user_id, amount, datetime.utcnow().isoformat(), amount, datetime.utcnow().isoformat()))
            conn.commit()
        except Error as e:
            print(e)
        finally:
            conn.close()