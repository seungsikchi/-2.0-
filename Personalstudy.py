import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras

#직선 가설 h = wx + b
#직선의 모양을 변경하는 요소는 w,b,이다
#w와 b가 주어졌을 때 특정 도매인 x값에 대한 y값을 구할 수 있다.

#완전한 직선데이터
x = [1, 2, 3, 4, 5] #데이터 정의
y = [0.5, 0.9, 1.3, 1.7, 2.1]#집 값


def linearMondel(w, b, x): 
  return w*x+b

#직선에서 y값 얻어내기
def getLinerSample(w, b):
  x_domain = x
  y_range = [] # 빈 리스트로 초기화
  
  #도매인 개수와 동일한 개수를 가지는 y 샘플을 직선의 방정식으로 생성
  for i in x_domain:
    y_sample = linearMondel(w, b, i)
    y_range.append(y_sample)

  return x_domain, y_range


#오차 함수를 사용하여 실제 데이터와 그 트렌드를 나타내는 직선과의 차이를 구함
def getCost(w, b, xSet, ySet):
  sampleN = len(xSet)
  errorSum = 0

  for i in range(sampleN):
    errorSum += abs(ySet[i] - linearMondel(w, b, xSet[i])) #오차 모두 더하기

  averageError = errorSum / sampleN #오차평균
  return averageError

plt.plot(x, y , 'ko')

#직선모델의 파라메터

w = 0.4
b = 0.1

samples = getLinerSample(w,b)
totalcost = getCost(w, b, x, y)
print("오차", totalcost)

plt.plot(samples[0], samples[1], 'b-')
plt.show()

print(linearMondel(w,b, 460))

def house_model(y_new):
  xs = np.array([1, 2, 3, 4, 5, 6], dtype=float)
  ys = np.array([0.5, 0.9, 1.3, 1.7, 2.1, 2.5], dtype=float)

  model = keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
  model.compile(optimizer='sgd', loss = 'mean_squared_error')
  model.fit(xs, ys, epochs=1000)
  return model.predict(y_new)[0]


prediction = house_model([12,0])
print("방 12개이면 집값은", prediction,"입니다.")