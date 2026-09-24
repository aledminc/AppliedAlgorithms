from collections import defaultdict, deque
import sys

input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())

    graph = defaultdict(list)
    indgr = [0]*(n+1)

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        indgr[b] += 1

    q = deque()
    order = []

    for course in range(1, n+1):
        if indgr[course] == 0:
            q.append(course)

    while q:
        cur = q.popleft()
        order.append(cur)
        for nbr in graph[cur]:
            indgr[nbr] -= 1
            if indgr[nbr] == 0:
                q.append(nbr)

    if len(order) == n:
        print(*order)
    else:
        print("IMPOSSIBLE")


if __name__ == "__main__":
    solve()