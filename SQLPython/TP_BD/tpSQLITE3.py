import sqlite3

class DataBase:
    def __init__(self, connection_name):
        self.connection = sqlite3.connect(connection_name)
        self.cursor = self.connection.cursor()
        
    def insere_dados_tabela(self, nome_tabela, dados):
        self.cursor.execute(f"INSERT INTO {nome_tabela} VALUES {dados}")
        self.connection.commit()
        
    def remove_dados_tabela(self, nome_tabela, condicao):
        self.cursor.execute(f"DELETE FROM {nome_tabela} WHERE {condicao}")
        self.connection.commit()
        
    def atualiza_dados_tabela(self, nome_tabela, dados, condicao):
        self.cursor.execute(f"UPDATE {nome_tabela} SET {dados} WHERE {condicao}")
        self.connection.commit()
        
    def consulta_dados_tabela(self, nome_tabela, campos, condicao):
        self.cursor.execute(f"SELECT {campos} FROM {nome_tabela} WHERE {condicao}")
        return self.cursor.fetchall()
    
    def fecha_conexao(self):
        self.connection.close()

db = DataBase('my_database.db')
db.insere_dados_tabela('my_table', ('value1', 'value2'))
db.fecha_conexao()
