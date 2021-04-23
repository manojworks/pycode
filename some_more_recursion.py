# Given a string, compute recursively a new string where all the 'x' chars have been removed.

def no_X(s, ret_str):
    if len(s) == 0:
        return
    if s[0] == 'x':
        return no_X(s[1:], ret_str)
    else:
        ret_str.append(s[0])
        return no_X(s[1:], ret_str)


def noX():
    ret_str = []
    no_X('xaxb', ret_str)
    print(''.join(ret_str))
    ret_str = []
    no_X('abc', ret_str)
    print(''.join(ret_str))
    ret_str = []
    no_X('xx', ret_str)
    print(''.join(ret_str))


# Given a string, compute recursively a new string where all the lowercase 'x' chars have
# been moved to the end of the string.

def end_X(s, ret_str, accu):
    if len(s) == 0:
        return accu
    if s[0] == 'x':
        accu += 1
        return end_X(s[1:], ret_str, accu)
    else:
        ret_str.append(s[0])
        return end_X(s[1:], ret_str, accu)


def endX():
    ret_str = []
    accu = end_X('xxre', ret_str, 0)
    ret_str.append('x' * accu)
    print(''.join(ret_str))
    ret_str = []
    accu = end_X('xxhixx', ret_str, 0)
    ret_str.append('x' * accu)
    print(''.join(ret_str))
    ret_str = []
    accu = end_X('xhixhix', ret_str, 0)
    ret_str.append('x' * accu)
    print(''.join(ret_str))


# Given a string that contains a single pair of parenthesis, compute recursively a new string made of only of the
# parenthesis and their contents, so "xyz(abc)123" yields "(abc)".

# assume that there is indeed a single pair of parenthesis
def paren_Bit(s, ret_str):
    if s[0] == ')':
        ret_str.append(')')
        return
    if s[0] == '(':
        ret_str.append('(')
        return paren_Bit(s[1:], ret_str)
    if len(ret_str):
        ret_str.append(s[0])
        return paren_Bit(s[1:], ret_str)
    else:
        return paren_Bit(s[1:], ret_str)


def parenBit():
    ret_str = []
    paren_Bit('xyz(abc)123', ret_str)
    print(''.join(ret_str))
    ret_str = []
    paren_Bit('x(hello)', ret_str)
    print(''.join(ret_str))
    ret_str = []
    paren_Bit('(xy)1', ret_str)
    print(''.join(ret_str))


# Given a string and a non-empty substring sub, compute recursively if at least n copies of sub appear in the string
# somewhere, possibly with overlapping. N will be non-negative.

def str_copies(s, sub, ind, accu, n):
    len_sub = len(sub)

    if n == accu:
        return True

    if ind >= len(s) - len_sub + 1:
        return False

    if s[ind: ind + len_sub] == sub:
        accu += 1
        ind = ind + len_sub
    else:
        ind = ind + 1
    return str_copies(s, sub, ind, accu, n)


def strCopies(s, sub, n):
    print(str_copies(s, sub, 0, 0, n))


# The fibonacci sequence is a famous bit of mathematics, and it happens to have a recursive definition.
# The first two values in the sequence are 0 and 1 (essentially 2 base cases). Each subsequent value is
# the sum of the previous two values, so the whole sequence is: 0, 1, 1, 2, 3, 5, 8, 13, 21 and so on.
# Define a recursive fibonacci(n) method that returns the nth fibonacci number, with n=0
# representing the start of the sequence.

def fibonacci(n):
    if n <= 1:
        return n, 0
    else:
        (a, b) = fibonacci(n - 1)
        return a + b, a


def fib_optimal(n):
    x, y = fibonacci(n)
    return x


# Given a non-negative int n, return the sum of its digits recursively (no loops).
def sumDigits(n, accu):
    if n == 0:
        return accu
    accu += n % 10
    return sumDigits(n // 10, accu)


def sum_digits(n):
    print(sumDigits(n, 0))


# Given base and n that are both 1 or more, compute recursively (no loops) the value of base to the n power,
# so powerN(3, 2) is 9 (3 squared)

def powpow(b, n, val):
    if n == 0:
        return val
    val = val * b
    return powpow(b, n - 1, val)


def power(b, n):
    print(powpow(b, n, 1))


# Given a string, compute recursively (no loops) a new string where all the lowercase 'x' chars
# have been changed to 'y' chars.

def change_XY(s, ret):
    if len(s) == 0:
        return
    if s[0] == 'x':
        ret.append('y')
    else:
        ret.append(s[0])
    return change_XY(s[1:], ret)


def changeXY(s):
    ret = []
    change_XY(s, ret)
    print(''.join(ret))


# Given an array of ints, compute recursively if the array contains a 6.

def array6(arr):
    if len(arr) == 0:
        return False

    if arr[0] == 6:
        return True
    return array6(arr[1:])


# Given a string, compute recursively a new string where all the adjacent chars are now separated by a "*".

def all_star(s, ret):
    if len(s) == 1:
        ret.append(s[0])
        return
    ret.append(s[0])
    ret.append('*')
    return all_star(s[1:], ret)


def allStar(s):
    ret = []
    all_star(s, ret)
    print(''.join(ret))


# We'll say that a "pair" in a string is two instances of a char separated by a char.
# So "AxA" the A's make a pair. Pair's can overlap, so "AxAxA" contains 3 pairs -- 2 for A and 1 for x.
# Recursively compute the number of pairs in the given string.

def count_pairs(s, ind, accu):
    if ind == len(s) - 2:
        return accu
    if s[ind] == s[ind + 2]:
        accu += 1
    ind += 1
    return count_pairs(s, ind, accu)


def countPairs(s):
    print(count_pairs(s, 0, 0))


# Given a string and a non-empty substring sub, compute recursively the largest substring
# which starts and ends with sub and return its length.


def str_dist(s, sub, ind, accu):
    # index has reached the point where only next len(sub) chats remain in string
    # and the sub has been already found in s
    if (ind == len(s) - len(sub)) and (accu > 0):
        if s[ind:ind + len(sub)] == sub:
            accu += len(sub)
        return accu

    if len(s) - ind - 1 < len(sub):
        return accu

    if s[ind:ind + len(sub)] == sub:
        accu += len(sub)
        ind += len(sub)
    else:
        if accu > 0:
            accu += 1
        ind += 1

    return str_dist(s, sub, ind, accu)


def strDist(s, sub):
    print(str_dist(s, sub, 0, 0))


# Given a string, return recursively a "cleaned" string where adjacent chars that are the same have been
# reduced to a single char. So "yyzzza" yields "yza".

def string_clean(s, ind, ret_str):
    if len(s) == 1:
        ret_str.append(s[0])
        return

    if s[0] != s[1]:
        ret_str.append(s[0])

    return string_clean(s[1:], ind, ret_str)


def stringClean(s):
    ret_str = []
    string_clean(s, 0, ret_str)
    print(''.join(ret_str))


# Given a string, return true if it is a nesting of zero or more pairs of parenthesis,
# like "(())" or "((()))".
# Suggestion: check the first and last chars, and then recur on what's inside them.


def nestParen(s):
    if len(s) == 0:
        return True

    if s[0] == '(' and s[-1] == ')':
        return nestParen(s[1:-1])
    else:
        return False


# Given an array of ints, compute recursively if the array contains somewhere a value followed in the array
# by that value times 10.
# We'll use the convention of considering only the part of the array that begins at the given index.
# In this way, a recursive call can pass index+1 to move down the array. The initial call will pass in index as 0.

def array220(arr, ind):
    if ind == len(arr) - 1:
        return False

    if arr[ind] * 10 in arr[ind:]:
        return True
    else:
        return array220(arr, ind+1)
