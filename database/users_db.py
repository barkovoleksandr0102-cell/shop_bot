import sqlite3


class UsersDB:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER UNIQUE,
                username TEXT,
                balance INTEGER DEFAULT 0
            )
        ''')
        self.conn.commit()

    def add_user(self, user_id, username):
        try:
            self.cursor.execute('''
                INSERT INTO users (user_id, username)
                VALUES (?, ?)
            ''', (user_id, username))
            self.conn.commit()
        except sqlite3.IntegrityError:
            pass  # User already exists

    def get_user(self, user_id):
        self.cursor.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
        return self.cursor.fetchone()

    def update_balance(self, user_id, amount):
        self.cursor.execute('''
            UPDATE users
            SET balance = balance + ?
            WHERE user_id = ?
        ''', (amount, user_id))
        self.conn.commit()

    def close(self):
        self.conn.close()


DB = UsersDB('users.db')