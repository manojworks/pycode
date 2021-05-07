class _Node:
    """
    A node of Linked List
    """
    __slots__ = '_element', '_next'

    def __init__(self, val, nxt):
        self._element = val
        self._next = nxt

    def element(self):
        return self._element

    def next(self):
        return self._next


class LinkedList:
    """
    LinkedList class that starts with head and tail and keeps track of its size.
    The underlying storage is a list.
    """
    def __init__(self, st=None):
        self._head = None
        self._tail = None
        self._size = 0
        if st is not None:
            [self.add_node(x) for x in st]

    # Add a node to list
    def add_node(self, val):
        n = _Node(val, None)
        n._next = self._head
        self._head = n
        if self._size == 0:
            self._tail = self._head
        self._size += 1

    # a a node to the left of list
    def add_left(self, val):
        return self.add_node(val)

    # a a node to the right of list
    def add_right(self, val):
        n = _Node(val, None)
        self._tail._next = n
        self._tail = self._tail.next()
        self._tail._next = None

    # delete the head node
    # if the node to be deleted is the leftmost node
    def delete_head(self):
        # where there are no nodes. Throw an exception
        if self._head is None and self._tail is None:
            pass
        # if there is only 1 node
        if self.size() == 1:
            val = self._head.element()
            self._head = None
            self._tail = None
            self._size = 0
            return val
        else:
            val = self._head.element()
            self._head = self._head.next()
            self._size -= 1
            return val

    # delete the tail node
    def delete_tail(self):
        # where there are no nodes. Throw an exception
        if self._head is None and self._tail is None:
            pass
        # if there is only 1 node
        if self.size() == 1:
            val = self._head.element()
            self._head = None
            self._tail = None
            self._size = 0
            return val
        else:
            temp = self._head
            prev = None

            while temp != self._tail:
                prev = temp
                temp = temp.next()
            prev._next = None
            self._tail = prev
            self._size -= 1
            return temp.element()

    # delete the node being passed
    def delete_this_node(self, node):
        # where there are no nodes. Throw an exception
        if self._head is None and self._tail is None:
            pass
        temp = self._head
        prev = None
        while temp != node and temp is not None:
            prev = temp
            temp = temp.next()

        if temp is None:
            return None

        if temp == self._tail:
            self._tail = prev

        if prev is not None:
            prev._next = temp.next()
            temp = None
        else:
            # we are still at head
            self._head = self._head.next()

        self._size -= 1
        return node.element()

    # delete the first node with value v
    def delete_node(self, val):
        # where there are no nodes. Throw an exception
        if self._head is None and self._tail is None:
            pass
        # if there is only 1 node
        if self.size() == 1:
            val = self._head.element()
            self._head = None
            self._tail = None
            self._size = 0
            return val
        else:
            temp = self._head
            prev = None

            while temp is not None and temp.element() != val:
                prev = temp
                temp = temp.next()

            if temp is None:
                return None

            if temp == self._tail:
                self._tail = prev

            prev._next = temp.next()
            temp = None
            self._size -= 1
            return val

    # check if list is empty
    def is_empty(self):
        return self._size == 0

    # return the first element in list
    def first(self):
        return self._head.element()

    # return the size of list
    def size(self):
        return self._size

    # return the head node
    def head(self):
        return self._head

    def next_node(self):
        return self._head.next()

    # cheeck if the list passed is same (has same values) as this node
    def is_equal(self, ll):
        l_head = self.head()
        r_head = ll.head()

        while l_head is not None or r_head is not None:
            if l_head.element() != r_head.element():
                return False
            l_head = l_head.next()
            r_head = r_head.next()

        if l_head is not None or r_head is not None:
            return False

        return True

    # string representation of the list
    def __str__(self):
        head_val = self._head
        ret_str = ''
        while head_val is not None:
            ret_str += str(head_val.element())
            head_val = head_val.next()

        return ret_str


# driver code
def do_linked_list():
    ll = LinkedList()
    ll.add_node(2)
    ll.add_node(3)
    ll.add_node(7)
    ll.add_node(4)

    return ll


# Reverse Linked List (Recursive Solution)

def reverse_list_recur(lst, rlst):
    if lst is None:
        return

    rlst.add_node(lst.element())
    return reverse_list_recur(lst.next(), rlst)


def reverse_list():
    lst = do_linked_list()
    r_lst = LinkedList()
    reverse_list_recur(lst.head(), r_lst)


# Check if linked list is palindrome or not

def palindrome():
    actual_list = LinkedList('HANQNAH')
    reversed_list = LinkedList()
    reverse_list_recur(actual_list.head(), reversed_list)
    print(actual_list.is_equal(reversed_list))


# Given a linked list containing 0s, 1s and 2s, sort linked list by doing a single traversal of it.

def order_012():
    data = [2, 2, 2, 2, 2, 0, 0, 0]
    ll = LinkedList(data)
    node_iter = ll.head()
    for _ in range(ll.size()):
        if node_iter.element() == 2:
            val = ll.delete_this_node(node_iter)
            ll.add_right(val)
        if node_iter.element() == 0:
            val = ll.delete_this_node(node_iter)
            ll.add_left(val)
        node_iter = node_iter.next()

    print(ll)


# You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and
# each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
#     342 + 465 = 807
# Make sure there are no trailing zeros in the output list
# So, 7 -> 0 -> 8 -> 0 is not a valid response even though the value is still 807.

def add_lists():
    # 789
    n1 = LinkedList([7, 8, 9])
    # 465
    n2 = LinkedList([4, 6, 5])

    sum_list = LinkedList()

    n1_iter = n1.head()
    n2_iter = n2.head()

    carry_over = 0
    while n1_iter is not None and n2_iter is not None:
        place_val = n1_iter.element() + n2_iter.element() + carry_over
        sum_list.add_node(place_val % 10)
        carry_over = place_val // 10

        n1_iter = n1_iter.next()
        n2_iter = n2_iter.next()

    if carry_over != 0:
        sum_list.add_node(carry_over)

    print(sum_list)
