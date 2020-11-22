# 두 리스트 합치기
# 오름차순으로 정렬이 된 두 리스트가 주어지면 두 리스트를 오름차순으로 합쳐 출력하는 프로
# 그램을 작성하세요.
# ▣ 입력설명
# 첫 번째 줄에 첫 번째 리스트의 크기 N(1<=N<=100)이 주어집니다.
# 두 번째 줄에 N개의 리스트 원소가 오름차순으로 주어집니다.
# 세 번째 줄에 두 번째 리스트의 크기 M(1<=M<=100)이 주어집니다.
# 네 번째 줄에 M개의 리스트 원소가 오름차순으로 주어집니다.
# 각 리스트의 원소는 int형 변수의 크기를 넘지 않습니다.
# ▣ 출력설명
# 오름차순으로 정렬된 리스트를 출력합니다.
# ▣ 입력예제 1
# 3
# 1 3 5
# 5
# 2 3 6 7 9
# ▣ 출력예제 1
# 1 2 3 3 5 6 7 9

import sys
# sys.stdin = open("input.txt", "rt")
N = int(input())
a = list(map(int, input().split()))
M = int(input())
b = list(map(int, input().split()))

p1 = p2 = 0
result = []

while p1 < N and p2 < M:
    if a[p1] > b[p2]:
        result.append(b[p2])
        p2 += 1

    else:
        result.append(a[p1])
        p1 += 1

if p1 < N:
    while p1 < N:
        result.append(a[p1])
        p1 += 1

if p2 < M:
    while p2 < M:
        result.append(b[p2])
        p2 += 1

for x in result:
    print(x, end=' ')