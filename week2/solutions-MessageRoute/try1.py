import sys
from collections import deque

input = sys.stdin.readline

def solve():

    param = list(map(int, input().split()))
    start = 1
    target = param[0]
    mapping = {}

    for edge in range(param[1]):
        a, b = map(int, input().split())
        mapping.setdefault(a, []).append(b)
        mapping.setdefault(b, []).append(a)

    queue = deque([start])
    visited = {start}
    parent = {start: None}

    while queue:
        node = queue.popleft()
        if node == target:
            break

        for nbr in mapping.get(node, []):
            if nbr not in visited:
                visited.add(nbr)
                parent[nbr] = node
                queue.append(nbr)

    if target not in parent:
        print("IMPOSSIBLE")
        return

    path = []
    cur = target

    while cur is not None:
        path.append(cur)
        cur = parent[cur]

    path.reverse()

    print(len(path))
    print(*path)


if __name__ == "__main__":
    solve()