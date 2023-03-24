import os
import numpy as np
import pandas as pd

path_with_files = os.path.join(os.getcwd(), 'Excel_files', 'tips.csv')
df = pd.read_csv(path_with_files)


def last_four(num):
    return str(num)[-4:]


def yelp(price):
    if price < 10:
        return '$'
    elif price >= 10 and price < 30:
        return '$$'
    else:
        return '$$$'

# Применяем метод apply (запуск функции)
df['Expensive'] = df['total_bill'].apply(yelp)

# Применяем метод apply (запуск функции)
df['last_four'] = df['CC Number'].apply(last_four)
df.head()
df['total_bill'].mean()
df['total_bill'].apply(lambda num: num*2)
# Сортировка по колонке
df.sort_values('tip')

# Найдем индекс строки с минимальным значением
df['total_bill'].idxmin()
# Корреляция
df.corr()
# Уникальные значения в колонке
df['day'].unique()
# Уникальные значения в колонке - количество
df['day'].nunique()
# Уникальные значения - количество каждого значения
df['day'].value_counts()
# Заменяем значения в колонке
df['sex'].replace('Female', 'F')
# Проверяем, есть ли дубликаты
df.duplicated()
# Удаляем дубликаты
df.drop_duplicates()
# Проверка в диапазоне значений
df['total_bill'].between(10, 20, inclusive=True)