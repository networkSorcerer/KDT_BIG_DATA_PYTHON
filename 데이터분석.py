import pandas as pd
exam =pd.read_csv('exam.csv')
print(exam.head())
print(exam.tail())
print(exam.shape)
print(exam.info())
print(exam.describe())
pd.DataFrame({'x':[1,2,3]})

mpg = pd.read_csv('mpg.csv')

df_raw = pd.DataFrame({
    'var1' : [1,2,3],
    'var2' : [2,3,2]
})
print(df_raw)

df_new = df_raw.copy()
df_new = df_new.rename(columns={'var2' : 'v2'})
print(df_new)

df = pd.DataFrame({
    'var1' : [4,3,8],
    'var2' : [2,6,1]
})
df['var_sum'] = df['var1'] + df['var2']
print(df)