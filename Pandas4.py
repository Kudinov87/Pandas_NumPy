import os
import numpy as np
import pandas as pd

path_with_files = os.path.join(os.getcwd(), 'Excel_files')
df = pd.read_csv(path_with_files + '\\movie_scores.csv')
df.head()
# Отсутствующие значения
np.nan
pd.NA
# вот так можно сравнивать такие числа
np.nan is np.nan
# есть ли значения nan в датафрейме: функция notnull() или notna()
df[df['pre_movie_score'].notnull()]
# удаляем строки со значением nan
df.dropna()
# удаляем все колонки (если есть значения nan)
df.dropna(axis=1)
# удаляем только выбранные колонки (если есть значения nan)
df.dropna(subset=['last_name'])
# Заменяем значения nan на 'Новое значение'
df.fillna('Новое значение')
# Сбрасываем индекс в датафрейме
df = df.reset_index()
df = df.drop('index', axis=1)
# Укажем заново индекс
df.index = range(len(df))