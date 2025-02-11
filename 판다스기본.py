import pandas as pd
import numpy as np

# 데이터 생성 (수학 열에 결측치 추가)
data = {
    '이름': ['민지', '하니', '해린', '해린', '혜인', '다니엘'],
    '수학': [90, 80, 70, 60, np.nan, np.nan],  # 수학 열에 결측치 추가
    '영어': [98, 100, np.nan, 89, 99, np.nan]  # 영어 열에도 결측치 추가
}

# 데이터프레임 생성
df = pd.DataFrame(data)
print("\nDataFrame:")
print(df)

# 데이터프레임 정보 확인
print("\n데이터프레임 정보:")
print(df.info())  # 데이터 타입 및 결측치 확인
print("\n데이터프레임 요약 통계:")
print(df.describe())  # 수치형 데이터 요약 및 통계 제공

# 그룹화 및 집계
# 반별 수학, 과학, 영어 평균 점수 구하기
class_avg = df.groupby('반')[['수학','영어','국어']].mean()
print(f"반별 평균 : {class_avg}")

class_avg2 = df.groupby('반').agg({'수학':'mean','영어':'mean','국어':'mean'})
print(f"반별 평균 : {class_avg2}")

# 1. 각 반별 수학과 영어 평균을 동시 출력하기
# 2. 각 반별 수학 점수의 최대값과 최소값 구하기
# 3. 과일의 가격 평균과 판매량 평균을 구해 보세요




