# 케라스 사용법

딥러닝 프로그램은 다음과 같은 단계를 거쳐 사용한다.

1. 필요 Package import
2. 데이터셋 생성(학습, 테스트)
3. 모델 생성(TF 그래프 생성)
4. 학습 알고리즘 지정
5. 학습
6. 학습된 모델 평가
7. 학습된 모델 사용하여 예측



모델 is Tensorflow Graph

데이터는 최소 3000개 있어야함





### 2.0 기본 세팅

``` python
import sys
import tensorflow as tf

print('Tensorflow:', tf.__version__)
print('Python:', sys.version)

!pip uninstall tensorflow -y
!pip uninstall tensorflow-gpu -y
!pip install tensorflow-gpu==2.0.0-rc1 -y
```



