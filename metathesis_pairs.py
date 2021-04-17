import itertools


def metathesis_pairs():
    """
    Two words form a “metathesis pair” if you can transform one into the other by swapping two letters; for example,
    “converse” and “conserve.” Write a program that finds all of the metathesis pairs in the dictionary.
    Hint: don’t test all pairs of words, and don’t test all possible swaps.
    """
    metathesis_pair_list = []
    for anagram_list in all_anagrams():
        for pair in itertools.combinations(anagram_list, 2):
            # in this pair, zip the two strings, find the pairs that are different
            is_metathesis = True
            zipped_pairs = list(zip(pair[0], pair[1]))
            for tup in zipped_pairs:
                if tup[0] != tup[1] and (tup[1], tup[0]) not in zipped_pairs:
                    is_metathesis = False
                    break
            if is_metathesis:
                metathesis_pair_list.append((pair[0], pair[1]))

    print(metathesis_pair_list)
    return metathesis_pair_list
