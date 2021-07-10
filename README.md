Tensorflow 2.0 Repository는 제가 책으로 공부하는 Tensorflow 2.0의 실습예제를 정리해서 올리는 Repository입니다.

1일차
실습파일 이름 : activation funtion, PredictiongHousePrices 
딥러닝에서 매번 사용되는 활성화함수가 어떤 공식으로 이루어져있고 함수의 선이 어떻게 그려지는 확인을 하기위해 함수로 활성화 함수를 설정하고
그 설정한 함수를 matplotlib를 사용하여 어떻게 그려지는지 확인했습니다
Tensorflow안에 있는 Bosten집값 데이터를 활용하여 집안에 방이 몇개 있는지를 설정하여 방이 몇개면 어느정도 가격인지 예측을 하는 프로그램을 만들었습니다.

2일차
실습파일 이름 : Binary Classification
이항분류를 실습하기 위해서 Tensorflow에 내장되어 있는 와인데이터를 불러와서 산도 알코올 도수 밀도 등 여러가지 기준으로 레드와인과 화이트와인을 분류하는 이항분류를 실습하였습니다.
공부를 하면서 정확도와 오차율을 나타내는 엔트로피에 대해서도 같이 공부했습니다.

3일차
실습파일 이름 : Fashion MNIST데이터 분류모델
이미지를 분류하는법을 실습하기 위해서 Tensorflow에 내장되어 있는 Fashion MNIST데이터를 불러와서 먼저 어떤 이미지 데이터가 있는지 확인하고 이미지를 x데이터로 넣고
y데이터에 라벨링 되어있는 데이터를 넣어 이미지를 분류하는 모델을 만들어봤습니다. 

4일차
실습파일 이름 : Fashion MINST데이터 분류 컨볼루션 신경망
Convolution Neural Network에 Convolution layer(특징추출)을 실습하기 위해서 전에 썻던 Fashion MNIST데이터를 불러와 Convolution layer(특징추출 레이어)를 추가한 Model을 만들고 학습시켜
3일차때 했던 분류를 하는 모델을 만들어 봤습니다.

5일차
실습파일 이름 : Convolution
Convolution이 어떻게 돌아가는지 또 Convolution의 필터는 어떻게 되어있는지를 확인하기 위해서 커널을 구현해보고 커널을 거쳤을때 어떻게 사진이 나오는지 확인해봤습니다.

6일차
실습파일 이름 : Fashion MINST데이터 분류 컨볼루션 신경망
Maxpooling과 Dropout에 대해서 공부를 하고 이전에 했던 Convolution Neural Network(CNN)에 공부를 했던 Maxpooling과 Dropout 레이어를 추가한 모델을 만들어봤습니다.

7일차
실습파일 이름 : Fashion MINST데이터 분류 컨볼루션 신경망
Maxpooling과 Dropout을 추가한 모델을 VGGNet 스타일로 바꾸고 데이터 양을 늘리는 이미지 보강기법을 공부하고 직접 이미지 보강기법을 사용한 모델로 바꿨습니다.

8일차
실습파일 이름 : AutoEncoder
AutoEncoder가 어떤 방법인지 Encoder는 뭐고 Decoder는 무엇을 하는건지 그리고 Encoder, Decoder가 어떻게 작용되는지를 학습했습니다 
AutoEncoder내용을 실제로 tensorflow에 있는 MNIST데이터 세트에 적용을 하면서 AutoEncoder에 대해서 공부했습니다.

9일차
실습파일 이름 : AutoEncoder
K평균 클러스터링을 공부하고 K평균 클러스터링을 저번에 했었던 AutoEncoder파일로 Decoder된 이미지를 사용하여 분류가 잘되는지 실습해봤습니다.

10일차
실습파일 이름 : AutoEncoder
저번에 K평균 클러스터링을 했었는데 K평균 클러스터링을 하고 그결과를 쉽게 보기위해 T-SNE을 활용하여 그래프로 보기 쉽게 나타내는 실습을 해봤습니다.

11일차
실습파일 이름 : Super Resolution
사이즈가 큰 이미지를 줄이게 될 경우는 별 차이가 없지만 사이즈가 적은 이미지를 크기를 키우면 일부 픽셀이 깨지는 현상이 일어나는데 이를 자연스럽게 해결하는 네트워크인 REDNet에 대해서 학습하고 이것을 실제로 모델을 만들어 구현을 해보는 실습을 해봤습니다
데이터파일은 BSD500와 Set5을 사용했습니다.

12일차
실습파일 이름 image segmentation
저번에 했던 저해상도로 파일을 다시 고해상도로 바꾸는 REDNet을 응용해서 이미지의 의미에 따라서 분류하는 네트워크를 만들어보는 실습을 해봤습니다.

13일차
실습파일 이름 image segmentation
앞에서 했던 파일에는 REDNet을 사용했는데 학습속도가 느리고, context 인식과 localization 간의 trade-off를 해결했다는 장점이 있는 U-Net으로 바꿔보는 실습을 하였습니다.(개인)

14일차
실습파일 이름 gym
강화 학습에 대해서 공부를 하고 책에 있는 내용을 실습해보는 시간을 해봤습니다 MountainCar -v0환경을 불러오고 에이전트는 해옹으로 환경에 영향을 줌 Box2D를 사용한 간단한 물리 조작계, 아타리(Atari)게임, 로봇 시뮬레이션을 실습해봤습니다.
