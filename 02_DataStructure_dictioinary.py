

#  키의 중복이 허용되지 않음


#  선언 및 초기화
#  변수명 = {키:값 }
cabinet = {3:"유재석", 100:"김태호"}
print(cabinet)
print(cabinet[3])
print(cabinet[100])
print(cabinet.get(3))


# 없는 키에 대한 출력
# print(cabinet[5])  #error code
print(cabinet.get(5))
print(cabinet.get(5, "available"))


# 키 유무 확인
# 리턴값은 bool
print(3 in cabinet)
print(5 in cabinet)



# 키를 String 으로 사용 가능
cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet.get("A-3"))


# 값 추가
cabinet["C-20"] = "조세호"
print(cabinet)


# 값 덮어쓰기
cabinet["A-3"] = "김종국"
print(cabinet)


# 값 지우기
del cabinet["C-20"]
print(cabinet)


# 키 값만 출력
print(cabinet.keys())


# 값 만 출력
print(cabinet.values)


# 키와 포함 값을 출력
print(cabinet.items())


# 모든항목 삭제
cabinet.clear()
print(cabinet)