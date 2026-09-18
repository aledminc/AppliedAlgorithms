# Round Trip

## Problem

Byteland has $n$ cities and $m$ roads between them. Find a round trip that starts in a city, visits at least two other distinct cities, and returns to the starting city.

## Input

The first line contains two integers $n$ and $m$, the number of cities and roads. The cities are numbered from $1$ to $n$.

The next $m$ lines each contain two integers $a$ and $b$, indicating that there is a road between cities $a$ and $b$.

Every road connects two different cities, and there is at most one road between any pair of cities.

## Output

First, print an integer $k$, the number of cities on the route. Then print the $k$ cities in the order they are visited. The starting city should appear at both the beginning and end of the route.

You may print any valid solution. If no round trip exists, print `IMPOSSIBLE`.

## Constraints

- $1 \le n \le 10^5$
- $1 \le m \le 2 \cdot 10^5$
- $1 \le a, b \le n$

## Example

### Input

```text
5 6
1 3
1 2
5 3
1 5
2 4
4 5
```

### Output

```text
4
3 5 1 3
```

# Message Route

## Problem

Syrjala's network has $n$ computers and $m$ connections. Find whether Uolevi can send a message from computer $1$ to Maija's computer $n$. If possible, find a route that uses the minimum number of computers.

## Input

The first line contains two integers $n$ and $m$, the number of computers and connections. The computers are numbered from $1$ to $n$.

The next $m$ lines each contain two integers $a$ and $b$, indicating that there is a connection between computers $a$ and $b$.

Every connection joins two different computers, and there is at most one connection between any pair of computers.

## Output

If a route exists, first print an integer $k$, the minimum number of computers on the route. Then print the $k$ computers in the order they are visited.

You may print any shortest route. If no route exists, print `IMPOSSIBLE`.

## Constraints

- $2 \le n \le 10^5$
- $1 \le m \le 2 \cdot 10^5$
- $1 \le a, b \le n$

## Example

### Input

```text
5 5
1 2
1 3
1 4
2 3
5 4
```

### Output

```text
3
1 4 5
```
