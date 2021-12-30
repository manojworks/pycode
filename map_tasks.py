
"""
Design a map that allows you to do the following:
Maps a string key to a given value.
Returns the sum of the values that have a key with a prefix equal to a given string.

Example 1:

Input
["MapSum", "insert", "sum", "insert", "sum"]
[[], ["apple", 3], ["ap"], ["app", 2], ["ap"]]
Output
[null, null, 3, null, 5]

Explanation
MapSum mapSum = new MapSum();
mapSum.insert("apple", 3);
mapSum.sum("ap");           // return 3 (apple = 3)
mapSum.insert("app", 2);
mapSum.sum("ap");           // return 5 (apple + app = 3 + 2 = 5)

Constraints:

1 <= key.length, prefix.length <= 50
key and prefix consist of only lowercase English letters.
1 <= val <= 1000
At most 50 calls will be made to insert and sum.

"""


class MapSum:
    # Initializes the MapSum object.
    def __init__(self):
        self.data ={}

    # Inserts the key-val pair into the map. If the key already existed,
    # the original key-value pair will be overridden to the new one.
    def insert(self, key: str, val: int) -> None:
        self.data[key] = val

    # Returns the sum of all the pairs' value whose key starts with the prefix.
    def sum(self, prefix: str) -> int:
        sum_val = 0
        for k, v in self.data.items():
            if str(k).startswith(prefix):
                sum_val += v
        return sum_val

    def __str__(self):
        return "".join(str(self.data))


"""
You are given a sequence of positive integers of length N
a = (a1,a2,...,aN)
Your objective is to remove some of the elements in a so that a will be a good sequence.

Here, a sequence b is a good sequence when the following condition holds true:

For each element x in b, the value x occurs exactly x times in b.
For example, (3,3,3), (4,2,4,1,4,2,4) and () (an empty sequence) are good sequences, while
(3,3,3,3) and (2,4,1,4,2) are not.

Find the minimum number of elements that needs to be removed so that a will be a good sequence.

"""

"""
    if k > v it means that we have to remove all v elements with value k from seq
    if k < v then we should should remove v - k elements with value k
    if k == v then the key is a good element in sequence
"""


def make_good_sequence(seq):

    set_seq = set(seq)

    map_set = {}
    for el in set_seq:
        map_set[el] = 0
    for el in seq:
        map_set[el] += 1

    count = 0
    for k, v in map_set.items():
        if k > v:
            seq = [val for val in seq if val != k]
            count += v
        if k < v:
            for j in range(v-k):
                seq.remove(k)
            count += (v-k)

    return seq, count


def good_sequence(seq) -> bool:

    set_seq = set(seq)

    map_set = {}
    for el in set_seq:
        map_set[el] = 0
    for el in seq:
        map_set[el] += 1
    for k, v in map_set.items():
        if k != v:
            return False
    print(map_set)

    return True

"""
A new e-mail service "Berlandesk" is going to be opened in Berland in the near future. The site administration wants
to launch their project as soon as possible, that's why they ask you to help. You're suggested to implement the
prototype of site registration system. The system should work on the following principle.

Each time a new user wants to register, he sends to the system a request with his name. If such a name does not
exist in the system database, it is inserted into the database, and the user gets the response OK, confirming the
successful registration. If the name already exists in the system database, the system makes up a new user name,
sends it to the user as a prompt and also inserts the prompt into the database. The new name is formed by the
following rule. Numbers, starting with 1, are appended one after another to name (name1, name2, ...), among these
numbers the least i is found so that namei does not yet exist in the database.

Input
The first line contains number n. The following n lines contain the requests to the system. Each request is a
non-empty line, and consists of not more than 32 characters, which are all lowercase Latin letters.

Output
Print n lines, which are system responses to the requests: OK in case of successful registration, or a prompt with
a new name, if the requested name is already taken.

"""


def generate_name(names, new_name) -> str:
    try:
        # list of all IDs associated with the key new_name, starts with 0
        id_list = names[new_name]
        counter = 0
        for i in sorted(id_list):
            if counter == i:
                counter += 1
        id_list.append(counter)
        names[new_name] = id_list
        return new_name+str(counter)
    except KeyError:
        names[new_name] = [0]
        return "OK"


def driver():
    names = {}
    new_name = "manoj"
    print(generate_name(names, new_name))
    print(names)
    new_name = "manoj"
    print(generate_name(names, new_name))
    print(names)
    new_name = "shubhi"
    print(generate_name(names, new_name))
    print(names)
    new_name = "manoj"
    print(generate_name(names, new_name))
    print(names)
    new_name = "shubhi"
    print(generate_name(names, new_name))
    print(names)


driver()
