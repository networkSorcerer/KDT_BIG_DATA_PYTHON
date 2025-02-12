from cProfile import label

import matplotlib.pyplot as plt # 데이터 시각화에서 가장 많이 사용되는 라이브러리 pyplot 모듈 import

# plt.plot([10,20,30,40]) # y축 데이터 ( 수직 방향 ), x  축 값을 지정하지 않으면 0에서 시작하는 값으로 자동 생성
# plt.show()

# plt.plot([10,20,30,40,50,60,70],[12,43,25,15,10,10,0]) # x 축, y 축
# plt.show()

# 그래프 옵션 추가하기
plt.rc("font", family='Malgun Gothic')
plt.title("제목 추가하기")

# 범례 추가하기
plt.plot([10,20,30,40],color='blue',label="X축")
plt.plot([40,30,20,10],color='pink', label="Y축")
plt.legend()
plt.show()

