import sys
# sys.stdin = open("input.txt", "rt")
n, m = map(int, input().split())
people = list(map(int, input().split()))
people.sort()

s = 0
e = n-1
cnt = 0
while people:
    if len(people) == 1:
        cnt += 1
        break

    if people[s] + people[e] > m:
        people.pop()
        cnt += 1
        e -= 1
    else:
        people.pop(0)
        people.pop()
        cnt += 1
        e -= 2

print(cnt)