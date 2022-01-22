"""

Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all
the original letters exactly once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.

"""


def group_anagrams(s):
    distinct_sets = set([tuple(sorted(w)) for w in s])
    word_map = {k: None for k in distinct_sets}
    for el in s:
        anagrams = word_map[tuple(sorted(el))]
        if anagrams is None:
            anagrams = []
        anagrams.append("".join(el))
        word_map[tuple(sorted(el))] = anagrams

    print(word_map.values())


# group_anagrams(["eat","tea","tan","ate","nat","bat"])
# group_anagrams([""])
# group_anagrams(["a"])

import random

"""
Design and Implement Tic Tac Toe
"""


class TicTacToe:

    def __init__(self, p1, p2):
        self._board = [[None, None, None]] * 3
        self.P1 = p1
        self.P2 = p2

    def move(self, p, x, y) -> bool:
        if 1 <= x <= 3 and 1 <= y <= 3:
            print("player {} valid coordinates x={} and y={}".format(p, x, y))
        else:
            print("invalid coordinates x={} and y={} for player {}".format(x, y, p))
            return False

        if p == self.P1 or p == self.P2:
            return self._apply_move(p, x, y)
        else:
            print("Invalid player {}: play with X or O".format(p))
            return False

    def _apply_move(self, p, x, y) -> bool:
        if self._board[x - 1][y - 1] is None:
            in_list = [val for val in self._board[x - 1]]
            in_list[y - 1] = p
            self._board[x - 1] = in_list
            return True
        else:
            print("invalid move for player {} at x={}, y={}. slot is already occupied".format(p, x, y))
            return False

    def game_state(self, p):

        found = False
        for i in range(3):
            found = False
            for j in range(3):
                if self._board[i][j] is None:
                    found = True
                    break
            if found:
                break

        if not found:
            return "D"

        if self._board[0][0] == p and self._board[0][1] == p and self._board[0][2] == p:
            return p
        if self._board[1][0] == p and self._board[1][1] == p and self._board[1][2] == p:
            return p
        if self._board[2][0] == p and self._board[2][1] == p and self._board[2][2] == p:
            return p
        if self._board[0][0] == p and self._board[1][0] == p and self._board[2][0] == p:
            return p
        if self._board[0][1] == p and self._board[1][1] == p and self._board[2][1] == p:
            return p
        if self._board[0][2] == p and self._board[1][2] == p and self._board[2][2] == p:
            return p
        if self._board[0][0] == p and self._board[1][1] == p and self._board[2][2] == p:
            return p
        if self._board[0][2] == p and self._board[1][1] == p and self._board[2][0] == p:
            return p

        return None

    def __str__(self):
        ret_str = ""
        for i in range(3):
            for j in range(3):
                if self._board[i][j] is not None:
                    ret_str += self._board[i][j]
                else:
                    ret_str += "E"
            ret_str += "\n"
        return ret_str


def play():
    p1 = 'X'
    p2 = 'O'

    ttt = TicTacToe(p1, p2)

    while True:
        while not ttt.move(p1, random.randint(1, 3), random.randint(1, 3)):
            pass
        if ttt.game_state(p1) == p1:
            print(ttt)
            print("p1 wins")
            break
        elif ttt.game_state(p1) == 'D':
            print(ttt)
            print("game draw")
            break
        while not ttt.move(p2, random.randint(1, 3), random.randint(1, 3)):
            pass
        if ttt.game_state(p2) == p2:
            print(ttt)
            print("p2 wins")
            break
        elif ttt.game_state(p2) == 'D':
            print(ttt)
            print("game draw")
            break


play()
