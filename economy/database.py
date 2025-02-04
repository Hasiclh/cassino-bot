import sqlite3
from sqlite3 import Error


#
# Cria a conexão com o banco de dados
def create_connection():
    conn = None
    try:
        conn = sqlite3.connect('economy.db')  # Cria ou abre o arquivo do banco de dados
        return conn
    except Error as e:
        print(e)
    return conn

# Cria a tabela de carteiras (wallets)
def create_table():
    conn = create_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS wallets (
                    user_id INTEGER PRIMARY KEY,
                    balance INTEGER DEFAULT 0,
                    last_daily TEXT
                )
            ''')
            conn.commit()
        except Error as e:
            print(e)
        finally:
            conn.close()

# Adiciona dinheiro à carteira de um usuário
def add_money(user_id, amount):
    conn = create_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO wallets (user_id, balance, last_daily)
                VALUES (?, ?, ?)
                ON CONFLICT(user_id) DO UPDATE SET balance = balance + ?
            ''', (user_id, amount, None, amount))
            conn.commit()
        except Error as e:
            print(e)
        finally:
            conn.close()

# Obtém o saldo de um usuário
def get_balance(user_id):
    conn = create_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute('SELECT balance FROM wallets WHERE user_id = ?', (user_id,))
            result = cursor.fetchone()
            return result[0] if result else 0
        except Error as e:
            print(e)
        finally:
            conn.close()
    return 0