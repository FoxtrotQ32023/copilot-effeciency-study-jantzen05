# __String Multimatching__

## __Input__
The input (_stringmultimatching.in_) consists of at most ten test cases.  
Each test case begins with an integer n on a line of its own, indicating the number of patterns. Then follow _n_ lines, each containing a non-empty pattern.  
The total length of all patterns in a test case is no more than 100.000.  
Then comes a line containing a non-empty text (of length at most 200.000).  
Input is terminated by end-of-file

### In other words.  
The input consist of a number of test cases.  
- Each test case begins with a number on it's own line.  
- The number represents the number of search terms.  
- The next number of lines are the search term, which cannot be empty lines.

```
Example input:
      2          <-- Number of search terms
      p          <-- First search term
      pup        <-- Second search term
      popup      <-- Line to search in
```

## __Output__
For each test case, output n lines, where the _i_’th line contains the positions of all the occurrences of the _i_’th pattern in text, from first to last, separated by a single space.

### In other word
Output format
```
Example output (0 based array):
      2 4        <-- Index positions for the first search term "p", separated with space 
      2          <-- Index position for the second search term "pup" 
```

## __Sample Input 1__

```
2
p
pup
Popup
2
You
peek a boo
you speek a bootiful language
4
anas
ana
an
a
bananananaspaj
```

## __Sample Output 1__

```
2 4
2

5
7
1 3 5 7
1 3 5 7
1 3 5 7 9 12
```