import pandas as pd
import numpy as np

base = pd.read_csv('iris.csv')
# print(base)
print('Base Geral: ', base.shape)

np.random.seed(2345)

amostra = np.random.choice(a=[0, 1], size=150, replace=True, p=[0.7, 0.3])

# print(amostra)

#print(amostra[amostra == 1])

base_final = base.loc[amostra == 0]
base_final2 = base.loc[amostra == 1]
print('Base Final (0): ', base_final.shape)
print('Base Final (1): ', base_final2.shape)
