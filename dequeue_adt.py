# Deque Implementation
# len(D)    number of elements
# D.appendleft( )   add to beginning
# D.append( )   add to end
# D.popleft( )  remove from beginning
# D.pop()   remove from end
# D.first( )    D[0]    access first element
# D.last( ) D[−1]   access last element
# D.clear( )    clear all contents

class DequeEmpty(Exception):

    def __str__(self):
        return "Deque Empty"


class MyDeque:

    def __init__(self):
        self._CAPACITY = 6
        self._data = [None] * self._CAPACITY
        self._front = 0
        self._length = 0

    def __len__(self):
        return self._length

    def first(self):
        return self._data[self._front]

    def last(self):
        return self._data[(self._front + self._length - 1) % self._CAPACITY]

    def append_left(self, val):
        if self._length == self._CAPACITY:
            self._resize(self._CAPACITY * 2)

        if self._length == 0:
            self._data[0] = val
            self._front = 0
            self._length = 1
        else:
            new_place = (self._front - 1) % self._CAPACITY
            self._data[new_place] = val
            self._front = new_place
            self._length += 1

    def pop_left(self):
        if self._length == 0:
            raise DequeEmpty()

        if self._length <= self._CAPACITY // 4:
            self._resize(self._CAPACITY // 2)

        val = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % self._CAPACITY
        self._length -= 1
        return val

    def pop(self):
        if self._length == 0:
            raise DequeEmpty()

        if self._length < self._CAPACITY // 4:
            self._resize(self._CAPACITY // 2)

        new_place = (self._front + self._length) % self._CAPACITY - 1
        val = self._data[new_place]
        self._data[new_place] = None
        self._length -= 1
        return val

    def append(self, val):
        if self._length == self._CAPACITY:
            self._resize(self._CAPACITY * 2)

        if self._length == 0:
            self._data[0] = val
            self._front = 0
            self._length = 1
        else:
            new_place = (self._front + self._length) % self._CAPACITY
            self._data[new_place] = val
            self._length += 1

    def clear(self):
        self._CAPACITY = 6
        self._data = [None] * self._CAPACITY
        self._front = 0
        self._length = 0

    def is_empty(self):
        return self._length == 0

    def _resize(self, new_cap):
        old_len = self._length
        new_data = [None] * new_cap
        k = self._front
        for ind in range(old_len):
            new_data[ind] = self._data[(k + ind) % old_len]
        self._front = 0
        self._CAPACITY = new_cap

        self._data = new_data[:]

    def __str__(self):
        ret_str = str()
        for ind in range(self._length):
            new_ind = (self._front + ind) % self._CAPACITY
            ret_str += str(self._data[new_ind])

        return ret_str


def queue_functions():
    print(5 % 5)
    md = MyDeque()
    md.append(5)
    print(md.last())
    md.append_left(3)
    print(md.last())
    md.append_left(7)
    print(md.last())
    print(md.first())
    print(md.pop())
    print(len(md))
    print(md.pop())
    print(md.pop())
    md.append_left(6)
    print(md)
    print(md.last())
    md.append_left(8)
    print(md)
    print(md.is_empty())
    print(md.last())


# Recently, on the course of algorithms and data structures, Valeriy learned how to use a deque.
# He built a deque filled with 𝑛 elements. The 𝑖-th element is 𝑎𝑖 (𝑖 = 1,2,…,𝑛).
# He gradually takes the first two leftmost elements from the deque (let's call them 𝐴 and 𝐵, respectively),
# and then does the following: if 𝐴>𝐵, he writes 𝐴 to the beginning and writes 𝐵 to the end of the deque, otherwise,
# he writes to the beginning 𝐵, and 𝐴 writes to the end of the deque. We call this sequence of actions an operation.
#
# For example, if deque was [2,3,4,5,1], on the operation he will write 𝐵=3 to the beginning and 𝐴=2 to the end,
# so he will get [3,4,5,1,2].
#
# The teacher of the course, seeing Valeriy, who was passionate about his work, approached him and gave him 𝑞 queries.
# Each query consists of the singular number 𝑚𝑗 (𝑗=1,2,…,𝑞). It is required for each query to answer which two elements
# he will pull out on the 𝑚𝑗-th operation.
#
# Note that the queries are independent and for each query the numbers 𝐴 and 𝐵 should be printed in the order in
# which they will be pulled out of the deque.
#
# Deque is a data structure representing a list of elements where insertion of new elements or deletion of
# existing elements can be made from both sides.
#
# Input
# The first line contains two integers 𝑛 and 𝑞 (2≤𝑛≤105, 0≤𝑞≤3⋅105) —
# the number of elements in the deque and the number of queries.
# The second line contains 𝑛 integers 𝑎1, 𝑎2, ..., 𝑎𝑛, where 𝑎𝑖 (0≤𝑎𝑖≤109) — the deque element in 𝑖-th position.
# The next 𝑞 lines contain one number each, meaning 𝑚𝑗 (1≤𝑚𝑗≤1018).
#
# Output
# For each teacher's query, output two numbers 𝐴 and 𝐵 —
# the numbers that Valeriy pulls out of the deque for the 𝑚𝑗-th operation.
#
# Examples
# input
# 5 3
# 1 2 3 4 5
# 1
# 2
# 10
# output
# 1 2
# 2 3
# 5 2


from collections import deque


def ValeriyQueue():
    j_queries = [1, 2, 10]

    for val in j_queries:
        dq = deque([1, 2, 3, 4, 5])
        a = None
        b = None
        for ind in range(val):
            a = dq.popleft()
            b = dq.popleft()
            if a > b:
                dq.appendleft(a)
                dq.append(b)
            else:
                dq.appendleft(b)
                dq.append(a)

        print(a)
        print(b)
