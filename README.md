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

```
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
```

is intended only to show the matching and nesting structure for tags in the language. Write a program that can check an HTML document for proper opening and closing tags.

*Two Stacks in an Array*
Describe a structure which provides two stacks with a single array as backup structure. Implement the Pop and Push operations.

*Queue ADT based problems*
1. Implementation of Queue ADT based on list with capacity management
2. Given M integers, task is to find the frequency of each number in the Queue.
3. Given an integer K and a queue of integers, we need to reverse the order of the first K elements of the queue, leaving the other elements in the same relative order. Only following standard operations are allowed on queue.
* enqueue(x) : Add an item x to rear of queue
* dequeue() : Remove an item from front of queue
* size() : Returns number of elements in queue.
* front() : Finds front item.
4. Sorting a Queue without extra space

*Dequeue ADT based problems*
1. Deque Implementation
* len(D)    number of elements
* D.appendleft( )   add to beginning
* D.append( )   add to end
* D.popleft( )  remove from beginning
* D.pop()   remove from end
* D.first( )    D[0]    access first element
* D.last( ) D[−1]   access last element
* D.clear( )    clear all contents
2. Recently, on the course of algorithms and data structures, Valeriy learned how to use a deque. He built a deque filled with 𝑛 elements. The 𝑖-th element is 𝑎𝑖 (𝑖 = 1,2,…,𝑛). He gradually takes the first two leftmost elements from the deque (let's call them 𝐴 and 𝐵, respectively), and then does the following: if 𝐴>𝐵, he writes 𝐴 to the beginning and writes 𝐵 to the end of the deque, otherwise, he writes to the beginning 𝐵, and 𝐴 writes to the end of the deque. We call this sequence of actions an operation.

For example, if deque was [2,3,4,5,1], on the operation he will write 𝐵=3 to the beginning and 𝐴=2 to the end, so he will get [3,4,5,1,2].
The teacher of the course, seeing Valeriy, who was passionate about his work, approached him and gave him 𝑞 queries. Each query consists of the singular number 𝑚𝑗 (𝑗=1,2,…,𝑞). It is required for each query to answer which two elements he will pull out on the 𝑚𝑗-th operation.
Note that the queries are independent and for each query the numbers 𝐴 and 𝐵 should be printed in the order in which they will be pulled out of the deque.

*Linked List - Operations and Some Problems*
1. A node class of Linked List
2. LinkedList class that starts with head and tail and keeps track of its size. The underlying storage is a list.
3. Add a node to list
4. Add a node to the left of list
5. Add a node to the right of list
6. Delete the head node
7. Delete the tail node
8. Delete the node being passed
9. Delete the first node with value v
10. Check if list is empty
11. Return the first element in list
12. Return the size of list
13. Return the head node
14. Cheeck if the list passed is same (has same values) as this node
15. String representation of the list
16. Driver code
17. Reverse Linked List (Recursive Solution)
18. Check if linked list is palindrome or not
19. Given a linked list containing 0s, 1s and 2s, sort linked list by doing a single traversal of it.
20. You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and  each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4) Output: 7 -> 0 -> 8

342 + 465 = 807

Make sure there are no trailing zeros in the output list. So, 7 -> 0 -> 8 -> 0 is not a valid response even though the value is still 807.

*Circular Linked List and a couple*
1. Implement Circular LinkedList with methods
* enqueue - Add an element to the back of queue.
* dequeue - Remove and return the first element of the queue (i.e., FIFO).
* rotate - Rotate front element to the back of the queue.
* first - Return (but do not remove) the element at the front of the queue.
* is_empty - Return True if the queue is empty
* delete_node - Delete a node with given value in Circular list
* delete_kth_node - Delete kth node in Circular list
* __len__ - Return the number of elements in the queue.
2. Split Circular Linked List Into Two Equal halves
3. In computer science and mathematics, the Josephus Problem (or Josephus permutation) is a theoretical problem. Following is the problem statement: There are n people standing in a circle waiting to be executed. The counting out begins at some point in the circle and proceeds around the circle in a fixed direction. In each step, a certain number of people are skipped and the next person is executed. The elimination proceeds around the circle (which is becoming smaller and smaller as the executed people are removed), until only the last person remains, who is given freedom. Given the total number of persons n and a number k which indicates that k-1 persons are skipped and kth person is killed in circle. The task is to choose the place in the initial circle so that you are the last one remaining and so survive.<br>
For example, if n = 5 and k = 2, then the safe position is 3. Firstly, the person at position 2 is killed, then person at position 4 is killed, then person at position 1 is killed. Finally, the person at position 5 is killed. So the person at position 3 survives.<br>
If n = 7 and k = 3, then the safe position is 4. The persons at positions 3, 6, 2, 7, 5, 1 are killed in order, and person at position 4 survives.

*Doubly Linked List*
1. A node class to represnet a node of a doubly linked list with references to previous and next
2. The doubly linked list class with references to nodes that are head and tail of the list
3. Add to the front of the list
4. Add after the node
5. Add before a node
6. Add to the end of the list
7. Delete a node from the list
8. Return an iterator to the list
9. Reverse the list using a generator
10. Return first element of the list
11. Return last element of the list
12. Rotate the list by n positions
13. Get the kth node in the list
14. The length of the list
15. String representation of the list
16. A class iterator using generator
17. A class to represent a player with a score
18. Driver code for the players in the doubly linked list fashion
19. Standard driver code
20. Given a doubly-linked list, the task is to swap Kth node from the beginning with Kth node from the ending.
21. Given a doubly-linked list and an integer N, the task is to rotate the linked list clockwise by N nodes.

