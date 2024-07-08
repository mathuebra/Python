import gspread
from google.oauth2.service_account import Credentials
import pandas as pd

# Define as credenciais
scope = ['https://spreadsheets.google.com/feeds', 
         'https://www.googleapis.com/auth/drive']
creds = Credentials.from_service_account_file('credentials.json', scopes=scope)

# Autentica e abre a planilha
client = gspread.authorize(creds)
sheet = client.open('Horários')

# Lista de abas que você deseja processar
abas = ['Normal', 'Cópia Normal']

# Dicionário para armazenar DataFrames
dataframes = {}

# Processa cada aba
for aba in abas:
    # Seleciona a aba
    worksheet = sheet.worksheet(aba)
    
    # Obtém todos os valores da aba como uma lista de listas
    data = worksheet.get_all_values()
    
    # Cria um DataFrame do Pandas com os dados
    df = pd.DataFrame(data[1:], columns=data[0])  # Assume que a primeira linha contém os nomes das colunas
    
    # Armazena o DataFrame no dicionário
    dataframes[aba] = df

# Agora você pode acessar os DataFrames individualmente pelo nome da aba
print(dataframes['Normal'])
print(dataframes['Cópia Normal'])
