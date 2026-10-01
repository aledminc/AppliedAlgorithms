import sys
import heapq

input = sys.stdin.readline

def solve():
    n = int(input())

    times = []

    for i in range(n):
        a, b = map(int, input().split())
        times.append((a, b, i))

    times.sort()
    allocation = [0] * n
    heap = []

    num_room = 0
    for arrival, departure, i in times:
        if heap and heap[0][0] < arrival:
            end, room = heapq.heappop(heap)
        else:
            num_room += 1
            room = num_room

        heapq.heappush(heap, (departure, room))
        allocation[i] = room

    print(num_room)
    print(*allocation)

if __name__ == "__main__":
    solve()