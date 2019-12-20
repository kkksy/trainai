from xxx import*
import numpy as np # 수학 연산 수행을 위한 모듈
import pandas as pd # 데이터 처리를 위한 모듈
import seaborn as sns # 데이터 시각화 모듈
import matplotlib.pyplot as plt # 데이터 시각화 모듈

traindata = read("train.csv")

traindata.drop('holiday', axis=1, inplace=True)


print(traindata)

myhist(traindata) # 각 데이터를 막대차트 형태로 볼 수 있다.

myviolinplot(traindata, 'weather', 'count') # 각 날씨별 자전거렌탈수

heatmap(traindata)

