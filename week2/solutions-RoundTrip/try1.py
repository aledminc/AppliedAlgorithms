import sys
from collections import defaultdict

input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())

    mapping = defaultdict(list)

    for _ in range(m):
        a, b = map(int, input().split())
        mapping[a].append(b)
        mapping[b].append(a)

    visited = set()
    parent = {}

    for start in range(1, n + 1):
        if start not in visited:
            parent[start] = -1
            cycle = dfs(start, visited, mapping, parent)
            if cycle:
                print(len(cycle))
                print(*cycle)
                return

    print("IMPOSSIBLE")

def dfs(node, visited, mapping, parent):

    visited.add(node)
    active = {node}
    stack = [(node, 0)]

    while stack:
        node, next_nbr = stack[-1]

        if next_nbr == len(mapping[node]):
            active.remove(node)
            stack.pop()
            continue

        nbr = mapping[node][next_nbr]
        stack[-1] = (node, next_nbr + 1)

        if nbr not in visited:
            parent[nbr] = node
            visited.add(nbr)
            active.add(nbr)
            stack.append((nbr, 0))
        elif nbr in active and parent[node] != nbr:
            cycle = [nbr, node]
            cur = parent[node]
            while cur != nbr:
                cycle.append(cur)
                cur = parent[cur]
            cycle.append(nbr)
            cycle.reverse()
            return cycle
    return None

if __name__ == "__main__":
    solve()
