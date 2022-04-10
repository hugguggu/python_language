

# 파일 쓰기권한으로 열기
score_file = open("score.txt", 'w', encoding="utf8")

# 파일에 쓰기
print("math : 0", file=score_file)
print("english : 50", file=score_file)

# 파일 닫기
score_file.close()

# 이어쓰기 권한으로 열기
score_file = open("score.txt", 'a', encoding="utf8")

# 파일에 쓰기. 이 형식은 줄바꿈이 없음
score_file.write("coding : 100\n")

# 파일 닫기
score_file.close()


# 읽기 권한으로 파일 열기
score_file = open("score.txt", 'r', encoding="utf8")

# 파일 내용 전체 읽기
print(score_file.read())

# 파일 닫기
score_file.close()




# 읽기 권한으로 파일 열기
score_file = open("score.txt", 'r', encoding="utf8")

# 파일 내용 한줄씩 읽기. 커서는 다음줄로 이동
print(score_file.readline())
print(score_file.readline())
print(score_file.readline(), end="")

# 파일 닫기
score_file.close()




# 읽기 권한으로 파일 열기
score_file = open("score.txt", 'r', encoding="utf8")

# 파일 내용 한줄씩 끝까지 읽기
while True:
    line = score_file.readline()
    if not line:
        break
    print(line, end="")

# 파일 닫기
score_file.close()






# 읽기 권한으로 파일 열기
score_file = open("score.txt", 'r', encoding="utf8")

# 라인별로 리스트에 넣기
lines = score_file.readlines()
# 리스트 내용 한줄씩 끝까지 읽기
for line in lines:
    print(line, end="")

# 파일 닫기
score_file.close()



