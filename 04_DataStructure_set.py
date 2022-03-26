

# 집합
# 중복 불가, 순서가 없음


# 초기화
from traceback import print_tb


sets = {1, 2, 3, 3, 3}
print(set)


# 교집합
java = {"유재석", "김태호", "양세형"}
py = set(["유재석", "박명수"])  #리스트를 집합으로 변경하는 형식
print(java & py)
print(java.intersection(py))

# 합집합
print(java | py)
print(java.union(py))
# print(java + py)  #error code

# 차집합
print(java - py)
print(java.difference(py))


# 항목 추가
print(py.add("김태호"))


# 항목 제거
print(py.remove("김태호"))
