import sqlite3 as sql

class Database:
    database = "/home/mathuebra/VSCode/Python/SQLPython/TP_BD/db"
    conn = None
    cursor = None
    connected = False
    
    def connect(self):
        Database.conn = sql.connect(Database.database)
        Database.cursor = Database.conn.cursor()
        Database.connected = True
        
    def disconnect(self):
        Database.conn.close()
        Database.connected = False
        
    def execute(self, sql):
        self.connect()
        self.cursor.execute(sql)
        self.disconnect()
        
    def persist(self):
        if Database.connected:
            Database.conn.commit()
            return True
        else:
            return False
        
    def fetchall(self):
        return Database.cursor.fetchall()
    
    def select(self, sqlquery):
        self.connect()
        self.cursor.execute(sqlquery)
        result = self.fetchall()
        self.disconnect()
        
        return result
    
    def insert(self, sqlquery):
        
        
    