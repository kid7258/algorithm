import sys
# sys.stdin = open("input.txt", "rt")
K, N = map(int, input().split())
a = []
for _ in range(K):
    a.append(int(input()))

lt = 0
rt = max(a)
res = 0
while lt <= rt:
    mid = (lt + rt) // 2
    cnt = 0
    for x in a:
        cnt += x // mid

    if cnt >= N:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(res)