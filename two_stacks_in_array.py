# Describe a structure which provides two stacks with a single array as backup structure. Implement
# the Pop and Push operations.

class Two_Stacks:

    def __init__(self):
        self._capacity = 8
        self._data = [None] * self._capacity

        self._length_left = 0
        self._top_left = -1

        self._length_right = 0
        self._top_right = self._capacity

    def push_left(self, val):
        # there is an empty slot in stack_left
        if self._top_left + 1 < self._top_right:
            self._data[self._top_left + 1] = val
            self._top_left += 1
            self._length_left += 1
        else:
            self._make_space()
            self.push_left(val)

    def is_empty_left(self):
        return self._length_left == 0

    def pop_left(self):
        if self.is_empty_left():
            raise StackEmpty
        else:
            val = self._data[self._top_left]
            self._data[self._top_left] = None
            self._top_left -= 1
            self._length_left -= 1
            return val

    def size_left(self):
        return self._length_left

    def push_right(self, val):
        # there is an empty slot
        if self._top_right - 1 > self._top_left:
            self._data[self._top_right - 1] = val
            self._top_right -= 1
            self._length_right += 1
        else:
            self._make_space()
            self.push_right(val)

    def is_empty_right(self):
        return self._length_right == 0

    def pop_right(self):
        if self.is_empty_right():
            raise StackEmpty
        else:
            val = self._data[self._top_right]
            self._data[self._top_right] = None
            self._top_right += 1
            self._length_right -= 1
            return val

    def size_right(self):
        return self._length_right

    def _make_space(self):
        new_capacity = self._capacity * 2
        self._data.extend([None] * self._capacity)
        # push stack_right elements to right
        j = new_capacity - 1
        for i in range(self._capacity - 1, self._top_right - 1, -1):
            self._data[j] = self._data[i]
            self._data[i] = None
            j -= 1
        self._capacity = new_capacity
        self._top_right = new_capacity - self._length_right

    def __str__(self):
        s1 = ' , '.join([str(self._data[i]) for i in range(0, self._top_left + 1)])
        s2 = ' , '.join([str(self._data[i]) for i in range(self._capacity - 1, self._top_right - 1, -1)])
        return "Left : " + s1 + '\n' + 'Right : ' + s2
