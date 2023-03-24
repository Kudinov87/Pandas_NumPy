import numpy as np
import pandas as pd

my_index = ['USA', 'Canada', 'Mexico']
my_data = [1085, 3421, 5659]
# Создаем объект Series стандартным способом
my_series = pd.Series(data=my_data, index=my_index)
print(my_series[0])
print(my_series['USA'])

# Создаем объекты Series из словарей (именованный индекс получится)
q1 = {'Japan': 80, 'China': 450, 'India': 200, 'USA': 250}
q2 = {'Brazil': 100, 'China': 500, 'India': 210, 'USA': 260}

sales_q1 = pd.Series(q1)
sales_q2 = pd.Series(q2)

sales_q1['Japan']  # пользоваться именованными индексами очень удобно
sales_q1.keys()
sales_q1 / 100
sales_q1 + sales_q2
sales_q1.add(sales_q2, fill_value=0)
sales_q1.dtype