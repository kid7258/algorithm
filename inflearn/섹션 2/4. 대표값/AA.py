# 대표값
# N명의 학생의 수학성적이 주어집니다. N명의 학생들의 평균(소수 첫째자리 반올림)을 구하고,
# N명의 학생 중 평균에 가장 가까운 학생은 몇 번째 학생인지 출력하는 프로그램을 작성하세요.
# 답이 2개일 경우 성적이 높은 학생의 번호를 출력하세요. 만약 답이 되는 점수가 여러 개일 경우 번호가 빠른 학생의 번호를 답으로 한다.
# ▣ 입력설명
# 첫줄에 자연수 N(5<=N<=100)이 주어지고, 두 번째 줄에는 N개의 자연수가 주어진다.
# 학생의 번호는 앞에서부터 1로 시작해서 N까지이다.
# ▣ 출력설명
# 첫줄에 평균과 평균에 가장 가까운 학생의 번호를 출력한다.
# 평균은 소수 첫째 자리에서 반올림합니다.
# ▣ 입력예제 1
# 10
# 65 73 66 87 92 67 55 79 75 80
# ▣ 출력예제 1
# 74 9

import sys
N = int(input())
a = list(map(int, input().split()))

avg = round(sum(a) / N)
min = max(a)
score, answer = 0, 0

for i, x in enumerate(a):
    tmp = abs(avg - x)
    if tmp < min:
        min = tmp
        score = x
        answer = i + 1

    elif tmp == min:
        if x > score:
            score = x
            answer = i + 1

print(avg, answer)