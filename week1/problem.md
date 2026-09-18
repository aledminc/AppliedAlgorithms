# Stable Matching

## Problem

There are $n$ men and $n$ women. Each person ranks every member of the opposite group in order of preference.

Find $n$ marriages such that no man and woman prefer each other over their current partners. A stable solution always exists.

## Input

The first line contains an integer $t$ ($1 \le t \le 100$), the number of test cases.

For each test case:

- The first line contains an integer $n$ ($1 \le n \le 500$).
- The next $n$ lines contain the women's preferences. Each line begins with the woman's number, followed by the numbers of all men in order of preference.
- The next $n$ lines contain the men's preferences in the same format.

## Output

For each test case, print $n$ lines. Each line should contain two integers $m$ and $w$, indicating that man $m$ marries woman $w$.

## Example

### Input

```text
2
4
1 4 3 1 2
2 2 1 3 4
3 1 3 4 2
4 4 3 1 2
1 3 2 4 1
2 2 3 1 4
3 3 1 2 4
4 3 2 4 1
7
1 3 4 2 1 6 7 5
2 6 4 2 3 5 1 7
3 6 3 5 7 2 4 1
4 1 6 3 2 4 7 5
5 1 6 5 3 4 7 2
6 1 7 3 4 5 6 2
7 5 6 2 4 3 7 1
1 4 5 3 7 2 6 1
2 5 6 4 7 3 2 1
3 1 6 5 4 3 7 2
4 3 5 6 7 2 4 1
5 1 7 6 4 3 5 2
6 6 3 7 5 2 4 1
7 1 7 4 2 6 5 3
```

### Output

```text
1 3
2 2
3 1
4 4
1 4
2 5
3 1
4 3
5 7
6 6
7 2
```
