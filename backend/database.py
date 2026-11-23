import sqlite3

def init_db():
    conn = sqlite3.connect('PomboTech.db')
    cursor = conn.cursor()
    
    # Criar tabela de produtos
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco REAL NOT NULL,
            imagem TEXT NOT NULL
        )
    ''')
    
    # Inserir dados de teste caso a tabela esteja vazia
    cursor.execute("SELECT COUNT(*) FROM produtos")
    if cursor.fetchone()[0] == 0:
        produtos_iniciais = [
            ('Processador Intel i7', 59.90, 'processador.jpg'),
            ('Monitor 120Hz', 399.90, 'monitor.jpg'),
            ('2P/Memoria ram 8gb', 129.90, 'memoria.jpg')
        ]
        cursor.executemany("INSERT INTO produtos (nome, preco, imagem) VALUES (?, ?, ?)", produtos_iniciais)
        conn.commit()

    conn.close()

def get_db_connection():
    conn = sqlite3.connect('PomboTech.db')
    conn.row_factory = sqlite3.Row
    return conn