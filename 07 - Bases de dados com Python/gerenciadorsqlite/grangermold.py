from pyclbr import Class
import sqlite3  # Biblioteca SQLite

class BDSQLite:
    def menu(self):
        print('GERENCIADOR DE BANCO DE DADOS SQLite3\n\n\n')
        print("01 - Criar Banco de Dados\n" + 
            "02 - Editar Banco de Dados Existente")

"""

conexao = sqlite3.connect('basededados.db') # Variavel que recebe o módulo sqlite3
cursor = conexao.cursor() # Objeto de cursor

# Criando a tabela
cursor.execute('CREATE TABLE IF NOT EXISTS clientes ('
               'id INTEGER PRIMARY KEY AUTOINCREMENT,'
               'nome TEXT,'
               'peso REAL'
               ')')

# Inserindo um registro na tabela (dados)
cursor.execute('INSERT INTO clientes (nome, peso) VALUES ("Daniel", 78.5)')
# Outra Forma de  inserir dados mas prevenindo o SQL injection
cursor.execute('INSERT INTO clientes (nome, peso) VALUES (?, ?)', ('Maria', 50))
cursor.execute(
    'INSERT INTO clientes (nome, peso) VALUES (?, ?)',
    {'id: None, 'nome': 'Maria', 'peso': 75}

)cursor.execute(
    'INSERT INTO clientes (:id, :nome, :peso)',
    {'nome': 'Maria', 'peso': 75}
)
# Executar o comando anterior
conexao.commit()

# Mostrar tabela clientes
cursor.execute('SELECT * FROM clientes')

# Buscar todos os valores
for linha in cursor.fetchall():
    print(linha) # Tupla com as colunhas

# Atualizar dados
cursor.execute(
    'UPDATE clientes SET nome=:nome WHERE id=:id',
    {'nome': 'Joana', 'id': 2})
    
# Deletar dados
cursor.execute(
    'DELETE FROM clientes WHERE id=:id',
    {'id': 2}
)

# Selecioção minuciosa
cursor.execute(
    'SELECT nome, peso FROM clientes WHERE peso>:peso',
    {'peso': 50}
)


# Boa prática de programação
cursor.close()
conexao.close()

"""
