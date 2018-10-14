s="hello world".split(' ')[0]#取hello第一位
print(s)

#第三次开始


#数值类型
print(888)
print(0X10,0o10,0B01)
print(555.555)
print(66+66j)#负数      print(type(66+666j))    (运算符重载，函数重载)

#字符串
"hello world"
'fgs'
"""fgsm"""

print("%d%c"%(65,66))
print("%2.5f"%3.1415926)

#序列
#[6,6,6]#list 可以变
#(6,6,2)#tuple 元组，不变
#{6,6,6}#set
s={6,6,6}
print(len(s))#s的长度为1,3个都是6

#{6:6,6:6}#字典

print(None)
print(True,False)

#f=fun()

#变量

x= "hello world"
print(type(x))#返回变量类型

x = 3
m=x ** 2
print(m)

y=x
x=[1,2,3]
print(id(y)== id(x[2]))  #基于值的管理机制

x[1]=5#修改元素值
y=x
print(y,x)



#del y
#运算符与表达式
a=3+4
s="hello"+"world"
l=[1,2,3]+[4,5,6]

c=(3+4j)+(4+2j)
print(c)

m=[1,2,3] *3
print(m)

print(3>2>1)
#3>2 and 2>1
#3>2 or 3>1

#"hello" > "hel"#字符串比较
#[1,2,3] < [1,2,3,4]#子集

#in   is

print(3 in [3,4,5])

for i in range(10):
    print(i, end = ' ')#迭代 随机



x=[1,2]
y=[1,2]
if x is y:
    print(True)



#第四次开始

#[1,2,3] & [4,5,6]#交集
#[1,2,3] | [4,5,6]#并集
#[1,2,3] - [4,5,6]#差集
#[1,2,3] ^ [4,5,6]#对称差集


x,y = 3,5
print(type(x))

print(++3, --5)



#常用内置函数
for i in range(5):#(start,end) 或者for i in range(15):
    print(i, end= ' ')

x=['aaa','bc','d','b','ba']
x_new=sorted(x, key=lambda item:(len(item),item),reverse=True)
print(x_new)


ite=list( reversed(x) )  #倒序
print(ite)
for i in reversed(x):
    print(i,end=' ')


import copy
z=copy.deepcopy(x)#深拷贝
print(z)


#基本输入输出
#x= input("请输入")
#print(x)

#x,y = map(int, input("请输入：").split(','))
#print(x,y)

#模块导入与使用

import  math
print(math.sin(20))

from  copy import  *
from random import  *
m=randint(0,12)
print(m)

import  sys
#print(sys.path)


#t,q,b=map(int, input())

#print(t,q,b)



































































