

# 리스트 선언, 초기화
from re import sub


subway = ["유재석", "조세호", "박명수"]
print(subway)


# 해당 오브젝트의 인덱스 출력
print(subway.index("조세호"))\


# 리스트에 오브젝트 추가
subway.append("하하")
print(subway)


# 리스트 중간에 삽입
subway.insert(1, "정형돈")
print(subway)


#   리스트 뒤에서 제거
print (subway.pop())
print (subway)


#   오브젝트 개수 출력
print(subway.count("유재석"))


#  리스트 정렬
subway.sort()
print(subway)


# 리스트 인덱스 거꾸로 하기
subway.reverse()
print(subway)

#  리스트에 모든 항목 삭제
subway.clear()
print(subway)


# 다양한 자료형 사용 가능
subway.append("조세호")
subway.append(888)
subway.append(True)
print(subway)


# 리스트 합치기
num = [1, 2, 3, 4, 5]
subway.extend(num)
print(subway)