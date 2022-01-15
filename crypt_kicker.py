Crypt Kicker

A common but insecure method of encrypting text is to permute the letters of the alphabet. In other words, each
letter of the alphabet is consistently replaced in the text by some other letter. To ensure that the encryption is
reversible, no two letters are replaced by the same letter.
Your task is to decrypt several encoded lines of text, assuming that each line uses a different set of replacements,
and that all words in the decrypted text are from a dictionary of known words.

Input
The input consists of a line containing an integer n, followed by n lowercase words, one per line, in alphabetical
order. These n words compose the dictionary of words which may appear in the decrypted text. Following the dictionary
are several lines of input. Each line is encrypted as described above.

There are no more than 1,000 words in the dictionary. No word exceeds 16 letters. The encrypted lines contain only
lower case letters and spaces and do not exceed 80 characters in length.

Output
Decrypt each line and print it to standard output. If there are multiple solutions, any one will do. If there is no
solution, replace every letter of the alphabet by an asterisk.

Sample Input
6
and
dick
jane
puff
spot
yertle
bjvg xsb hxsn xsb qymm xsb rqat xsb pnetfn
xxxx yyy zzzz www yyyy aaa bbbb ccc dddddd

Sample Output
dick and jane and puff and spot and yertle
**** *** **** *** **** *** **** *** ******

"""

import itertools

valid_words = ["and", "dick", "jane", "puff", "spot", "yertle"]


def words_with_length(w_len) -> list:
    return [wrd for wrd in valid_words if len(wrd) == w_len]


# "bjvg xsb hxsn xsb qymm xsb rqat xsb pnetfn"
def decrypt(s) -> list:
    decoded = []
    char_map = make_char_map(s)
    words = s.split()
    for w in words:
        probable_new_words = list(char_map[w[0]])
        for ind in range(1, len(w)):
            t = char_map[w[ind]]
            word_part = ["".join(x) for x in itertools.product(probable_new_words, t)]
            probable_new_words = list(word_part)

        words_here = [word for word in probable_new_words if word in words_with_length(len(w))]
        if len(words_here) == 0:
            words_here.append('*' * len(w))
        decoded.append(words_here)

    return decoded


def make_char_map(s) -> dict:
    probable_char_map = {}
    tokens = s.split()
    tokens.sort(key=len)
    for w in tokens:
        w_len = len(w)
        same_len_words = words_with_length(w_len)
        for i, ch in enumerate(w):
            same_len_set = set(val[i] for val in same_len_words)
            if ch not in probable_char_map.keys():
                probable_char_map[ch] = same_len_set
            else:
                curr_set = probable_char_map[ch]
                curr_set = curr_set.intersection(same_len_set)
                probable_char_map[ch] = curr_set

    resolved_ch = set([next(iter(val)) for val in probable_char_map.values() if len(val) == 1])

    for k, v in probable_char_map.items():
        if len(v) > 1:
            v = v.difference(resolved_ch)
            probable_char_map[k] = v
            if len(v) == 1:
                resolved_ch.add(next(iter(v)))

    char_map = {}
    for k, v in probable_char_map.items():
        char_map[k] = tuple(v)

    return char_map


def crypt_kicker():
    s1 = "bjvg xsb hxsn xsb qymm xsb rqat xsb pnetfn"
    #print(decrypt(s1))
    s2 = "xxxx yyy zzzz www yyyy aaa bbbb ccc dddddd"
    print(decrypt(s2))


crypt_kicker()
