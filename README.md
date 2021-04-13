# Sample Python Code

*Sorted Insert*

Take in numbers as input until “stop” is entered. As you take in each number, insert it into a list so that the list is sorted in ascending order. That is, look through the list until you find the place where the new element belongs, then use .insert() to place it there. If the number is already in the list, do not add it again. After “stop” is entered, print out the list. Do not use any of Python’s built-in sorting functions.

*Frequency of letters*

Write a program that reads a file and prints the letters in decreasing order of frequency. Your program should convert all the input to lower case and only count the letters a-z. Your program should not count spaces, digits, punctuation, or anything other than the letters a-z. Find text samples from several different languages and see how letter frequency varies between languages. Compare your results with the tables at [wikipedia.org/wiki/Letter_frequencies](wikipedia.org/wiki/Letter_frequencies)

*All Anagrams*

Write a program that reads a word list from a file  and prints all the sets of words that are anagrams. Here is an example of what the output might look like:

- 'deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled'
- 'retainers', 'ternaries'
- 'generating', 'greatening'
- 'resmelts', 'smelters', 'termless'

Hint: you might want to build a dictionary that maps from a set of letters to a list of words that can be spelled with those letters. The question is, how can you represent the set of letters in a way that can be used as a key? Modify the previous program so that it prints the largest set of anagrams first, followed by the second largest set, and so on.
