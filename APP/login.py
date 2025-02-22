import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

class UserDatabase:
    def __init__(self, db_name='user_accounts.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        """Cria a tabela de usuários se não existir"""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def add_user(self, username, password):
        """Adiciona um novo usuário ao banco de dados"""
        if self.user_exists(username):
            print("Erro: Nome de usuário já existe. Escolha outro nome.")
            return False
        
        hashed_password = generate_password_hash(password)
        self.cursor.execute('''
            INSERT INTO users (username, password)
            VALUES (?, ?)
        ''', (username, hashed_password))
        self.conn.commit()
        print(f"Usuário '{username}' cadastrado com sucesso!")
        return True

    def user_exists(self, username):
        """Verifica se um usuário já existe no banco de dados"""
        self.cursor.execute('''
            SELECT 1 FROM users WHERE username = ?
        ''', (username,))
        return self.cursor.fetchone() is not None

    def verify_user(self, username, password):
        """Verifica se as credenciais do usuário estão corretas"""
        self.cursor.execute('''
            SELECT password FROM users WHERE username = ?
        ''', (username,))
        result = self.cursor.fetchone()
        
        if result and check_password_hash(result[0], password):
            return True
        return False

    def close(self):
        """Fecha a conexão com o banco de dados"""
        self.conn.close()

# Função para interação com o usuário
def main():
    db = UserDatabase()

    while True:
        print("\n--- Menu ---")
        print("1. Criar nova conta")
        print("2. Verificar login")
        print("3. Sair")
        choice = input("Escolha uma opção: ")

        if choice == "1":
            username = input("Escolha um nome de usuário: ")
            password = input("Escolha uma senha: ")
            db.add_user(username, password)

        elif choice == "2":
            username = input("Digite seu nome de usuário: ")
            password = input("Digite sua senha: ")
            if db.verify_user(username, password):
                print("Login válido! Bem-vindo,", username)
            else:
                print("Credenciais inválidas.")

        elif choice == "3":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

    db.close()

if __name__ == "__main__":
    main()