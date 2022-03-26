


# 기본 for 문
for waiting_num in [0, 1 , 2, 3, 4]:
    print("대기번호 : {0}".format(waiting_num))


# 범위를 지정하여 반복
for waiting_num in range(100):
    print("대기번호 : {0}".format(waiting_num))


starbucks = ["아이언맨", "토르", "캡아"]
for customer in starbucks:
    print(f"대기번호 : {customer}")

# 한줄로 요약
students = range(5)
students = [i + 100 for i in students]

students = ["Iron Man", "Thor", "groot"]
students = [i.upper() for i in students]
print(students)
