import sys

input = sys.stdin.readline

def solve():
    n = int(input())

    times = []

    for line in range(n):
        times.append(tuple(map(int, input().split())))

    times.sort(key=lambda x: x[0])

    # rooms[room number] = next available time
    # n keys for maximum n rooms needed worst case
    rooms = {}

    for i in range(1, n+1):
        rooms[i] = 0

    allocation = []
    for customer in times:
        #print(f"customer needs room at {customer[0]}")
        for room in rooms:
            #print(f"room {room} open at {rooms[room]}")
            if rooms[room] < customer[0]:
                #print("ACCEPT")
                rooms[room] = customer[1]
                allocation.append(room)
                break
            #print("REJECT")

    print(len(set(allocation)))
    print(*allocation)

if __name__ == "__main__":
    solve()