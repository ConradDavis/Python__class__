# a = ['sss', 'sss', 'dd', 'dd', 'f']
# a_1 = ""
# for i in a:
#     if i not in a_1:
#         a_1 += i
# m = list(a_1)
# print(a_1)
# print(m)
#
# for n in range(100, 1, -1):
#     for i in range(2, n):
#         if n % 2 == 0:
#             break
#         else:
#             print(n)
#             break
#
# li='ddddertyuihgtfffffgggggttt'
#
#
# print(li.count('d'))
#
# s = {'a':1, 'b':2, 'c':3}
# b, c, d = s.items()
# print(b)
#
# b, c, d = s
# print(c)

import random
import string
ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
# print(ran_str)



sy = {'key'+str(i):[''.join(random.sample(string.ascii_letters + string.digits,4)) for i in range(4)] for i in range(6)}

print(sy)
comments = ['这是一本非常好的书，作者用心了',
            '作者大大辛苦了',
            '好书，感谢作者提供了这么多的好案例',
            '书在运输的路上破损了，我好悲伤。。。',
            '为啥我买的书上有菜汤。。。。',
            '啊啊啊啊啊啊',
            '书的质量有问题啊，怎么会开胶呢？？？？？？',
            '好好好好好好好好好好好',
            '好难啊看不懂好难啊看不懂好难啊看不懂',
            '书的内容很充实',
            '你的书上好多代码啊，不过想想也是，编程的书嘛，肯定代码多一些',
            '书很不错!!一级棒!!买书就上当当，正版，价格又实惠，让人放心!!! ',
            '无意中来到你小铺就淘到心意的宝贝，心情不错! ',
            '送给朋友的、很不错',
            '这是一本好书，讲解内容深入浅出又清晰明了，推荐给所有喜欢阅读的朋友同好们。']

r=lambda c :len(set(c))/len(c)> 0.5
print(list(filter(r,comments)))




