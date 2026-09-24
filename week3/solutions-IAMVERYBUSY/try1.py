import sys

input = sys.stdin.readline

def solve():
    T = int(input())
    for test in range(T):
        n = int(input())
        schedule = []
        for _ in range(n):
            a, b = map(int, input().split())
            schedule.append((a,b))
        schedule.sort(key=lambda x: x[1])

        free = schedule[0][1]
        count = 1
        for activity in schedule[1:]:
            if activity[0] >= free:
                free = activity[1]
                count += 1
            else:
                continue
        print(count)


if __name__ == "__main__":
    solve()