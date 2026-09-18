import sys
input = sys.stdin.readline

def solve():
    tests = int(input())

    for _ in range(tests):
        people = int(input())

        women = {}

        for _ in range(people):
            row = list(map(int, input().split()))
            women[row[0]] = row[1:]

        men = {}

        for _ in range(people):
            row = list(map(int, input().split()))
            men[row[0]] = row[1:]

        match = {}
        single = list(men.keys())

        while single:
            man = single.pop(0)
            best_match = men[man][0]

            if best_match not in match:
                match[best_match] = man

            else:
                current_man = match[best_match]

                if women[best_match].index(man) < women[best_match].index(current_man):
                    match[best_match] = man

                    men[current_man] = men[current_man][1:]
                    single.append(current_man)

                else:
                    men[man] = men[man][1:]
                    single.append(man)

        for woman in match:
            print(match[woman], woman)
            

if __name__ == "__main__":
    solve()