# Массивы NumPy
import numpy as np

# Создаем массивы на основе списков (1-мерный)
my_list = [1, 2, 3]
my_arr = np.array(my_list)
print(my_arr)
print(type(my_arr))

# Создаем массивы на основе списков (2-мерный)
my_matr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
my_matrix = np.array(my_matr)
print(my_matrix)
print(type(my_matrix))

# Создаем массивы через функцию arange
np.arange(0, 10, 2)
"""
arange([start,] stop[, step,], dtype=None, *, like=None)

    Return evenly spaced values within a given interval.
    
    Examples
    --------
    >>> np.arange(3)
    array([0, 1, 2])
    >>> np.arange(3.0)
    array([ 0.,  1.,  2.])
    >>> np.arange(3,7)
    array([3, 4, 5, 6])
    >>> np.arange(3,7,2)
    array([3, 5])
"""

# Создаем массивы из нулей (1-мерный)
np.zeros(5)
# Создаем массивы из нулей (2-мерный)
np.zeros((3, 5))
# Создаем массивы из единиц (2-мерный)
np.ones((4, 4))

# Создаем массив при помощи linspace от 0 до 10 включительно, равноотстоящие друг от друга
np.linspace(0, 10, 11)
len(np.linspace(0, 10, 11))

# Создаем единичную матрицу
np.eye(5)

# Создаем массив с равномерным распределением при помощи rand (числа от о до 1)
np.random.rand(2)
# Создаем массив с равномерным распределением при помощи rand (5 строк и 2 колонки)
np.random.rand(5, 2)
# Создаем массив с нормальным распределением (распределение Гаусса)
np.random.randn(5)

# Создаем массив из случайных целых чисел от 0 до 100, 5 чисел
np.random.randint(0, 101, 5)

np.random.seed(42)

# Примерчик
arr = np.arange(0, 25)
# переделаем массив в матрицу размером 5 на 5
arr.reshape(5, 5)

# Рассмотрим популярные функции для работы с numpy
ranarr = np.random.randint(0, 101, 10)
# максимальное
ranarr.max()
# минимальное
ranarr.min()
# индекс максимального числа
ranarr.argmax()
# индекс минимального числа
ranarr.argmin()
# атрибут массива shape - размер
ranarr.shape

# Рассмотрим функции broadcast - операция для каждого элемента массива
print(ranarr)
ranarr[1:5] = 100
print(ranarr)

# сделаем срез массива
arr = np.arange(0, 11)
slice_of_arr = arr[0:3]

slice_of_arr[:] = 99

arr_copy = arr.copy() # Копируем массив через функцию np.copy()

arr_2d = np.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])
# первая строка из матрицы
arr_2d[0]
# извлекаем конкретное значение, например 25
arr_2d[1][1]
# получаем 2 первые строки
arr_2d[:2]
# получаем числа 10,15,25,30
arr_2d[:2, 1:]

arr = np.arange(1, 11)
arr > 4
bool_array = arr > 4
# массив с числами больше 4
arr[bool_array]

# Операции в NumPy
arr = np.arange(0,10)
# прибавили к каждому элементу 5
arr + 5
np.sqrt(arr)
np.sin(arr)
np.log(arr)

arr.sum()
arr.mean()
arr.max()
arr.var()
arr.std()

arr = np.arange(0, 25)
arr_2d = arr.reshape(5, 5)
arr_2d.sum(axis=0) # сумма по колонкам
arr_2d.sum(axis=1) # сумма по строкам

print('Работа завершена.')