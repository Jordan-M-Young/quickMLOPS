from quickmlops.templates import scikit_learn
import os

path = scikit_learn.__path__[0]
print(path)

train = f'{path}/train.py'
print(train)