# 로지스틱 회귀 : 입력값을 0과 1사이의 확률로 변환하는 시스모이드 함수를 사용해서 .
# 머신 러닝과 통계학에서 자주 사용되는 분류 알고리즘 (이진분류에 많이 사용)
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler # 데이터를 표준화 하기 위해
from sympy.stats import Logistic

# 1.데이터 불러오기
fish = pd.read_csv('http://bit.ly/fish_csv_data')
# 2. 입력(X)과 타겟(Y)
fish_input = fish[['Weight','Length','Diagonal','Height',"Width"]].to_numpy()
fish_target = fish['Species'].to_numpy() # 타깃인 물고기의 종류

# 3. 학습 데이터와 테스트 데이터를 분할
train_input, test_input, train_target, test_target = train_test_split(fish_input, fish_target, random_state=42)

# 데이터 표준화 (평균 0, 표준 편차 1로 변환)
ss = StandardScaler()
ss.fit(train_input)
train_scaled = ss.transform(train_input)
test_scaled = ss.transform(test_input)

# 5. k-최근접 이웃 (k-NN)분류기
kn = KNeighborsClassifier(n_neighbors=3)
kn.fit(train_scaled, train_target)

# k-NN 모델 성능 확인
print("===== k-NN 모델 성능 =====")
print(f"훈련 세트 정확도 : {kn.score(train_scaled,train_target)}")
print(f"테스트 세트 정확도 : {kn.score(test_scaled,test_target)}")
print(f"테스트 데이터 예측 결과 : {kn.predict(test_scaled[:5])}")
print(f"각 클래스의 확률 예측 : {kn.predict_proba(test_scaled[:5])}" )

# 6. 로지스틱 회귀 (이진 분류 : Bream vs Smelt)
bream_smelt_indexes = (train_target == 'Bream') | (train_target == 'Smelt')
train_bream_smelt = train_scaled[bream_smelt_indexes]
target_bream_smelt = train_target[bream_smelt_indexes]
lr_binary = LogisticRegression()
lr_binary.fit(train_bream_smelt, target_bream_smelt)


# 로지스틱 회귀 (이진 분류) 성능
print("\n\n===== 로지스틱 회귀(이진 분류) 성능 =====")
print(f"이진 분류 예측 결과 : {lr_binary.predict(train_bream_smelt[:5])}")
print(f"이진 분류 확률 예측 : {lr_binary.predict_proba(train_bream_smelt[:5])}")
print(f"이진 분류 계수(기울기) : {lr_binary.coef_}")
print(f"이진 분류 절편 : {lr_binary.intercept_}")

# 7. 로지스틱 회귀 (다중 분류 : 7개의 물고기 중 선택 )
lr_multi = LogisticRegression(C=20,max_iter=1000)
lr_multi.fit(train_scaled, train_target)

# 로지스틱 회귀 다중 분류 성능
print(f"\n\n===== 로지스틱 회귀(다중 분류) 성능 =====")
print(f"훈련세트 정확도 : {lr_multi.score(train_scaled,train_target)}")
print(f"테스트 세트 정확도 : {lr_multi.score(test_scaled, test_target)}")
print(f"테스트 데이터 예측 결과  :{lr_multi.predict(test_scaled[:5])}")
print(f"다중 클래스 확률 예측 : {lr_multi.predict_proba(test_scaled[:5])}")