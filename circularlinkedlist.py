# Implement Circular LinkedList with methods
# enqueue - Add an element to the back of queue.
# dequeue - Remove and return the first element of the queue (i.e., FIFO).
# rotate - Rotate front element to the back of the queue.
# first - Return (but do not remove) the element at the front of the queue.
# is_empty - Return True if the queue is empty
# __len__ - Return the number of elements in the queue.


class Node:
    __slots__ = '_element', '_next'

    def __init__(self, el, n):
        self._element = el
        self._next = n

    def element(self):
        return self._element

    def next_node(self):
        return self._next


class CircularLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._length = 0

    # enqueue - Add an element to the back of queue.
    def enqueue(self, val):
        new_node = Node(val, None)
        if self._head is None:
            self._head = new_node
            self._tail = new_node
            new_node._next = self._head
        else:
            self._tail._next = new_node
            new_node._next = self._head
            self._tail = new_node

        self._length += 1

    # dequeue - Remove and return the first element of the queue (i.e., FIFO).
    def dequeue(self):
        if self._length == 0:
            return None
        else:
            temp = self._head
            val = temp.element()
            self._head = self._head.next_node()
            self._tail._next = self._head
            self._length -= 1
            return val

    # Delete a node with given value in Circular list
    def delete_node(self, val):
        curr = self._head
        prev = self._tail
        while curr != self._tail:
            if curr.element() == val:
                if curr == self._head:
                    self._head = self._head.next_node()
                    self._tail._next = self._head
                else:
                    prev._next = curr.next_node()
                self._length -= 1
                return
            prev = curr
            curr = curr.next_node()

        if curr == self._tail and curr.element() == val:
            prev._next = self._head
            self._tail = prev

    # Delete kth node in Circular list
    def delete_kth_node(self, k):
        if self._head is None:
            pass

        curr = self._head
        prev = self._tail

        for _ in range(k - 1):
            prev = curr
            curr = curr.next_node()

        if curr == self._head:
            self._head = self._head.next_node()
            self._tail._next = self._head
        elif curr == self._tail:
            prev._next = self._head
            self._tail = prev
        else:
            prev._next = curr.next_node()
        self._length -= 1
        curr._next = None
        return curr

    def move_head_to_k(self, k):
        if self._head is None:
            pass

        curr = self._head
        prev = self._tail

        for _ in range(k - 1):
            prev = curr
            curr = curr.next_node()

        self._head = curr
        self._tail = prev
        self._tail._next = self._head

    # rotate - Rotate front element to the back of the queue.
    def rotate(self):
        self._tail = self._tail._next
        self._head = self._head.next_node()
        self._tail._next = self._head

    # first - Return (but do not remove) the element at the front of the queue.
    def first(self):
        if self._head is None:
            return None
        else:
            return self._head.element()

    # is_empty - Return True if the queue is empty
    def is_empty(self):
        return self._length == 0

    # __len__ - Return the number of elements in the queue.
    def __len__(self):
        return self._length

    def __str__(self):
        retStr = ''
        t = self._head
        while t != self._tail:
            retStr += str(t.element())
            retStr += " "
            t = t.next_node()
        retStr += str(t.element())
        return retStr


def make_circular_list():
    cll = CircularLinkedList()
    cll.enqueue(2)
    cll.enqueue(4)
    cll.enqueue(6)
    cll.enqueue(8)
    cll.enqueue(10)
    cll.enqueue(12)
    cll.enqueue(14)
    print(cll)
    return cll


# Split Circular Linked List Into Two Equal halves
def split_in_two():
    cll = make_circular_list()
    cll_new = CircularLinkedList()
    sz = len(cll)

    for _ in range(sz//2):
        n = cll.delete_kth_node(1)
        cll_new.enqueue(n.element())

    return cll, cll_new


split_in_two()

# In computer science and mathematics, the Josephus Problem (or Josephus permutation) is a theoretical problem.
# Following is the problem statement: There are n people standing in a circle waiting to be executed.
# The counting out begins at some point in the circle and proceeds around the circle in a fixed direction.
# In each step, a certain number of people are skipped and the next person is executed.
# The elimination proceeds around the circle (which is becoming smaller and smaller as the executed people are removed),
# until only the last person remains, who is given freedom. Given the total number of persons n and a number k which
# indicates that k-1 persons are skipped and kth person is killed in circle. The task is to choose the place in the
# initial circle so that you are the last one remaining and so survive.
# For example, if n = 5 and k = 2, then the safe position is 3. Firstly, the person at position 2 is killed, then
# person at position 4 is killed, then person at position 1 is killed. Finally, the person at position 5 is killed.
# So the person at position 3 survives.
# If n = 7 and k = 3, then the safe position is 4. The persons at positions 3, 6, 2, 7, 5, 1 are killed in order,
# and person at position 4 survives.


def josephus():
    cll = make_circular_list()
    k = 3

    while len(cll) != 1:
        cll.delete_kth_node(k)
        cll.move_head_to_k(k)

    print(cll)
