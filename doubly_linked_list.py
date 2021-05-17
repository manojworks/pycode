# A node class to represnet a node of a doubly linked list
# with references to previous and next
class Node:
    __slots__ = '_element', '_next', '_prev'

    def __init__(self, el, n, p):
        self._element = el
        self._next = n
        self._prev = p

    def element(self):
        return self._element

    def next_node(self):
        return self._next

    def prev_node(self):
        return self._prev

# The doubly linked list class with references to nodes that are head and tail of the list
class DoublyLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._length = 0

    # add to the front of the list
    def add_front(self, val):
        new_node = Node(val, None, None)

        if self._head is None:
            self._head = new_node
            self._tail = new_node
        else:
            new_node._next = self._head
            self._head._prev = new_node
            self._head = new_node

        self._length += 1

    # add after the node
    def add_after(self, n, val):
        temp = self._head
        while temp != n:
            temp = temp.next_node()

        next_to_temp = temp.next_node()
        new_node = Node(val, None, None)
        new_node._next = temp.next_node()
        temp._next = new_node

        new_node._prev = temp
        next_to_temp._prev = new_node

        self._length += 1

    # add before a node
    def add_before(self, n, val):
        temp = self._tail
        while temp != n:
            temp = temp.prev_node()

        prev_to_temp = temp.prev_node()
        new_node = Node(val, None, None)
        new_node._next = temp
        prev_to_temp._next = new_node
        new_node._prev = prev_to_temp
        temp._prev = new_node

        self._length += 1

    # add to the end of the list
    def add_end(self, val):
        new_node = Node(val, None, None)

        if self._head is None:
            self._head = new_node
            self._tail = new_node
        else:
            self._tail._next = new_node
            new_node._prev = self._tail
            self._tail = new_node

        self._length += 1

    # delete a node from the list
    def delete_node(self, n):
        if self._head == n:
            self._head.next_node()._prev = None
            self._head = self._head.next_node()
        elif self._tail == n:
            prev_to_tail = self._tail.prev_node()
            self._tail._prev = None
            prev_to_tail._next = None
            self._tail = prev_to_tail
        else:
            curr = self._head
            while curr != n:
                curr = curr.next_node()
            prev_to_curr = curr.prev_node()
            prev_to_curr._next = curr.next_node()
            curr.next_node()._prev = prev_to_curr
            curr._next = None
            curr._prev = None

        self._length -= 1

    # return an iterator to the list
    def __iter__(self):
        return DllIterator(self)

    # reverse the list using a generator
    def __reversed__(self):
        cursor = self._tail
        while cursor is not None:
            yield cursor
            cursor = cursor.prev_node()

    # return first element of the list
    def first(self):
        return self._head

    # return last element of the list
    def last(self):
        return self._tail

    # rotate the list by n positions
    def rotate_by_n(self, n):

        self._tail._next = self._head
        self._head._prev = self._tail

        nth_node = self.kth_node(n)
        prev_nth_node = nth_node.prev_node()

        nth_node._prev = None
        self._head = nth_node

        prev_nth_node._next = None
        self._tail = prev_nth_node

    # get t he kth node in the list
    def kth_node(self, k):
        if k > self._length:
            return None
        ind = 1
        temp = self._head
        while ind < k:
            temp = temp.next_node()
            ind += 1
        return temp

    # the length of the list
    def __len__(self):
        return self._length

    # string representation of the list
    def __str__(self):
        retStr = ''
        temp = self._head
        while temp is not None:
            retStr += str(temp.element())
            retStr += '\n'
            temp = temp.next_node()

        return retStr


# A class iterator using generator
class DllIterator:
    def __init__(self, dll):
        self._dll = dll
        self._cursor = dll.first()
        self._index = 0

    def __next__(self):
        if self._index < len(self._dll):
            yield self._cursor.next_node()
            self._index += 1
        raise StopIteration

# A class to represent a player with a score
class Player:
    def __init__(self, name, score):
        self._name = name
        self._score = score

    def score(self):
        return self._score

    def __eq__(self, other):
        if isinstance(other, Player):
            return self._score == other._score
        else:
            return False

    def __str__(self):
        return f'[ {self._name} : {self._score} ]'

# Driver code for the players in the doubly linked list fashion
def make_dll():
    dll = DoublyLinkedList()
    dll.add_front(Player('Manoj', 20))
    dll.add_front(Player('Shreya', 10))
    dll.add_end(Player('Shubhi', 30))
    dll.add_after(dll.kth_node(2), Player('Shalinee', 50))
    dll.add_before(dll.kth_node(2), Player('Chiku', 40))
    dll.add_front(Player('Chunmun', 90))
    dll.add_front(Player('Shinu', 80))
    dll.add_end(Player('Dolly', 60))
    dll.add_end(Player('Jhalli', 70))

    return dll

# Standard driver code
def make_dll1():
    dll = DoublyLinkedList()
    print('Empty ' + str(dll))
    dll.add_front(1)
    print('1 in front ' + str(dll))
    dll.add_front(2)
    print('2 in front ' + str(dll))
    dll.add_end(9)
    print('9 in end ' + str(dll))
    dll.add_front(3)
    print('3 in front ' + str(dll))
    dll.add_end(98)
    print('98 nin end ' + str(dll))
    dll.add_front(4)
    print('4 in front ' + str(dll))
    dll.add_end(45)
    print('45 in end ' + str(dll))
    node2 = dll.kth_node(3)
    dll.add_before(node2, 55)
    print('Add 55 before 3rd node ' + str(dll))
    dll.add_after(node2, 32)
    print('Add 32 after 3rd node ' + str(dll))
    node2 = dll.kth_node(1)
    dll.delete_node(node2)
    print('Delete first ' + str(dll))
    node2 = dll.kth_node(len(dll))
    dll.delete_node(node2)
    print('Delete last ' + str(dll))
    node2 = dll.kth_node(4)
    dll.delete_node(node2)
    print('Delete 4th ' + str(dll))
    print('Forward:')
    for val in dll:
        print(val, end=' ')
    print('\nReversed')
    for val in reversed(dll):
        print(val, end=' ')


# Given a doubly-linked list, the task is to swap Kth node from the beginning with Kth node from the ending.
def swap_kth(k):
    dll = make_dll()
    print(dll)
    l = len(dll)

    if k <= 0:
        return None

    if k > l:
        return dll

    if k == l//2 + 1:
        return dll

    if k == 1:
        # swap head and tail
        head = dll.kth_node(0)
        tail = dll.kth_node(l)
        dll.delete_node(dll.first())
        dll.delete_node(dll.last())
        dll.add_front(tail.element())
        dll.add_end(head.element())
        return dll
    else:
        to_add_after = dll.kth_node(k-1)
        to_delete_left = to_add_after.next_node()
        element_to_swap_left = to_delete_left.element()
        dll.delete_node(to_delete_left)
        to_add_before = dll.kth_node(l-k+1)
        to_delete_right = to_add_before.prev_node()
        element_to_swap_right = to_delete_right.element()
        dll.delete_node(to_delete_right)
        dll.add_after(to_add_after, element_to_swap_right)
        dll.add_before(to_add_before, element_to_swap_left)
        return dll


# Given a doubly-linked list and an integer N, the task is to rotate the linked list clockwise by N nodes.
def rotate_dll(dll, n):
    print(dll)
    dll.rotate_by_n(n+1)
    print(dll)
