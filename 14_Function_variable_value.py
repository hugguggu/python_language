

# 기본 함수 형
# 몇개가 입력될지 알수 없는 변수 때문에 복잡해짐
# def profile(name, age, lan1, lang2, lang3, lang4, lang5):
#     print(f"이름 : {name}, 나이 : {age}, 주 언어 : {lan1}", end= " ")
#     print(lan1, lang2, lang3, lang4, lang5)

# profile("유재석", 20, "파이썬", "자바", "C", "C++", "C#")
# profile("김태호", 30, "코틀린", "스위프트", "", "" , "")

def profile(name, age, *lang):
    print(f"이름 : {name}, 나이 : {age}, ", end= " ")
    for i in lang:
        print(i, end = " ") 
    print()

profile("유재석", 20, "파이썬", "자바", "C", "C++", "C#")
profile("김태호", 30, "코틀린", "스위프트", "", "" , "")