


#조건이 반복하는 동안 
customer = "토르"
index = 5
while index >= 1:
    print(f"{customer}의 커피가 준비 되었습니다. {index}번 남았습니다. ")
    index -= 1
    if index == 0:
        print(f"{customer}의 커피를 폐기 하겠습니다. ")



customer = "캡아"
person = "Unknown"
while person != customer :
    print(f"{customer}의 커피가 준비 되었습니다.")
    person = input("이름이 어떻게 되세요?")


    # 무한루프
customer = "아이언맨"
index = 1
while True:
    print(f"{customer}의 커피가 준비 되었습니다. {index}번 호출 하였습니다. ")
    index += 1
