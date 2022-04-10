

import sys

# print("python", "java", sep=',', end='?')
# print('new line')

# 일반 시스템 출력
print("python", "java", file=sys.stdout)
# 시스템 에러 출력
print("python", "java", file=sys.stderr)


# 줄맞춤 예제
scores = {"math":0, "english":50, "coding":100}
for sub, score in scores.items():
    # print(sub, score)
    print(sub.ljust(8), str(score).rjust(4), sep=':')
    

# 0으로 자리 채우기 예제

for num in range(1, 21):
    print("wating number : " + str(num).zfill(3))



# 일반 입력
ans = input("input : ")
print('echo :' + ans)

# input()함수는 숫자도 str 형식으로 받는다
print(type(ans))