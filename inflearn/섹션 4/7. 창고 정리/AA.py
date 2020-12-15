import sys
# sys.stdin = open("input.txt", "rt")
n = int(input())
stack = list(map(int, input().split()))
m = int(input())

stack.sort()
for _ in range(m):
    stack[0] += 1
    stack[n-1] -= 1
    stack.sort()

print(stack[n-1] - stack[0])