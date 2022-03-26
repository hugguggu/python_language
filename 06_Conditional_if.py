

weather = '비'

# 기본 if문 형식
if weather == '비':
    print ("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비물은 없어요")

# 여러개 조건중 하나 만족 할 때
if weather == '비' or '눈' or '우박':
    print ("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비물은 없어요")



# 비교하여 조건 만족할때
temp = int(input("기온은 어때요? "))
if 30 <= temp:
    print("너무 덥네요")
elif 10 < temp and temp < 30:
    print("괜찮은 날씨네요")
elif 0 <= temp < 10:
    print("조금 춥네요")
else:
    print("얼어 죽겠네여")