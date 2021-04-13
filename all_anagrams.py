
def all_anagrams():
    """
    Write a program that reads a word list from a file  and prints all the sets of words that are anagrams.
    Here is an example of what the output might look like:

    ['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled']
    ['retainers', 'ternaries']
    ['generating', 'greatening']
    ['resmelts', 'smelters', 'termless']
    Hint: you might want to build a dictionary that maps from a set of letters to a list of words that can be spelled
    with those letters. The question is, how can you represent the set of letters in a way that can be used as a key?
    Modify the previous program so that it prints the largest set of anagrams first, followed by the second largest set,
    and so on.

    """
    anagram_map = {}
    with open('words.txt', 'r') as fp:
        lines = fp.readlines()
        for ln in lines:
            word_tup = tuple(sorted(ln.strip()))
            if word_tup in anagram_map.keys():
                anagram_map[word_tup].append(ln.strip())
            else:
                anagram_map[word_tup] = [ln.strip()]

    anagrams_list = sorted(anagram_map.values(), key=lambda x: len(x), reverse=True)
    return [x for x in anagrams_list if len(x) > 1]
