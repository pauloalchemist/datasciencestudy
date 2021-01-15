import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

iris = pd.read_csv('iris.csv')
print(iris['species'].value_counts(), '\n')

x, _, y, _ = train_test_split(iris.iloc[:, 0:4], iris.iloc[:, 4],
                              test_size=0.5, stratify=iris.iloc[:, 4])
print(y.value_counts())
