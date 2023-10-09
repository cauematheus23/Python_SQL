import sqlite3

# Conecte-se ao banco de dados SQLite (isso criará um novo arquivo de banco de dados se ele não existir)
conn = sqlite3.connect('banco_loja.db')
cursor = conn.cursor()

"""# Modifique a tabela Cliente para usar CPF como chave primária
cursor.execute('''
    CREATE TABLE Cliente (
        CPF INTEGER PRIMARY KEY,
        Nome TEXT,
        Email TEXT,
        Endereco TEXT,
        Telefone TEXT
    )
''')

# Modifique a tabela Pedido para usar CPF em vez de IDCliente
cursor.execute('''
    CREATE TABLE Pedido (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        DataPedido DATETIME,
        Status TEXT,
        CPF INTEGER,
        FOREIGN KEY (CPF) REFERENCES Cliente(CPF)
    )
''')

# Modifique a tabela ItemPedido para usar CPF em vez de IDCliente e atualize a chave estrangeira para Cliente
cursor.execute('''
    CREATE TABLE ItemPedido (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Quantidade INTEGER,
        PrecoUnitario DECIMAL(10, 2),
        IDProduto INTEGER,
        CPF INTEGER,
        FOREIGN KEY (IDProduto) REFERENCES Produto(ID),
        FOREIGN KEY (CPF) REFERENCES Cliente(CPF)
    )
''')

cursor.execute('''
    CREATE TABLE Produto (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Nome TEXT,
        Descricao TEXT,
        Preco DECIMAL(10, 2),
        Estoque INTEGER
    )
''')
# Crie a tabela Estoque
cursor.execute('''
    CREATE TABLE Estoque (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        QuantidadeEmEstoque INTEGER,
        DataAtualizacao DATETIME,
        IDProduto INTEGER,
        FOREIGN KEY (IDProduto) REFERENCES Produto(ID)
    )
''')"""
# Salve as alterações e feche a conexão
cursor.execute('''ALTER TABLE cliente ADD COLUMN ID INTEGER AUTOINCREMENT''')
conn.commit()
conn.close()

print("Tabelas modificadas com sucesso.")
