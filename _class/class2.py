# range()  zip()


# ['a','b','c','d'] 用zip首尾相接
for im in zip([1, 2, 3], [4, 5, 6]):
    print(im)

# 序列分类
# 可变：【1,2,3】、{1,2,3}、{6:6,3:3}
# 有序：【3,3,3】、{3,3,3}

# 列表
l = list()
l = [1, 2, 3]
l.append([6, 6, 6])  # l增加1个
l.extend([6, 6, 6])
# l.insert(0,100)#慎用
print(l)

# 查
print(l.index([6, 6, 6]))

print(l.count(6))  # 次数

# 改
l[0] = 'aaa'

# 删
# l.remove(6)
# print(l)


# l.pop()
# l.clear()
# print(l)


# 其他成员函数
# l.__new=l.copy()


#序列接包


key=['a','b','c','d']
value =[97,98,99]

for k ,v in zip(key,value):
    print(k,v)

[*(1,2,3)]
{'x':102,**{'y':103}}#函数参数传递

#无序----字典
#key-value可变序列 ，key ：不可变
x=100
d={x:'tony'}
x=1
print(d)
d={}
d= dict(zip(key,value))
#d= dict(name='tony',age=40)

#查
# print(d['e)
print(d.get('e',[]))
print(d.items())
print(d.keys())
print(d.values())

#增加与改
d['e']=100
# d.update({})


#删除
del  d['e']
# d.clear()
d.pop('a',[])#不存在返回[]
# d.popitem()#任意删除一个

# 有序字典
import  collections
od = collections.OrderedDict()


# 字典推导式
keys = ['a','b','c']
values=[97,98,99]
d_new = {i:j for i,j in zip(keys,values)}   #序列解包

# 集合----无序可变序列
s=set()
s={1,2,3}
# 集合存放不可变类型（可以哈希）：数字，字符串，元组  s{[1,2,3],4} 错误不能为列表
# 1.曾
s.add(100)

#2. 删
s.remove(100)
s.pop()
s.clear()


# 集合运算
# 交集，并集，差集，对称差集
s1={1,2,3,4}
s2 = {3,2,4,5}
s_new = s1 | s2# 并集
s_new = s1 & s2 #交集
s_new = s1 - s2 #差集 s1.difference(s2)
s_new = s1 ^ s2 #对称差集

# 集合推导式
s={x.strip() for x in ('he','she', ','  ,   ',')}

#1.应用
# from random import randint
# data = {
#     'user '+ str:{'film'+str(1,10) for i in randint(1,15)}  for i in range(10)
#    }#

user={'file1','file2','file3'}

# ta最爱电影---兴趣接近
# 推荐ta看过但是user没看


#2.应用:过滤重复无效评论




# 规则;重复字符串超过50%，无效

# def rules():
#     filter(,comments)

#3.应用: 实现优先级队列，入队列，出队列，取队首
# 堆排序



import copy
# copy.deepcopy()

import random
n=[random.randint(1,100) for x in range(10)]

print(n)
sorted(n)
print(n)
n.sort()  # 原地址修改
print(n)

# 循环轻量
#n = [random.randint(1, 100) for x in range[10]]

# [express
# for expre in seql if cond
# for expre in seq2 if cond2


boys = ['chris', 'arnold', 'bob']
girls = ['ace', 'clar', 'bhh']
bg = [b + '+' + g for b in boys
for g in girls if b[0] == g[0]]
print(bg)

letter = {}
for i in girls:
    letter.setdefault(i[0],[]).append(i)
bg = {b+''+g for b in  boys for g in letter[b[0]]}


# import os
# print(os.listdir())
# files = [filename for filename in os.listdir('.')
#          if filename.endswith('.py','.pjw')]



#元组

t=tuple()
t=()
t= tuple(l)



#del 切片
#切片----有序序列
#【start:end:step]   [start :end)左毕右开

l=[x for x in range(10)]
print(l[2:8:4])
print(l[-1:2:-1])#倒着取 start >= end &&step<0

#l[len(l):]=[6,7,8]#追加
# del l[1:4:2]

l[::2]=[0]*(int(len(l)/2))
print(l)































