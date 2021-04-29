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

*Metathesis Pairs*

Two words form a “metathesis pair” if you can transform one into the other by swapping two letters; for example, “converse” and “conserve.” Write a program that finds all of the metathesis pairs in the dictionary.
Hint: don’t test all pairs of words, and don’t test all possible swaps.

*Longest Word With Words*

What is the longest English word, that remains a valid English word, as you remove its letters one at a time? Now, letters can be removed from either end, or the middle, but you can’t rearrange any of the letters. Every time you drop a letter, you wind up with another English word. If you do that, you’re eventually going to wind up with one letter and that too is going to be an English word—one that’s found in the dictionary. I want to know what’s the longest word and how many letters does it have? I’m going to give you a little modest example: Sprite. Ok? You start off with sprite, you take a letter off, one from the interior of the word, take the r away, and we’re left with the word spite, then we take the e off the end, we’re left with spit, we take the s off, we’re left with pit, it, and I.
Write a program to find all words that can be reduced in this way, and then find the longest one. This exercise is a little more challenging than most, so here are some suggestions: You might want to write a function that takes a word and computes a list of all the words that can be formed by removing one letter. These are the “children” of the word. Recursively, a word is reducible if any of its children are reducible. As a base case, you can consider the empty string reducible. The wordlist I provided, words.txt, doesn’t contain single letter words. So you might want to add “I”, “a”, and the empty string.
To improve the performance of your program, you might want to memorize the words that are known to be reducible.

*Recursion*

1. Given n of 1 or more, return the factorial of n, which is n * (n-1) * (n-2) ... 1. Compute the result recursively (without loops).
2. We have a number of bunnies and each bunny has two big floppy ears. We want to compute the total number of ears across all the bunnies recursively (without loops or multiplication).
3. We have bunnies standing in a line, numbered 1, 2, ... The odd bunnies (1, 3, ..) have the normal 2 ears. The even bunnies (2, 4, ..) we'll say have 3 ears, because they each have a raised foot. Recursively return the number of "ears" in the bunny line 1, 2, ... n (without loops or multiplication).
4. Given a non-negative int n, return the count of the occurrences of 7 as a digit, so for example 717 yields 2. (no loops)
5. Given a string, compute recursively (no loops) the number of lowercase 'x' chars in the string.
6. Given a string, compute recursively (no loops) the number of times lowercase "hi" appears in the string.
7. Given a string, compute recursively (no loops) a new string where all appearances of "pi" have been replaced by "3.14".
8. Given an array of ints, compute recursively the number of times that the value 11 appears in the array. We'll use the convention of considering only the part of the array that begins at the given index. In this way, a recursive call can pass index+1 to move down the array. The initial call will pass in index as 0.
9. Given a string, compute recursively a new string where identical chars that are adjacent in the original string are separated from each other by a "*".
10. Count recursively the total number of "abc" substrings that appear in the given string.
11. Given a string, compute recursively the number of times lowercase "hi" appears in the string, however do not count "hi" that have an 'x' immedately before them.
12. Given a string and a non-empty substring sub, compute recursively the number of times that sub appears in the string, without the sub strings overlapping.
13. We have triangle made of blocks. The topmost row has 1 block, the next row down has 2 blocks, the next row has 3 blocks, and so on. Compute recursively (no loops or multiplication) the total number of blocks in such a triangle with the given number of rows.
14. Given a non-negative int n, compute recursively (no loops) the count of the occurrences of 8 as a digit, except that an 8 with another 8 immediately to its left counts double, so 8818 yields 4.

*More Recusrion*

1. Given a string, compute recursively a new string where all the 'x' chars have been removed.
2. Given a string, compute recursively a new string where all the lowercase 'x' chars have been moved to the end of the string.
3. Given a string that contains a single pair of parenthesis, compute recursively a new string made of only of the parenthesis and their contents, so "xyz(abc)123" yields "(abc)". Assume that there is indeed a single pair of parenthesis
4. Given a string and a non-empty substring sub, compute recursively if at least n copies of sub appear in the string somewhere, possibly with overlapping. N will be non-negative.
5. The fibonacci sequence is a famous bit of mathematics, and it happens to have a recursive definition. The first two values in the sequence are 0 and 1 (essentially 2 base cases). Each subsequent value is the sum of the previous two values, so the whole sequence is: 0, 1, 1, 2, 3, 5, 8, 13, 21 and so on. Define a recursive fibonacci(n) method that returns the nth fibonacci number, with n=0 representing the start of the sequence.
6. Given a non-negative int n, return the sum of its digits recursively (no loops).
7. Given base and n that are both 1 or more, compute recursively (no loops) the value of base to the n power, so powerN(3, 2) is 9 (3 squared)
8. Given a string, compute recursively (no loops) a new string where all the lowercase 'x' chars have been changed to 'y' chars.
9. Given an array of ints, compute recursively if the array contains a 6.
10. Given a string, compute recursively a new string where all the adjacent chars are now separated by a "*".
11. We'll say that a "pair" in a string is two instances of a char separated by a char. So "AxA" the A's make a pair. Pair's can overlap, so "AxAxA" contains 3 pairs -- 2 for A and 1 for x. Recursively compute the number of pairs in the given string.
12. Given a string and a non-empty substring sub, compute recursively the largest substring which starts and ends with sub and return its length.
13. Given a string, return recursively a "cleaned" string where adjacent chars that are the same have been reduced to a single char. So "yyzzza" yields "yza".
14. Given a string, return true if it is a nesting of zero or more pairs of parenthesis, like "(())" or "((()))". Suggestion: check the first and last chars, and then recur on what's inside them.
15. Given an array of ints, compute recursively if the array contains somewhere a value followed in the array by that value times 10. We'll use the convention of considering only the part of the array that begins at the given index. In this way, a recursive call can pass index+1 to move down the array. The initial call will pass in index as 0.

*Stack and related problems*

1. Placeholder for exception when the stack is empty
2. A stak ADT implementation  based on a list
  * push to stack
  * pop from stack
  * is stack empty
  * return the top of stack, without popping the element
  * return size of the stack
  * string representation of stack elements
3. Here is a technique that employs two stacks in order to determine if a phrase is a palindrome, that is, reads the same forward and backward (for example, the word “rotator'” is a palindrome, as is the string “rats live on no evil star”). Read the characters one by one and transfer them into a stack. The characters in  the stack will then represent the reversed word. Once all characters have been read, transfer half the characters from the first stack into a second stack. Thus, the order of the words will have been restored. If there were an odd number of characters, remove one further character from the original stack. Finally, test the two stacks for equality, element by element. If they are the same, then the word is a palindrome. Write a procedure that takes a String argument and tests to see if it is a palindrome using this algorithm.
4. Give a recursive implementation of the client-side function int stack_size(stack_t S); that takes as input a stack S and returns the number of elements in it. Upon returning, the input stack should contain the same elements in the same order as when it was called.
5. Implement the function void stack_sort(stack_t S); that sorts its input stack in-place. The resulting stack should be sorted in ascending order, with the largest item at the top and the smallest at the bottom. Your code may use temporary stacks but no other data structures. You may use any function on stack interface. Hint an effective way to solve this exercise is carefully consider what loop invariants should hold at various points.
6. Another example of the parentheses matching problem comes from hypertext markup language (HTML). In HTML, tags exist in both opening and closing forms and must be balanced to properly describe a web document. This very simple HTML document:

 <html>
    <head>
       <title>
          Example
       </title>
    </head>

    <body>
       <h1>Hello, world</h1>
    </body>
 </html>
is intended only to show the matching and nesting structure for tags in the language. Write a program that can check an HTML document for proper opening and closing tags.

