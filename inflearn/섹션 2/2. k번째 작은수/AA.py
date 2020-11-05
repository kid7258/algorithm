# K번째 작은수
# N개의 숫자로 이루어진 숫자열이 주어지면 해당 숫자열중에서 s번째부터 e번째 까지의 수 중
# k번째로 작은 수를 출력하는 프로그램을 작성하세요.
# ▣ 입력설명
# 첫 번째 줄에 테스트 케이스 T(1<=T<=10)이 주어집니다.
# 각 케이스별
# 첫 번째 줄은 자연수 N(5<=N<=500), s, e, k가 차례로 주어진다.
# 두 번째 줄에 N개의 숫자가 차례로 주어진다.
# ▣ 출력설명
# 각 케이스별 k번째 수를 아래 출력예제와 같이 출력하세요.
# ▣ 입력예제 1
# 2
# 6 2 5 3
# 5 2 7 3 8 9
# 15 3 10 3
# 4 15 8 16 6 6 17 3 10 11 18 7 14 7 15
# ▣ 출력예제 1
# 1 7
# 2 6
# 입력예제1 해설 : 2 7 3 8의 숫자 중 3번째로 작은 수는 7이다.


import sys

# sys.stdin = open("input.txt", "rt")
T = int(input())
for i in range(T):
    N, s, e, k = map(int, input().split())
    a=list(map(int, input().split()))
    a=a[s-1:e]
    a.sort()
    for idx, j in enumerate(a):
        if idx + 1 == k:
            print("#{0} {1}".format(i+1, j))

# import sys
# sys.stdin=open("input.txt", "r")
# T=int(input())
# for t in range(T):
#     n, s, e, k=map(int, input().split())
#     a=list(map(int, input().split()))
#     a=a[s-1:e]
#     a.sort()
#     print("#%d %d" %(t+1, a[k-1]))