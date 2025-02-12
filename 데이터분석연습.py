import pandas as pd
import numpy as np

midwest = pd.read_csv('midwest.csv')
midwest.head()
midwest.tail()
midwest.shape
midwest.info()
midwest.describe()

midwest = midwest.rename(columns = {'poptotal':'total'})
midwest = midwest.rename(columns={'popasian':'asian'})

midwest['ratio'] = midwest['asian']/midwest['total']*100
midwest['ratio'].plot.hist()

midwest['ratio'].mean()
midwest['group'] = np.where(midwest['ratio'] > 0.4872, 'large', 'small')

midwest['group'].value_counts().plot.bar(rot=0)
