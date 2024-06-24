import pyautogui
import pyperclip
import time
import re

# IMPORTANTÍSSIMO: LEIA AS INSTRUÇÕES COM CUIDADO 

# O código deve ser executado enquanto já aberto na área de busca
# Com o campo de escrita em branco
# A partir dai é só executar e escrever o número que você quer procurar
# Simples assim

def buscar_patentes(search_number):
    # Definição de coordenadas

    # Aba onde escreve o numero de cpf/cnpj
    search_field_x = 950
    search_field_y = 490

    # Botão de pesquisa
    search_button_x = 630
    search_button_y = 565

    # Onde está as opções para selecionar cpf/cnpj
    search_type_x = 1200
    search_type_y = search_field_y

    # Opção correta para buscar por cpf/cnpj
    search_correct_x = search_type_x
    search_correct_y = 565

    # Clica na posição (x, y) e escreve um texto
    def click_and_write(x, y, text):
        pyautogui.click(button='left', x=x, y=y)
        pyautogui.write(text)

    # Clica na posição (x, y)
    def click_button(x, y):
        pyautogui.click(button='left', x=x, y=y)

    # Realiza a busca, com intervalos de 0.5s para garantir funcionalidade

    click_and_write(search_field_x, search_field_y, search_number)
    time.sleep(0.5)

    click_button(search_type_x, search_type_y)
    click_button(search_correct_x, search_correct_y)
    time.sleep(0.5)

    click_button(search_button_x, search_button_y)
    time.sleep(3) # Tempo de espera maior para garantir que a página mudou

    patentes = []

    while True:
       # Define a 'área' que ele vai copiar
       initial_drag_x = 580
       initial_drag_y = 380
       final_drag_x = 1390
       final_drag_y = 800

       pyautogui.moveTo(x=initial_drag_x, y=initial_drag_y)
       pyautogui.mouseDown(button='left')
       pyautogui.moveTo(x=final_drag_x, y=final_drag_y, duration=0.5)
       pyautogui.mouseUp(button='left')
       pyautogui.hotkey('ctrl', 'c')

       text = pyperclip.paste()

       # Define os números que ele vai encontrar com padrão no regex 
       # Explicação:
       # BR seguido de 1 ou mais espaços, seguido de captura de grupos de dígitos separados por 1 ou mais espaços
       regex_patente = r'BR\s+(\d+\s+\d+\s+\d+\s+\d+)' 
       novas_patentes = re.findall(regex_patente, text)
       patentes.extend(novas_patentes)

       # Se ele encontrar a palavra "Próxima", significa que tem mais páginas para buscar
       if 'Próxima' in text:
            # Coordenadas do botão
            proxima_x = 615
            proxima_y = 775
            click_button(proxima_x, proxima_y)
            time.sleep(3)  # Espera um pouco para carregar a próxima página
       else:
            break

    return patentes

# Exemplo de uso:
search_number = input("Digite o número a ser pesquisado: ")
patentes_encontradas = buscar_patentes(search_number)
print("Patentes encontradas:")
for patente in patentes_encontradas:
     print(patente)