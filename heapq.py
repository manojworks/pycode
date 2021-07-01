# A Heap Priority Queue using an array-based heap with methods
# add - Add a key-value pair to the Heap Priority Queue
# min - Return but do not remove (k,v) tuple with minimum key, Raise Empty exception if empty
# remove_min - Remove and return (k,v) tuple with minimum key. Raise Empty exception if empty.
# _parent(self, j)
# _left(self, j) - left child node
# _right(self, j)
# _has_left(self, j)
# _has_right(self, j)
# _swap(self, i, j)
# _upheap(self, j)
# _downheap(self, j)
# pushpop(e) - Push element e on list L and then pop and return the smallest item.

# Convert max heap to min heap in linear time


class HeapQ:

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def _append(self, k, v):
        self._data.append((k, v))

    def _parent(self, j) -> int:
        return (j - 1) // 2

    def _left(self, j) -> int:
        return 2 * j + 1

    def _right(self, j) -> int:
        return 2 * (j + 1)

    def _has_left(self, j) -> bool:
        return j >= 0 and self._left(j) < len(self._data)

    def _has_right(self, j) -> bool:
        return j >= 0 and self._right(j) < len(self._data)

    def _swap(self, i, j) -> None:
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _upheap(self, j):
        i = self._parent(j)
        if i >= 0 and self._data[i][0] > self._data[j][0]:
            self._swap(i, j)
            self._upheap(i)

    def _upheap_max(self, j):
        i = self._parent(j)
        if i >= 0 and self._data[i][0] < self._data[j][0]:
            self._swap(i, j)
            self._upheap(i)

    def _downheap(self, j):
        # if there is a left child then swap with it and recur
        if self._has_left(j):
            left_child = self._data[self._left(j)]
            smaller_child_key = left_child[0]
            smaller_child_ind = self._left(j)
        if self._has_right(j):
            right_child = self._data[self._right(j)]
            if right_child[0] < left_child[0]:
                smaller_child_key = right_child[0]
                smaller_child_ind = self._right(j)
            if smaller_child_key < self._data[j][0]:
                self._swap(smaller_child_ind, j)
                self._downheap(smaller_child_ind)

    def is_empty(self):
        return len(self) == 0

    def add(self, k, v):
        self._data.append((k, v))
        self._upheap(len(self._data) - 1)

    def add_max(self, k, v):
        self._data.append((k, v))
        self._upheap_max(len(self._data) - 1)

    def min(self):
        # TODO: Raise exception
        if self.is_empty():
            pass
        else:
            return self._data[0]

    def remove_min(self):
        # TODO: Raise exception
        if self.is_empty():
            pass
        else:
            # first swap the last and first item
            self._swap(0, len(self._data)-1)
            # original first is the min so this is now the last
            min_item = self._data.pop()
            # the max is actually at root now, so bring it to its place
            self._downheap(0)
            return min_item

    def pushpop(self, k, v) -> ():
        self.add(k, v)
        return self.remove_min()

    def __str__(self):
        return ''.join(map(str, self._data))


def transform_to_max_heap(hmin):
    hmax = HeapQ()
    while not hmin.is_empty():
        el = hmin.remove_min()
        hmax.add_max(el[0], el[1])

    return hmax


def heap_driver():
    hpq = HeapQ()
    hpq.add(6, 'Z')
    hpq.add(5, 'A')
    hpq.add(13, 'W')
    hpq.add(20, 'B')
    hpq.add(15, 'K')
    hpq.add(7, 'Q')
    hpq.add(14, 'E')
    hpq.add(25, 'J')
    hpq.add(11, 'S')
    hpq.add(9, 'F')
    hpq.add(16, 'X')
    hpq.add(12, 'M')
    hpq.add(4, 'C')
    print(hpq)

    hmax = transform_to_max_heap(hpq)
    print(hmax)


heap_driver()
