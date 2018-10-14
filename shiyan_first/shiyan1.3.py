from heapq import heappush, heappop

class PriorityQueue:
    def __init__(self):
        self._queue = []

    def put(self, item, priority):
        heappush(self._queue, (-priority, item))

    def get(self):
        return heappop(self._queue)[-1]


q = PriorityQueue()
q.put('world', 1)
q.put('hello', 2)
print(q.get())
print(q.get())











# from random import randint
#
# data = {'user' + str(i): {'film' + str(randint(1, 15)) for i in range(10)} for i in range(10)}
# user = {'film1', 'film2', 'film3'}
#
# userName,flims=max(data.items(),key= lambda item : len(item[1]&user))
# print(userName)
# print(flims-user)