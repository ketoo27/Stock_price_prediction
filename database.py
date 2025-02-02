import sqlite3

def connect_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Create a table for user information
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        username TEXT PRIMARY KEY,
                        password TEXT,
                        full_name TEXT,
                        email TEXT
                    )''')
    
    # Create a table for favorite stocks
    cursor.execute('''CREATE TABLE IF NOT EXISTS favorite_stocks (
                        username TEXT,
                        stock_symbol TEXT,
                        FOREIGN KEY(username) REFERENCES users(username)
                    )''')

    conn.commit()
    conn.close()

def add_user(username, password, full_name, email):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (username, password, full_name, email) VALUES (?, ?, ?, ?)',
                   (username, password, full_name, email))
    conn.commit()
    conn.close()

def get_user(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    data = cursor.fetchone()
    conn.close()
    return data

def add_favorite_stock(username, stock_symbol):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO favorite_stocks (username, stock_symbol) VALUES (?, ?)', 
                   (username, stock_symbol))
    conn.commit()
    conn.close()

def get_favorite_stocks(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT stock_symbol FROM favorite_stocks WHERE username = ?', (username,))
    stocks = cursor.fetchall()
    conn.close()
    return [stock[0] for stock in stocks]

def remove_favorite_stock(username, stock_symbol):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM favorite_stocks WHERE username = ? AND stock_symbol = ?', 
                   (username, stock_symbol))
    conn.commit()
    conn.close()
