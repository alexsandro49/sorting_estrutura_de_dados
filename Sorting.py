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

def Heapify(array:list, n:int, index:int):
        maior = index
        l = 2 * index + 1
        r = 2 * index + 2

        if l < n and array[maior] < array[l]:
            maior = l

        if r < n and array[maior] < array[r]:
            maior = r

        if maior != index:
            array[maior], array[index] = array[index], array[maior]
            Heapify(array,n,maior)

def heap_sort(array:list):
    N = len(array)

    #Constroi Heap Máximo
    for i in range(N//2 - 1, -1, -1):
        Heapify(array, N, i)

    for i in range(N-1, 0, -1):
        #substitui ultimo elemento com o começo da array, reoganiza a array e repete
        array[i], array[0] = array[0], array[i]
        Heapify(array, i, 0)

    