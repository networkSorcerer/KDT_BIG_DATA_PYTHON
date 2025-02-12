import pandas as pd
import matplotlib.pyplot as plt

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

mgr_new = mpg.copy()
mgr_new = mgr_new.rename(columns={'cty':'city'})
mgr_new = mgr_new.rename(columns={'hwy':'highway'})
print(mgr_new.head())

df = pd.DataFrame({
    'var1' : [4,3,8],
    'var2' : [2,6,1]
})
df['var_sum'] = df['var1'] + df['var2']
print(df)

df['var_mean'] = (df['var1']+df['var2'])/2
print(df)


import matplotlib.pyplot as plt

# 예시로 mpg 데이터 불러오기 (파일을 실제로 로드하려면 파일 경로를 지정해야 함)
# mpg = pd.read_csv('mpg.csv')

# 여기서 mpg가 이미 존재한다고 가정하고 진행합니다.

# 1. 'total' 열 계산
mpg['total'] = (mpg['cty'] + mpg['hwy']) / 2

# 2. 결과 출력
print("첫 5개의 데이터 (head):")
print(mpg.head())  # 'total' 열을 포함한 첫 5개의 데이터 출력

# 3. 평균 계산 (두 방법)
print("\n두 가지 방법으로 평균 계산:")
print("sum / len 방법:", sum(mpg['total']) / len(mpg))  # sum / len 방법
print("mean() 방법:", mpg['total'].mean())  # mean() 내장 함수

# 4. 기술 통계량 (describe)
print("\n'시스템 통계량 (describe)' 출력:")
print(mpg['total'].describe())  # 기술 통계량

# 5. 히스토그램 플로팅
print("\n'히스토그램' 출력:")
mpg['total'].plot.hist(rwidth=0.8, bins=20)
plt.title('Histogram of Total')
plt.xlabel('Total')
plt.ylabel('Frequency')
plt.show()

import numpy as np

mpg['test'] = np.where(mpg['total'] >= 20, 'pass', 'fail')
print(mpg.head())

print(mpg['test'].value_counts())

count_test = mpg['test'].value_counts()
count_test.plot.bar()
plt.show()

count_test.plot.bar(rot=0)

mpg['grade'] = np.where(mpg['total'] >= 30, 'A',
np.where(mpg['total'] >= 20 , 'B', 'C'))
print(mpg.head())

df = mpg['grade']
df = df.value_counts()
df = df.sort_index()

# 또는 한 줄로
df = mpg['grade'].value_counts().sort_index()
print(df)

mpg['size'] = np.where((mpg['category']=='compact') |
                       (mpg['category'] == 'subcompact') |
                       (mpg['category'] == '2seater'),
                       'small', 'large')
mpg['size'].value_counts()

mpg['size'] = np.where(mpg['category'].isin(['compact','subcompact','2seater']), 'small', 'large')
mpg['size'].value_counts()
