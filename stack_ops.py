class StackEmpty(Exception):

    def __str__(self):
        return "Stack empty"


class Stack_t:

    def __init__(self):
        self._data = []

    def push(self, val):
        self._data.append(val)

    def pop(self):
        if len(self._data) == 0:
            raise StackEmpty

        return self._data.pop()

    def is_empty(self):
        return len(self._data) == 0

    def top(self):
        if not self.is_empty():
            return self._data[-1]
        else:
            return None

    def size(self):
        return len(self._data)

    def __str__(self):
        return ' , '.join(str(ch) for ch in self._data)


def make_stack():
    s = Stack_t()

    for ch in 'rats live on no evil star':
    #for ch in 'rotator':
        s.push(ch)

    return s

# Here is a technique that employs two stacks in order to determine if a phrase is a palindrome, that is,
# reads the same forward and backward (for example, the word “rotator'” is a palindrome, as is the string
# “rats live on no evil star”). Read the characters one by one and transfer them into a stack. The characters in
# the stack will then represent the reversed word. Once all characters have been read, transfer half the characters
# from the first stack into a second stack. Thus, the order of the words will have been restored. If there were an odd
# number of characters, remove one further character from the original stack. Finally, test the two stacks for
# equality, element by element. If they are the same, then the word is a palindrome.
# Write a procedure that takes a String argument and tests to see if it is a palindrome using this algorithm.

def palindrome():
    s = make_stack()
    t = Stack_t()

    length = s.size() // 2

    for _ in range(length):
        t.push(s.pop())

    if s.size() != t.size():
        s.pop()

    while not s.is_empty():
        if s.pop() != t.pop():
            print('Not a Palindrome')
            return

    print('A Palindrome')


# Give a recursive implementation of the client-side function int stack_size(stack_t S);
# that takes as input a stack S and returns the number of elements in it. Upon returning, the input stack should
# contain the same elements in the same order as when it was called.


def recur_stack_size(s, t, ret_val):
    if s.is_empty():
        return
    val = s.pop()
    t.push(val)
    ret_val[0] += 1
    recur_stack_size(s, t, ret_val)
    val = t.pop()
    s.push(val)


def stack_size(s):
    t = Stack_t()
    ret_val = [0]
    recur_stack_size(s, t, ret_val)
    print(ret_val[0])
    print(s)


# Implement the function void stack_sort(stack_t S); that sorts its input stack in-place.
# The resulting stack should be sorted in ascending order, with the largest item at the top and the smallest at the
# bottom. Your code may use temporary stacks but no other data structures. You may use any function on stack interface
# Hint an effective way to solve this exercise is carefully consider what loop invariants should hold at various points.

def stack_sort(s):
    t = Stack_t()
    is_sorted = False

    for _ in range(s.size()):
        is_sorted = True
        while True:

            v1 = s.pop()
            if s.top() is not None:
                v2 = s.pop()
            else:
                s.push(v1)
                break

            if v1 < v2:
                s.push(v1)
                t.push(v2)
                is_sorted = False
            else:
                t.push(v1)
                s.push(v2)

        while not t.is_empty():
            val = t.pop()
            s.push(val)

        if is_sorted:
            break

    print(s)


# Another example of the parentheses matching problem comes from hypertext markup language (HTML).
# In HTML, tags exist in both opening and closing forms and must be balanced to properly describe a web document.
# This very simple HTML document:
#
# <html>
#    <head>
#       <title>
#          Example
#       </title>
#    </head>
#
#    <body>
#       <h1>Hello, world</h1>
#    </body>
# </html>
# is intended only to show the matching and nesting structure for tags in the language. Write a program that can
# check an HTML document for proper opening and closing tags.

def valid_html():
    tag_stack = Stack_t()

    with open('sample.html', 'r') as fp:
        html_content = fp.read().replace('\n', '')
        ind = html_content.find('<')
        curr = ind
        while ind != -1:
            ind = html_content[curr + 1:].find('>')
            if ind == -1:
                return False
            tag = html_content[curr + 1:curr + ind + 1]
            if tag[0] == '<':
                tag = tag[1:]
            # closing tag
            if tag[0] == '/':
                tag = tag[1:]
                last_tag = tag_stack.pop()
                if last_tag != tag:
                    return False
            else:
                tag_stack.push(tag)

            curr = curr + ind + 1
            ind = html_content[curr + 1:].find('<')
            curr += ind

    return True
