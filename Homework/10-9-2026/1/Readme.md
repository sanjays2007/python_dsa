# Reverse the Student ID

## Problem Statement

A college stores a student's ID as a string. Reverse the ID without changing the characters.

## Input Format

A single string `S`

## Output Format

Print the reversed string.

## Constraints

`1 ≤ |S| ≤ 100`

## Sample Test Cases

### TC 1

**Input**

```text
12345
```

**Output**

```text
54321
```

### TC 2

**Input**

```text
ABC123
```

**Output**

```text
321CBA
```

### TC 3

**Input**

```text
A
```

**Output**

```text
A
```

## Time Complexity:
- O(n), where n is the length of the input string. Each character is swapped once, so the loop runs floor(n/2) iterations.
## Space Complexity:
- O(1) extra space, aside from the input string list and a few variables. The reversal is done in place.