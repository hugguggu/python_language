

# 기본 함수 형
# def profile(name, age, main_lang):
#     print(f"이름 : {name}, 나이 : {age}, 주 언어 : {main_lang}")


# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")


# 기본값이 지정된 함수
def profile(name, age = 17, main_lang = "파이썬"):
    print(f"이름 : {name}, 나이 : {age}, 주 언어 : {main_lang}")


profile("유재석")
profile("김태호", "자바")