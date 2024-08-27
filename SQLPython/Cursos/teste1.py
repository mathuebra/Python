import sqlite3
import pandas as pd

series_obj = pd.Series([1,7,9,13,17,99])
series_obj

series_obj2 = pd.Series([4,7,8,-2], index = ['alfa', 'beta', 'teta', 'gama'])
series_obj2

disciplinas = {'cursos' : ['Estatística', 'Economia', 'Cálculo', 'Geometria'],
               'créditos' : [90, 60, 90, 40],
               'requisito' : [True, False, True, False]}

data = pd.DataFrame(disciplinas)
print(data)

connection = sqlite3.connect("/home/mathuebra/Cursos/PythonEstruturaDeDados/agenda/agenda.db")

cursor = connection.cursor()

cursor.execute("CREATE TABLE contato(nome,endereco,telefone)")
