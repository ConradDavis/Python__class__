# 选择语句

# 1..
# if condition:
#     statements

# condition 惰性求值且不能赋值运算

# 2..
# if condition:
#     statements
# else:
#     statements

# exp1 ? exp2 :exp3 c语言
# value1

# if condition1:
#     statements

# else if condition2:
#     statements

# else if condition3:
#     statements

# python 没有switch case
switch = {
    'a': lambda x: x ** 2,
    'b': lambda x: x ** 3,
    'c': lambda x: x ** x
}

print(switch['b'](2))

# 判断闰年----今天是今年第几天
import time

year, month, day = time.localtime()[:3]

# not(year %400) or (not (year%4)and year %100)
day_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if not (year % 400) or (not (year % 4) and year % 100):
    day_month[1] = 29
if month == 1:
    print(day)
else:
    print(sum(day_month[:month - 1]) + day)  # 切片，左闭右开从0开始

import calendar

if calendar.isleap(year):
    day[1] = 29


# 循环
# 1.. while ----非计数循环
# while condition1:
#     statements

# else:        #while不成立时执行
#     statements

# 2..
# for ----计数循环
# for values in iter/seq
#     statements


# break continue

# 练习1  : 一个包含若干数字的序列A，以列表为例
# 满足0<=a<b<=n的A[b]-A[a]最大值（交集）
import random
A=[random.randint(10,99) for i in range(10)]
print(A)
minVal= A[0]
diff=-float('inf')
for idx,val in enumerate(A[1:]):
    if val < minVal:
        minVal=val
    else:
        t= val-minVal
        r=(idx+1,minVal,val)
        diff=t#更新最大值
print(r)




# 练习2;每天固定的时间自动完成一定事情
# 动态规划
def doSth():
    print('test')

import datetime

def main(h=0,m=0):
    while True:
        now= datetime.datetime.now()
        if now.minute==m and now.hour==h:
            doSth()
        else:
            time.sleep(20)#秒

import threading
t=threading.Thread()
t.start()
# t.setDaemon()





















