import sqlite3 as sql

# TODO tratar erros possíveis pois o webframe não está tratando

class BD:
    database = "/home/mathuebra/VSCode/Python/SQLPython/TP_BD/db"
    conn = None
    cursor = None
    connected = False
    
    def connect(self):
        BD.conn = sql.connect(BD.database)
        BD.cursor = BD.conn.cursor()
        BD.connected = True
        
    def disconnect(self):
        BD.conn.close()
        BD.connected = False
        
    def execute(self, sql, parms=None):
        if BD.connected:
            if parms is None:
                BD.cursor.execute(sql)
            else:
                BD.cursor.execute(sql, parms)
            return True
        else:
            return False
        
    def fetchall(self):
        return BD.cursor.fetchall()
    
    def persist(self):
        if BD.connected:
            BD.conn.commit()
            return True
        else:
            return False
        
    def insert(self, table, columns, values):
        placeholders = ', '.join(['?'] * len(values))
        columns_str = ', '.join(columns)
        sqlquery = f"INSERT INTO {table} ({columns_str}) VALUES ({placeholders})"

        self.connect()
        self.execute(sqlquery, values)
        self.persist()
        self.disconnect()
        
    # columns vai ser uma lista de strings e values uma lista de valores respectiva a cada column
    def update(self, table, columns, values, condition):
        place_holders = ", ".join([f"{col} = ?" for col in columns])
        sqlquery = f"UPDATE {table} SET {place_holders} WHERE {condition}"
        
        self.connect()
        self.execute(sqlquery, values)
        self.persist()
        self.disconnect()
        
    def delete(self, table, condition):
        sqlquery = f"DELETE FROM {table} WHERE {condition}"
        
        self.connect()
        self.execute(sqlquery)
        self.persist()
        self.disconnect()
        
    def select(self, table, columns, condition, params=()):
        columns = ", ".join(columns)
        sqlquery = f"SELECT {columns} FROM {table} WHERE {condition}"
        
        self.connect()
        self.execute(sqlquery, params)
        result = self.fetchall()
        self.disconnect()
        return result

        
    def execute_unique(self, sql):
        self.connect()
        self.execute(sql)
        self.persist()
        self.disconnect()
        
    def verify_login(self, email, senha):
        return self.select("USUARIO", "*", f"EMAIL = ? AND SENHA = ?", [email, senha])
    
    def create_user(self, nome, email, senha, data):
        status = None
        self.insert("USUARIO", ["NOME", "STATUS", "DATA_NASCIMENTO", "EMAIL", "SENHA"], [nome, status, data, email, senha])
        

# Exemplo de uso da classe BD
# #database.create("users", ["NOME VARCHAR(50)", "EMAIL VARCHAR(50)", "SENHA VARCHAR(50)"])
# database.insert("users", ["Matheus", "mathuebra@gmail.com", "123e456"])
# database.insert("users", ["Letícia", "leticinha@gmail.com", "123e456"])
# database.execute_unique("INSERT INTO users VALUES ('Laura', 'laura@gmail.com', '123e456')")
# database.execute_unique("INSERT INTO users VALUES ('Caio', 'caio@gmail.com', '123e456')")
# # database.execute_unique("DROP TABLE users")
# database.delete("users", "NOME = 'Laura'")