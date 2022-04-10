

gun = 10

# 변수 gun 때문에 오류 발생
# def checkpoint(soldiers):
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))

# 전역 변수를 이용한 방법
def checkpoint(soldiers):
    global gun
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    

print("[함수 밖] 남은 총 : {0}".format(gun))
checkpoint(2)
print("[함수 밖] 남은 총 : {0}".format(gun))