def assembly(e1, e2, x1, x2, a1, a2, t1, t2, n):
    memo = {} # Vetor memorizador

    # Tempo para percorrer a linha de montagem até a estação 'j'
    def min_time(line, j):
        if j == 0:
            if line == 1:
                return e1 + a1[0] 
            else: 
                return e2 + a2[0]

        # Parte do código que utiliza a memorização do vetor 'memo'
        if (line, j) in memo:
            return memo[(line, j)]

        if line == 1:
            time = min(min_time(1, j-1) + a1[j], min_time(2, j-1) + t2[j-1] + a1[j])
        else:
            time = min(min_time(2, j-1) + a2[j], min_time(1, j-1) + t1[j-1] + a2[j])

        memo[(line, j)] = time
        return time

    # Constrói o caminho ótimo para a linha de montagem até a estação 'j'
    def assembly_line(line, j):
        if j == 0:
            return [line]

        prev_line = None
        if line == 1:
            if min_time(1, j-1) + a1[j] <= min_time(2, j-1) + t2[j-1] + a1[j]:
                prev_line = 1
            else: 
                prev_line = 2
        else:
            if min_time(2, j-1) + a2[j] <= min_time(1, j-1) + t1[j-1] + a2[j]:
                prev_line = 2  
            else:
                prev_line = 1

        # Chamada recursiva da função para construção do caminho ótimo
        return assembly_line(prev_line, j-1) + [line]

    f1 = min_time(1, n-1) + x1
    f2 = min_time(2, n-1) + x2

    if f1 <= f2:
        return f1, assembly_line(1, n-1)
    else:
        return f2, assembly_line(2, n-1)


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
result, path = assembly(e1, e2, x1, x2, a1, a2, t1, t2, n)

print("Tempo mínimo:", result)
print("Caminho ótimo:", path)
