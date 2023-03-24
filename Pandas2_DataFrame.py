import os
import numpy as np
import pandas as pd

path_with_files = os.path.join(os.getcwd(), 'Excel_files', 'tips.csv')
df = pd.read_csv(path_with_files)
df.info()
# Названия колонок
df.columns
# Названия индексов
df.index
# Посмотрим первые строки
df.head()
# Посмотрим последние строки
df.tail()
# Характеристики
df.describe()
# отдельная колонка - объект Series
df['total_bill']
# пара колонок выделяем
my_cols = ['total_bill', 'tip']
df[my_cols]
# пара колонок выделяем (2 способ)
df[['total_bill', 'tip']]
# Добавляем новую колонку (обязательно с новым названием)
df['tip_percentage'] = 100 * df['tip'] / df['total_bill']
df.head()
df['tip_percentage'] = np.round(100 * df['tip'] / df['total_bill'], 2)
df.head()
# Пробуем удалить колонку, только что созданную
df = df.drop('tip_percentage', axis=1)
df.shape
# Установим колонку Payment ID вместо индекса (для удобства)...обязательно делаем изменения через df = df...
df = df.set_index('Payment ID')
# Сбросим индекс
df = df.reset_index()
# Установим колонку Payment ID вместо индекса
df = df.set_index('Payment ID')
# Выберем первую строку
df.iloc[0]
# Выберем первую строку по индексу
df.loc['Sun2959']
# Выберем строки
df.iloc[0:4]
# Выберем строки по индексу
df.loc[['Sun2959', 'Sun5260']]
# Удаляем строки по индексу
df = df.drop('Sun2959', axis=0)
# Добавляем строку
one_row = df.iloc[0]
df.append(one_row)
# Фильтруем по условию
df[df['total_bill'] > 20]
# Фильтруем по нескольким условиям '''AND -> &''' или '''OR -> |'''
df[(df['total_bill'] > 30) & (df['sex'] == 'Male')]
# еще один вариант фильтрации
options = ['Fri', 'Sat', 'Sun']
df[df['day'].isin(options)]