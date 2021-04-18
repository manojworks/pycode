# Given n of 1 or more, return the factorial of n, which is n * (n-1) * (n-2) ... 1.
# Compute the result recursively (without loops).

def factorial_recurse(n, accu):
    print(n, ' ', accu)
    if n == 0:
        return accu
    return factorial_recurse(n - 1, n * accu)


# We have a number of bunnies and each bunny has two big floppy ears. We want to compute the total number of ears
# across all the bunnies recursively (without loops or multiplication).

def bunny_ears_h(bunnies, accu):
    if bunnies == 0:
        return accu
    return bunny_ears_h(bunnies - 1, 2 + accu)


def bunny_count_h():
    print(bunny_ears_h(5, 0))


# We have bunnies standing in a line, numbered 1, 2, ... The odd bunnies (1, 3, ..) have the normal 2 ears.
# The even bunnies (2, 4, ..) we'll say have 3 ears, because they each have a raised foot.
# Recursively return the number of "ears" in the bunny line 1, 2, ... n (without loops or multiplication).

def bunny_ears(bunnies, accu):
    if bunnies == 0:
        return accu
    if bunnies % 2 == 0:
        return bunny_ears(bunnies - 1, 3 + accu)
    else:
        return bunny_ears(bunnies - 1, 2 + accu)


def bunny_count():
    print(bunny_ears(5, 0))


#  Given a non-negative int n, return the count of the occurrences of 7 as a digit, so for example 717 yields 2.
#  (no loops).

def count7(num, accu):
    if num == 0:
        return accu
    if num % 10 == 7:
        return count7(num // 10, 1 + accu)
    else:
        return count7(num // 10, accu)


def count7_if():
    print(count7(777777, 0))


# Given a string, compute recursively (no loops) the number of lowercase 'x' chars in the string.

def count_x(s, accu):
    if len(s) == 0:
        return accu
    if s[0] == 'x':
        return count_x(s[1:], 1 + accu)
    else:
        return count_x(s[1:], accu)


def countx():
    print(count_x('hi', 0))


# Given a string, compute recursively (no loops) the number of times lowercase "hi" appears in the string.

def count_hi(s, accu):
    if len(s) < 2:
        return accu
    if s[0:2] == 'hi':
        return count_hi(s[2:], 1 + accu)
    else:
        return count_hi(s[1:], accu)


def counthi():
    print(count_hi('xxhixx', 0))
    print(count_hi('xhixhix', 0))
    print(count_hi('hi', 0))


# Given a string, compute recursively (no loops) a new string where all appearances of "pi"
# have been replaced by "3.14".

def change_pi(s, ret_str):
    if len(s) < 2:
        ret_str.append(s)
        return
    if s[0:2] == 'pi':
        ret_str.append('3.14')
        return change_pi(s[2:], ret_str)
    else:
        ret_str.append(s[0])
        return change_pi(s[1:], ret_str)


def changepi():
    ret_str = []
    change_pi('xpix', ret_str)
    print(''.join(ret_str))
    ret_str = []
    change_pi('pipi', ret_str)
    print(''.join(ret_str))
    ret_str = []
    change_pi('pip', ret_str)
    print(''.join(ret_str))


# Given an array of ints, compute recursively the number of times that the value 11 appears in the array.
# We'll use the convention of considering only the part of the array that begins at the given index.
# In this way, a recursive call can pass index+1 to move down the array. The initial call will pass in index as 0.

def array11(arr, ind, accu):
    if ind == len(arr):
        return accu
    if arr[ind] == 11:
        return array11(arr, ind + 1, 1 + accu)
    else:
        return array11(arr, ind + 1, accu)


def array_11(arr, ind):
    print(array11(arr, ind, 0))


# Given a string, compute recursively a new string where identical chars that are adjacent in the original string
# are separated from each other by a "*".

def pair_stair(s, ind, new_str):
    new_str.append(s[ind])
    if ind == len(s) - 1:
        return
    if s[ind] == s[ind + 1]:
        new_str.append('*')
        return pair_stair(s, ind + 1, new_str)
    else:
        return pair_stair(s, ind + 1, new_str)


def pairStar(s):
    new_str = []
    pair_stair(list(s), 0, new_str)
    print(''.join(new_str))


# Count recursively the total number of "abc" substrings that appear in the given string.

def count_abc(s, ind, accu):
    if ind >= len(s) - 2:
        return accu

    if s[ind: ind + 3] == 'abc':
        accu += 1
        ind = ind + 3
    else:
        ind = ind + 1
    return count_abc(s, ind, accu)


def countAbc(s):
    print(count_abc(s, 0, 0))


# Given a string, compute recursively the number of times lowercase "hi" appears in the string,
# however do not count "hi" that have an 'x' immedately before them.

def count_Hi2(s, ind, accu):
    if ind >= len(s) - 1:
        return accu

    if s[ind: ind + 2] == 'hi' and s[ind - 1] != 'x':
        accu += 1
        ind = ind + 2
    else:
        ind = ind + 1
    return count_Hi2(s, ind, accu)


def countHi2(s):
    print(count_Hi2(s, 0, 0))


# Given a string and a non-empty substring sub, compute recursively the number of times that sub appears in the string,
# without the sub strings overlapping.

def str_Count(s, sub, ind, accu):
    len_sub = len(sub)
    if ind >= len(s) - len_sub + 1:
        return accu

    if s[ind: ind + len_sub] == sub:
        accu += 1
        ind = ind + len_sub
    else:
        ind = ind + 1
    return str_Count(s, sub, ind, accu)


def strCount(s, sub):
    print(str_Count(s, sub, 0, 0))


# We have triangle made of blocks. The topmost row has 1 block, the next row down has 2 blocks,
# the next row has 3 blocks, and so on. Compute recursively (no loops or multiplication) the total number of blocks
# in such a triangle with the given number of rows.

def triangle(num_rows):
    if num_rows == 1:
        return 1
    return num_rows + triangle(num_rows - 1)


# Given a non-negative int n, compute recursively (no loops) the count of the occurrences of 8 as a digit,
# except that an 8 with another 8 immediately to its left counts double,
# so 8818 yields 4.

def count_8(num, accu):
    if num == 0:
        return accu
    if num % 10 == 8:
        val = num // 10
        if val % 10 == 8:
            return count_8(num // 10, 2 + accu)
        else:
            return count_8(num // 10, 1 + accu)
    else:
        return count_8(num // 10, accu)


def count8(num):
    print(count_8(num, 0))
