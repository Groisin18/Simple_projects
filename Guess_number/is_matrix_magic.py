def is_matrix_magic(N):
    """
    Возвращает True, если матрица N является магическим квадратомб и False, если не является.\n
    Магическим квадратом порядка n называется квадратная таблица размера n×n,\n 
    составленная из всех чисел 1, 2, 3... n^2 так, что\n
    суммы по каждому столбцу, каждой строке и каждой из двух диагоналей равны между собой.
    """
    n = len(N)
    if n != len(N[0]):
        return False   # Проверяем, что матрица квадратная
    P = []
    for i in N:
        P.extend(i)
    P.sort()
    if P[0] != 1:
        return False    # Проверяем, что матрица содержит числа от 1 
    for i in range(1, len(P)):
        if P[i] - P[i-1] != 1:
            return False    # Проверяем, что матрица содержит числа от 1 до n^2
    sum_st, sum_str, sum_gl_d, sum_pb_d = [0] * n, [0] * n, 0, 0
    for i in range(n):
        sum_str[i] = sum(N[i])    # Считаем сумму строк
        sum_gl_d += N[i][i]    # Считаем сумму главной диагонали
        for j in range(n):
            sum_st[j] += N[i][j]    # Считаем сумму столбцов
            if j == n - i - 1:
                sum_pb_d += N[i][j]    # Считаем сумму побочной диагонали
    count_sum = sum_st + sum_str
    count_sum.append(sum_gl_d)
    count_sum.append(sum_pb_d)
    if count_sum.count(count_sum[0]) != len(count_sum):
        return False    # Проверяем равность сумм столбцов, строк, диагоналей
    return True

n, N = int(input()), []
for i in range(n):
    N.append([int(j) for j in input().split()])
if is_matrix_magic(N):
    print("YES")
else:
    print("NO")