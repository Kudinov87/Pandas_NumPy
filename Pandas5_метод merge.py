import os
import numpy as np
import pandas as pd

registrations = pd.DataFrame({'reg_id':[1,2,3,4],'name':['Andrew','Bobo','Claire','David']})
logins = pd.DataFrame({'log_id':[1,2,3,4],'name':['Xavier','Andrew','Yolanda','Bobo']})

help(pd.merge)

pd.merge(registrations,logins,how='inner',on='name')

# Используем функции для работы с текстом (как с обычным текстом, помимо метода apply)
names = pd.Series(['andrew','bobo','claire','david','4'])
names.str.capitalize()
names.str.isdigit()

messy_names = pd.Series(["andrew  ","bo;bo","  claire  "])
messy_names.str.replace(";","").str.strip().str.capitalize()

def cleanup(name):
    name = name.replace(";","")
    name = name.strip()
    name = name.capitalize()
    return name

messy_names.apply(cleanup)