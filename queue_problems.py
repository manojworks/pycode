class QueueT:

    def __init__(self):
        self._CAPACITY = 6
        self._data = [None] * self._CAPACITY
        self._length = 0
        self._first = 0

    def enqueue(self, val):
        if self.size() == self._CAPACITY:
            self._resize(self._CAPACITY * 2)
            self.enqueue(val)
        else:
            new_place = (self._first + self.size()) % self._CAPACITY
            self._data[new_place] = val
            self._length += 1

    def dequeue(self):
        if self.size() <= self._CAPACITY // 4:
            self._resize(self._CAPACITY // 4)
            return self.dequeue()
        else:
            val = self._data[self._first]
            self._data[self._first] = None
            self._length -= 1
            self._first = (self._first + 1) % self._CAPACITY
            return val

    def size(self):
        return self._length

    def front(self):
        return self._data[self._first]

    def is_empty(self):
        return self._length == 0

    def clear(self):
        self._CAPACITY = 6
        self._data = [None] * self._CAPACITY
        self._length = 0
        self._first = 0

    def _resize(self, new_capacity):
        old = self._data
        old_capacity = len(old)
        self._data = [None] * new_capacity
        k = self._first
        self._first = 0
        for j in range(self._length):
            self._data[j] = old[k]
            k = (1 + k) % old_capacity
        self._CAPACITY = new_capacity

    def __str__(self):
        st = ''
        k = self._first
        for i in range(self._length):
            st += str(self._data[k])
            st += ' '
            k = (1 + k) % self._CAPACITY

        return st


def make_queue():
    q = QueueT()
    q.enqueue(7)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(1)
    q.enqueue(8)

    return q


# Given M integers, task is to find the frequency of each number in the Queue.

def number_frequency():
    q = make_queue()
    t = QueueT()
    freq_map = {}

    while q.size() > 0:
        key = q.dequeue()
        val = freq_map.setdefault(key, 0)
        freq_map[key] = val + 1
        t.enqueue(key)

    print(freq_map)


# Given a Queue Q containing N elements. The task is to reverse the Queue.

def reverse_q_all():
    q = make_queue()
    s = Stack_t()

    while not q.is_empty():
        val = q.dequeue()
        s.push(val)

    q.clear()

    while not s.is_empty():
        val = s.pop()
        q.enqueue(val)

    print(q)


# Given an integer K and a queue of integers, we need to reverse the order of the first K elements of the queue,
# leaving the other elements in the same relative order.
# Only following standard operations are allowed on queue.
# enqueue(x) : Add an item x to rear of queue
# dequeue() : Remove an item from front of queue
# size() : Returns number of elements in queue.
# front() : Finds front item.


def reverse_q_k():
    q = make_queue()
    print(q)

    s = Stack_t()
    k = 4

    ind = 0
    while not q.is_empty() and ind < k:
        val = q.dequeue()
        s.push(val)
        ind += 1

    new_q = QueueT()

    while not s.is_empty():
        val = s.pop()
        new_q.enqueue(val)

    while not q.is_empty():
        val = q.dequeue()
        new_q.enqueue(val)

    print(new_q)


# Sorting a Queue without extra space

def find_min_q(q, max_ind):
    min_val = q.front()
    min_ind = 0
    n = q.size()
    for ind in range(0, n):
        val = q.dequeue()
        if val < min_val and ind < max_ind:
            min_val = val
            min_ind = ind
        q.enqueue(val)

    return min_val, min_ind


def put_min_in_rear(q, min_ind):
    min_val = q.front()
    for i in range(q.size()):
        val = q.dequeue()
        if i != min_ind:
            q.enqueue(val)
        else:
            min_val = val
    q.enqueue(min_val)


def sort_queue(q=make_queue()):
    for j in range(q.size()):
        min_val, min_ind = find_min_q(q, q.size() - j)
        put_min_in_rear(q, min_ind)

    return q
