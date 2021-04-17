def get_child_words(word, all_words, child_words):

    if len(word) == 0:
        return
    for val in itertools.combinations(word, len(word) - 1):
        smaller_word = ''.join(val)
        if smaller_word in all_words:
            child_words.append(smaller_word) if smaller_word not in child_words else child_words
            get_child_words(smaller_word, all_words, child_words)


def longest_word_with_words():
    """
    What is the longest English word, that remains a valid English word, as you remove its letters one at a time?
    Now, letters can be removed from either end, or the middle, but you can’t rearrange any of the letters.
    Every time you drop a letter, you wind up with another English word. If you do that, you’re eventually going to
    wind up with one letter and that too is going to be an English word—one that’s found in the dictionary. I want to
    know what’s the longest word and how many letters does it have?
    I’m going to give you a little modest example: Sprite. Ok? You start off with sprite, you take a letter off,
    one from the interior of the word, take the r away, and we’re left with the word spite, then we take the e off the
    end, we’re left with spit, we take the s off, we’re left with pit, it, and I.
    Write a program to find all words that can be reduced in this way, and then find the longest one.
    This exercise is a little more challenging than most, so here are some suggestions:
    You might want to write a function that takes a word and computes a list of all the words that can be formed by
    removing one letter. These are the “children” of the word.
    Recursively, a word is reducible if any of its children are reducible. As a base case, you can consider the
    empty string reducible.
    The wordlist I provided, words.txt, doesn’t contain single letter words. So you might want to add “I”, “a”,
    and the empty string.
    To improve the performance of your program, you might want to memorize the words that are known to be reducible.
    """
    words_dict = {}

    with open('words.txt', 'r') as fp:
        lines = fp.readlines()
        for ln in lines:
            words_dict[ln.strip()] = []

    for key in words_dict:
        child_words = []
        get_child_words(key, words_dict.keys(), child_words)
        if len(child_words) > 0:
            child_words.append(key)
            words_dict[key] = child_words

    words_to_remove = [key for key, val in words_dict.items() if len(val) <= 1]
    for empty_words in words_to_remove:
        del words_dict[empty_words]

    ordered_word_list = sorted(words_dict.values(), key=lambda x : len(x), reverse=True)
