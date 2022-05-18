import random
import time
import copy


def generate_mas(n=50, min_limit=-1000, max_limit=1000):
    mas = []
    mas_index = [i for i in range(n)]
    for i in range(n):
        mas.append(random.randint(min_limit, max_limit))
    return mas, mas_index


def sort(mas, mas_index):
    mas_sort = mas.copy()
    for i in range(1, len(mas_sort)):
        item_to_insert = mas_sort[i]
        index_to_insert = mas_index[i]
        j = i - 1
        while j >= 0 and mas_sort[j] > item_to_insert:
            mas_sort[j + 1] = mas_sort[j]
            mas_index[j + 1] = mas_index[j]
            j -= 1
        mas_sort[j + 1] = item_to_insert
        mas_index[j + 1] = index_to_insert
    return mas_sort


def bin_poisk(mas, mas_index, key):
    first = 0
    last = len(mas) - 1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first + last) // 2
        if mas[mid] == key:
            index = mid
        else:
            if key < mas[mid]:
                last = mid - 1
            else:
                first = mid + 1
    if index == -1:
        print("Введенный элемент отсутствует в сгенерированном массиве")
    else:
        print("Введенный элемент находится в сгенерированном массиве под индексом", mas_index[index])


def insert(mas):
    print("Нужно ли вставить элемент? ")
    ans = input()
    if ans == "да" or ans == "Да" or ans == "Lf" or ans == "lf":
        el = int(input("Введите число: "))
        index = int(input("Введите его индекс: "))
        mas.insert(index, el)
        mas_index.insert(index, index)
        for i in range(len(mas_index) - 1, (len(mas_index) - index), -1):
            mas_index[i] += 1
        print(mas)


def delete(mas):
    print("Нужно ли удалить элемент? ")
    ans = input()
    if ans == "да" or ans == "Да" or ans == "Lf" or ans == "lf":
        index = int(input("Введите его индекс: "))
        del mas[index]
        for i in range(len(mas_index) - 1, index - 1, -1):
            mas_index[i] -= 1
        del mas_index[index]
        print(mas)


def fibonacci(lys, mas_index, val):
    flag = False
    fibM_minus_2 = 0
    fibM_minus_1 = 1
    fibM = fibM_minus_1 + fibM_minus_2
    while (fibM < len(lys)):
        fibM_minus_2 = fibM_minus_1
        fibM_minus_1 = fibM
        fibM = fibM_minus_1 + fibM_minus_2
    index = -1
    while (fibM > 1):
        i = min(index + fibM_minus_2, (len(lys) - 1))
        if (lys[i] < val):
            fibM = fibM_minus_1
            fibM_minus_1 = fibM_minus_2
            fibM_minus_2 = fibM - fibM_minus_1
            index = i
        elif (lys[i] > val):
            fibM = fibM_minus_2
            fibM_minus_1 = fibM_minus_1 - fibM_minus_2
            fibM_minus_2 = fibM - fibM_minus_1
        else:
            answ = i
            flag = True
            break
    if (fibM_minus_1 and index < (len(lys) - 1) and lys[index + 1] == val):
        answ = index + 1
        flag = True
    if not flag:
        answ = -1
    if answ == -1:
        print("Введенный элемент отсутствует в сгенерированном массиве")
    if answ != -1:
        print("Введенный элемент находится в сгенерированном массиве под индексом", mas_index[answ])


def interpolation(lys, mas_index, val):
    low = 0
    high = (len(lys) - 1)
    answ = -1
    while low <= high and val >= lys[low] and val <= lys[high]:
        index = low + int(((float(high - low) / (lys[high] - lys[low])) * (val - lys[low])))
        if lys[index] == val:
            answ = index
        if lys[index] < val:
            low = index + 1
        else:
            high = index - 1
    if answ == -1:
        print("Введенный элемент отсутствует в сгенерированном массиве")
    else:
        print("Введенный элемент находится в сгенерированном массиве под индексом", mas_index[answ])


class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def findval(self, lkpval):
        if lkpval < self.data:
            if self.left is None:
                print(lkpval, "не найден.")
                return False
            return self.left.findval(lkpval)
        elif lkpval > self.data:
            if self.right is None:
                print(lkpval, "не найден.")
                return False
            return self.right.findval(lkpval)
        else:
            print(self.data, ' найден.')
            return True

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()


def make_a_tree(arr):
    root = Node(arr[0])
    for i in arr[1::]:
        root.insert(i)
    return root


n = int(input("Введите количество элементов массива: "))
min_limit = int(input("Укажите начальный диапозон чисел для генерации: "))
max_limit = int(input("Укажите конечный диапозон чисел для генерации: "))
mas, mas_index = generate_mas(n, min_limit, max_limit)
print("Сгененированный массив: ")
print(mas)

mas_index_sort = mas_index.copy()
mas_sort = sort(mas, mas_index_sort)
print("Отсортированный массив: ")
print(mas_sort)

print("Бинарный поиск")
print(mas)
print("Введите элемент, который хотите найти: ")
key = int(input())
start_time_bin = time.time()
bin_poisk(mas_sort, mas_index_sort, key)
end_time_bin = time.time() - start_time_bin
insert(mas)
delete(mas)

print("Интерполяционный поиск")
print(mas)
print("Введите элемент, который хотите найти: ")
key = int(input())
mas_index_inter = mas_index.copy()
mas_inter = sort(mas, mas_index_inter)
start_time_inter = time.time()
interpolation(mas_inter, mas_index_inter, key)
end_time_inter = time.time() - start_time_inter
insert(mas)
delete(mas)

print("Фибоначчиев поиск")
print(mas)
print("Введите элемент, который хотите найти: ")
key = int(input())
mas_index_fib = mas_index.copy()
mas_fib = sort(mas, mas_index_fib)
start_time_fib = time.time()
fibonacci(mas_fib, mas_index_fib, key)
end_time_fib = time.time() - start_time_fib
insert(mas)
delete(mas)

print("Бинарное дерево")
mas_tree = copy.deepcopy(mas)
root = make_a_tree(mas_tree)
num = int(input("Введите элемент, который хотите найти: "))
start_time_tree = time.time()
result = root.findval(num)
end_time_tree = time.time() - start_time_tree
ans = input("Хотите внести элемент? ")
if ans == "да" or ans == "Да" or ans == "Lf" or ans == "lf":
    num = int(input("Введите элемент, который хотите внести: "))
    root.insert(num)
    root.PrintTree()
answ = input("Хотите удалить элемент? ")
if ans == "да" or ans == "Да" or ans == "Lf" or ans == "lf":
    num = int(input("Введите элемент, который хотите удалить: "))
    mas_tree.remove(num)
    root = make_a_tree(mas_tree)
    root.PrintTree()
