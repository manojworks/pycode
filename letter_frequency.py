def letter_frequency():
    """
    Write a program that reads a file and prints the letters in decreasing order of frequency. Your program should
    convert all the input to lower case and only count the letters a-z. Your program should not count spaces, digits,
    punctuation, or anything other than the letters a-z. Find text samples from several different languages and see how
    letter frequency varies between languages. Compare your results with the tables at
    wikipedia.org/wiki/Letter_frequencies.
    
    """
    letter_count = []
    for i in range(26):
        letter_count.append((chr(i + ord('a')), 0))
    with open('words.txt', 'r') as fp:
        lines = fp.readlines()
        for ln in lines:
            for ch in ln.strip():
                if ch.isalpha():
                    val = letter_count[ord(ch.lower()) - ord('a')]
                    letter_count[ord(ch.lower()) - ord('a')] = (val[0], val[1] + 1)

    letter_count = sorted(letter_count, key=lambda x: x[1], reverse=True)
    for i in range(26):
        print(letter_count[i])
