#字符编码  ASCII
# unicode
# GBK
b ='abc'.encode(encoding='GBK')  #bytes
s= b.decode(encoding='GBK')

# 字符串常用方法
#格式化字符串
"%x"%666

# format
print("{0},{0:#o},{1:#x}".format(66,6666))
t="{name},{age}".format(name='lc',age='fg')
print(t)



# 查找
# s.find() s.rfind()#找不到不抛异常返回-1
# s.index()  s.rindex()#找不到抛异常
# s.count()
s="apple,peach,banana,pear,peach"
print(s.find('peach,0,100'))
# print(s.rindex('peach,9,100'))



# 字符串分割
# s.split()  s.rsplit()
# s.partition() s.rpartition()
s='2018-10-10'
print(s.split('-',2))
print(s.rpartition('-'))
# 无参数按空白字符切割，但参数不能为空字符


# 字符串拼接
# s1+s2#效率低
# s.join(iter)#iter必须为字符串

l="apple,peach,banana,pear,peach".split(' ')
print(','.join(l))


# 字符串替换
# s.replace(src,dst)
words = ('测试','暴力','非法','话')
text='这句话有非法内容'
for word in words:
    if word in text:
        text = text.replace(word,'**')

print(text)

# 字符串加密与解密
# table = s.maketrans()
# s.translate(table)




import string
before = string.ascii_letters
lower =  string.ascii_lowercaseser
upper = string.ascii_uppercase
k=int(input())
after = lower[k:]+lower[:k]+upper[k:]+upper[:k]

table= ''.maketrans(before,after)
s = input()

print(before)


print(s.translate(table))