from random import randint

data = {
    'user' + str(i): {'film' + str(randint(1, 30)) for i in range(1, 12)} for i in range(10)
}

# print(data)
user = {'film2', 'film3', 'film5', 'film8', 'film11', 'film13', 'film14'}
x =[]
for vaule in data.values():
    m = vaule.difference(user)
    # print(m)
    u = list(m)
    if u not in x:
        s=x+u
        k=set(s)
        # print(x)

print(k)

data = {'user' + str(i): {'film' + str(randint(1, 15)) for i in range(10)} for i in range(10)}
user = {'film1', 'film2', 'film3'}

userName,flims=max(data.items(),key= lambda item : len(item[1]&user))
print(userName)
print(flims-user)



# u = {'file' + str(i): 'user3' for i in range(5)}
# c = set(u)
# print(c)
#
# print(u)
#
# user = {'film1', 'film2', 'film3'}
# user2 = {'film2', 'film5', 'film8'}
# sd = user.intersection(user2)
# print(sd)
#
# print(user)

# s={x.strip() for x in ('ae','she', 'ta'  ,  'wo')}
# print(s)

# a = [1, 2, 5, 6, 9]
# b = [1, 2, 8, 9, 7, 4, 3]
# c = [1, 5, 9, 3, 6, 8]
# qs = [i for i in a if i in b and i in c]
# print(qs)
#
# vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for v in vec:
#     print(v)
#     for num in v:
#         print(num)

# ac = [3, 5, 7, 9, 11]
# var = ac[1:3:]
# print(var)
#
# a=[1,2,3]
# b,c,d=a
# print(c)
#
#
# x = {'age':25,'name':'ssss','sex':'male'}
# x['score']=[97,98]
# for z in x.values():
#    print(z)
# x.pop('name')
# # x.pop('sex')
# print(x)
