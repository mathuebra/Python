import pandas as pd

Autor = ['Sun Tzu', 'Fernando Pessoa', 'Thomas Mann', 'João Guimarães Rosa']
Livro = ['A Arte da Guerra', 'Poesias Selecionadas', 'A Montanha Mágica', 'Primeiras Estórias']
Ano = [2000, 2004, 2015, 2017]

dados = {
    'Autor':Autor,
    'Livro':Livro,
    'Ano':Ano
}

autores = pd.DataFrame(dados)

df = autores


print(autores.index)