def merge_sort(x):
    # Verifica se a lista tem mais de um elemento
    if len(x) > 1:
        middle = len(x) // 2
        middle_lt = x[:middle]
        middle_rt = x[middle:]

        # Ordena cada uma das sublistas
        merge_sort(middle_lt)
        merge_sort(middle_rt)

        # Combina as sublistas ordenadas em uma lista ordenada
        pos_lt = 0
        pos_rt = 0
        pos_new = 0
        while pos_lt < len(middle_lt) and pos_rt < len(middle_rt):
            if middle_lt[pos_lt] < middle_rt[pos_rt]:
                x[pos_new] = middle_lt[pos_lt]
                pos_lt += 1
            else:
                x[pos_new] = middle_rt[pos_rt]
                pos_rt += 1
            pos_new += 1

        while pos_lt < len(middle_lt):
            x[pos_new] = middle_lt[pos_lt]
            pos_lt += 1
            pos_new += 1

        while pos_rt < len(middle_rt):
            x[pos_new] = middle_rt[pos_rt]
            pos_rt += 1
            pos_new += 1
