# Print All Pairs

## Problem Statement

Given `N` elements, print every possible ordered pair `(Ai, Aj)` where `i < j`.

## Input Format

```text
N
A1 A2 ... AN
```

## Output Format

Print each pair on a separate line.

## Constraints

`2 ≤ N ≤ 100`

## Sample Test Cases

### TC 1

**Input**

```text
3
1 2 3
```

**Output**

```text
(1,2)
(1,3)
(2,3)
```

### TC 2

**Input**

```text
2
5 10
```

**Output**

```text
(5,10)
```

### TC 3

**Input**

```text
4
1 2 3 4
```

**Output**

```text
(1,2)
(1,3)
(1,4)
(2,3)
(2,4)
(3,4)
```

## Time complexity:
- The nested loops generate all pairs (i, j) with i < j for an array of size n.
- Number of iterations is n(n-1)/2, so time complexity is O(n^2).

## Space complexity:
- The array stores n integers, plus a constant amount of extra space for loop indices and temporary tuple in print.
- Overall auxiliary space is O(n) (the input array). If counting additional space beyond input, it’s O(1).