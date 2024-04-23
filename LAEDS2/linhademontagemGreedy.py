def assembly_greedy(e1, e2, x1, x2, a1, a2, t1, t2, n):
    line1_time = [0] * n
    line2_time = [0] * n

    line1_path = [0] * n
    line2_path = [0] * n

    # Inicialização dos tempos para as estações iniciais
    line1_time[0] = e1 + a1[0]
    line2_time[0] = e2 + a2[0]

    # Percorre as estações de montagem para calcular os tempos mínimos
    for j in range(1, n):
        # Linha 1
        time1 = min(line1_time[j - 1] + a1[j], line2_time[j - 1] + t2[j - 1] + a1[j])
        if time1 == line1_time[j - 1] + a1[j]:
            line1_path[j] = 1
        else:
            line1_path[j] = 2
        line1_time[j] = time1

        # Linha 2
        time2 = min(line2_time[j - 1] + a2[j], line1_time[j - 1] + t1[j - 1] + a2[j])
        if time2 == line2_time[j - 1] + a2[j]:
            line2_path[j] = 2
        else:
            line2_path[j] = 1
        line2_time[j] = time2

    # Escolhe a melhor linha para a estação final
    if line1_time[n - 1] + x1 <= line2_time[n - 1] + x2:
        final_line = 1
    else:
        final_line = 2

    # Caminho ótimo 
    optimal_path = [final_line]
    for j in range(n - 1, 0, -1):
        if final_line == 1:
            final_line = line1_path[j]
        else:
            final_line = line2_path[j]
        optimal_path.insert(0, final_line)

    return min(line1_time[n - 1] + x1, line2_time[n - 1] + x2), optimal_path

# A atividade considera 'e' e 'x' como os primeiros e últimos elementos de 'a', aqui houve preferência pela
# separação dos elementos para ficar melhor a visualização e entendimento do programa

#e1 = 3
#e2 = 2
#x1 = 6
#x2 = 5
#a1 = [5, 7, 10, 5, 9, 11, 9, 5, 2]
#a2 = [6, 3, 9, 11, 4, 9, 3, 12, 4]
#t1 = [3, 5, 4, 2, 7, 5, 8, 1]
#t2 = [5, 3, 7, 5, 6, 2, 5, 2]

e1 = 5
e2 = 7
x1 = 8
x2 = 9
a1 = [10, 6, 3, 8, 5, 3, 7, 12]
a2 = [3, 5, 3, 7, 6, 4, 9, 10]
t1 = [4, 2, 7, 2, 5, 8, 2]
t2 = [6, 1, 7, 3, 6, 4, 5]


n = len(a1)
result, path = assembly_greedy(e1, e2, x1, x2, a1, a2, t1, t2, n)

print("Tempo mínimo:", result)
print("Caminho ótimo:", path)
