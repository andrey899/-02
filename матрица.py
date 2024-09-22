def get_matrix(n, m, Value):
    matrix = []                       # создайте пустой список matrix внутри функции get_matrix
    for i in range(n):                # напишите первый(внешний) цикл for для кол-ва строк матрицы n
        matrix.append([])          # в первом цикле добовляйте пустой список в список matrix


        for j in range(m):                # напишите второй(внешний) цикл for для кол-ва столбов матрицы m
            matrix[i].append(Value)       # во втором цикле пополняйте ранее добавленный пустой список значениями Value
    return matrix



result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)

print(result1)
print(result2)
print(result3)


