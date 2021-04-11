def place_number(lst, num):
    if len(lst) == 0:
        lst.insert(0, num)
        return
    j = len(lst) - 1
    while num < lst[j] and j >= 0:
        j -= 1
    if lst[j] != num:
        lst.insert(j + 1, num)


def sorted_insert():
    """
    Take in numbers as input until “stop” is entered. As you take in each number, insert it into a
    list so that the list is sorted in ascending order. That is, look through the list until you find the
    place where the new element belongs, then use .insert() to place it there. If the number is
    already in the list, do not add it again. After “stop” is entered, print out the list. Do not use
    any of Python’s built-in sorting functions.
    """
    sorted_lst = list()
    inp = input()

    while inp != 'stop':
        if inp.isnumeric():
            place_number(sorted_lst, inp)
        inp = input()

    print(','.join(sorted_lst))

sorted_insert()
