def swap(a, b):
    return b, a

def binary_search(nums, k):
    n_op = 0
    
    l = 0
    r = len(nums) - 1
    while (l < r):
        m = int((l + r) / 2)
        print(f'Left {l}, M {m}, Right {r}')
        if (nums[m] < k):
            l = m + 1
        else:
            r = m
        n_op += 1

    print(f'Number operations: {n_op}')
    if (nums[r] == k):
        return r
    return -1

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j] :
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print(arr)
        
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = swap(arr[j], arr[j + 1])

def quick_sort(l, r, a):
    print(f'Begin of sort {a}')
    i = l
    j = r
    x = a[int((i + j)/ 2)]
    
    print(f'Left {l}, Right {r}, Middle {int((i + j)/ 2)}, arr {a[l:r + 1]}')
    while i <= j:
        while (a[i] < x):
            i += 1
        while (a[j] > x):
            j -= 1
        if (i <= j):
            a[i], a[j] = swap(a[i], a[j])
            i += 1
            j -= 1
    if (i < r):
        quick_sort(i, r, a)
    if (j > l):
        quick_sort(l, j, a)
    print(f'Result of sort {a}\n')
    
import operator
def merge(left, right, compare):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

def merge_sort(L, compare=operator.lt):
    print('Array in merge_sort:', L)
    if len(L) < 2:
        return L[:]
    else:
        middle = int(len(L) / 2)
        left = merge_sort(L[:middle], compare)
        print('Array after left merge_sort', left, end='\n\n')
        right = merge_sort(L[middle:], compare)
        print('Array after right merge_sort', right, end='\n\n')
        return merge(left, right, compare)
    
def radix_sort(arr):
    
    # находим размер самого длинного числа
    max_digits = max([len(str(x)) for x in arr])

    # основание системы счисления
    base = 10

    # создаём промежуточный пустой массив из 10 элементов
    bins = [[] for _ in range(base)]

    # перебираем все разряды, начиная с нулевого
    print(f'Max digits {max_digits}')
    for i in range(0, max_digits):
        # для удобства выводим текущий номер разряда, с которым будем работать
        print('!!! Номер разряда → ' + str(i))
        # перебираем все элементы в массиве
        for x in arr:
            # получаем цифру, стоящую на текущем разряде в каждом числе массива
            digit = (x // base ** i) % base
            # отправляем число в промежуточный массив в ячейку, которая совпадает со значением этой цифры 
            bins[digit].append(x)
        # собираем в исходный массив все ненулевые значения из промежуточного массива
        arr = [x for queue in bins for x in queue]
        # текущее состояние массива
        print('Исходный массив', arr)
        # текущее состояние промежуточного массива
        print('Промежуточный массив', bins)

        # очищаем промежуточный массив
        bins = [[] for _ in range(base)]

    # возвращаем отсортированный массив
    return arr

def bucketSort(a):
    max_v = max(a)
    min_v = min(a)
    
    buckets = [0 for _ in range(max_v - min_v + 1)]
    print(f'Max {max_v}, Min {min_v}, Buckets len {len(buckets)}')
    for i in range(len(a)):
        buckets[a[i] - min_v] += 1
    i = 0
    print('Buckets result', {min_v + k: v for k, v in enumerate(buckets)})
    for j in range(len(buckets)):
        for k in range(buckets[j]):
            a[i] = j
            i += 1