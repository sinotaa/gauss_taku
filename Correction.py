#ここにコードを書いて送る
import math
import matplotlib.pyplot as plt
import numpy as np


x=np.linspace(-5,5,100)
#平均０分散１の標準偏差を関数として用意する。
def y(a):
  return (np.exp(-(a)**2 / 2))/np.sqrt(2*math.pi)

#この際注意点としてyもnumpyの関数で処理しておかないとerrorが出る点に注意
plt.plot(x,y(x))

n=int(input())
'''
listは積分した面積の数値を求めた面積ごとに記憶していくリストで、リストの番号は
0~n-1個であり各時点の数値はlistに保存される。
'''
list=[0]*n
result=0

#この点における理解は自分で行い説明できるようにしてください
for i in range(n):
  if i==0:
    result=(y(x[i])+y(x[i]+0.1))*0.1/2
    list[i]=result
  else:
    result=list[i-1]+(y(x[i])+y(x[i]+0.1))*0.1/2
    list[i]=result

#print(x)
print(list)
plt.plot(x,list)
plt.show()


#以上で添削を終わります。必要に応じて連絡・質問を受け付けます。