def merge_sort(x):
    if len(x) > 1:
        middle = len(x) // 2
        middle_lt = x[:middle]
        middle_rt = x[middle:]

        merge_sort(middle_lt)
        merge_sort(middle_rt)

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
            
def quick_sort(x, beginning=0, end=None):
    def partition(x, beginning, end):
        pi = x[end]
        i = beginning
        for k in range(beginning, end):
            if x [k] <= pi:
                x[k], x[i] = x[i], x[k]
                i = i + 1
        x[i], x[end] = x[end], x[i]
        return i

    if end is None:
        end = len(x)-1

    if beginning < end:
        p = partition(x, beginning, end)
        quick_sort(x, beginning, p-1)
        quick_sort(x, p+1, end)

def heap_sort(array:list):
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

    n = len(array)

    for i in range(n//2 - 1, -1, -1):
        Heapify(array, n, i)

    for i in range(n-1, 0, -1):
        array[i], array[0] = array[0], array[i]
        Heapify(array, i, 0)

