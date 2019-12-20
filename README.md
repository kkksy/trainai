<H1>Bike Sharing Demand </H1> 캐글의 2년간 자전거 임대 데이터를 이용해 날씨별 자전거 임대수요 예측해보기

<HR>

<H2>데이터 출처</H2>
https://www.kaggle.com/c/bike-sharing-demand
->2년에 걸친 시간별 임대데이터
  
<HR>
  
<H2>데이터 읽기/정제</H2>
<pre><code>traindata = read("train.csv") # 데이터 읽기
traindata.drop('holiday', axis=1, inplace=True) #필요없는 데이터 없애고 적용</code></pre>

![데이터](./이미지/데이터.png)
