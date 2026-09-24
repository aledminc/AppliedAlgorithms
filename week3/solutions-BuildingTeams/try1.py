from collections import defaultdict, deque
import sys

input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())

    graph = defaultdict(list)

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    group = [0]*(n+1)

    for friend in range(1, n+1):
        if group[friend] != 0:
            continue
        group[friend] = 1
        q = deque([friend])
        while q:
            cur = q.popleft()
            for nbr in graph[cur]:
                if group[nbr] == 0:
                    group[nbr] = 3 - group[cur]
                    q.append(nbr)
                elif group[nbr] == group[cur]:
                    print("IMPOSSIBLE")
                    return
                
    print(*group[1:])


if __name__ == "__main__":
    solve()