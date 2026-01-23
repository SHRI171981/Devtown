import pandas as pd
import numpy as np

data=np.random.randn(10,3)
df=pd.DataFrame(data,columns=['col1','col2','col3'])
df=df.head()
print(f'First 5 rows:\n{df}\n')

cov=df['col2'].cov(df['col3'])
print(f'Covariance of col2 and col3:\n{cov}\n')
print(f'Covariance of entire df:\n{df.cov()}\n')

corr=df['col2'].corr(df['col3'])
print(f'Correlation of col2 and col3:\n{corr}\n')
print(f'Correlation of entire df:\n{df.corr()}\n{df}')
