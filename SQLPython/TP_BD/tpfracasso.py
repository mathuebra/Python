import sqlite3

connection = sqlite3.connect('test.db')

cursor = connection.cursor()

#cursor.execute('''CREATE TABLE ALUNO (
#    id int PRIMARY KEY,
#    nome VARCHAR(50),
#    data_nascimento DATE,
#    nota int 
#    )
#''')

#cursor.execute('''INSERT INTO ALUNO VALUES (1, 'Matheus', '09/06/2003', 10)''')
#cursor.execute('''INSERT INTO ALUNO VALUES (2, 'Letícia', '31/07/2002', 11)''')

cursor.execute('SELECT * FROM ALUNO')
rows = cursor.fetchall()

for row in rows:
    print(row)

connection.close()