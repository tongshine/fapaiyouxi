# 1.检查是否在页面源代码里面
#     如果在，直接requests.get()
#     如果不在，则异步加载，看抓包工具（network→XHR）
import random
i=0
sum=[]

x=["J", "Q","K"]
while i<10:
    i=i+1
    x.append(i)
#给每张牌配上花色
for it in x:
    str= "♥{}".format(it)
    sum.append(str)
    str= "♣{}".format(it)
    sum.append(str)
    str= "♠{}".format(it)
    sum.append(str)
    str= "♦{}".format(it)
    sum.append(str)
#加上双王
sum.append("King")
sum.append("Queen")
# print(sum)
random.shuffle(sum)
print("玩家A:{}".format(sum[0:17]))
print("玩家B:{}".format(sum[17:34]))
print("玩家C:{}".format(sum[34:53]))