

absent = [2, 5] 
nobook = [7]
for student in range(10):
    if student in absent:
        continue
    elif student in nobook:
        print(f"{student}책 읽어봐! 안가져왔어?! 수업 끝! 교무실로 따라와!")
        break
    print(f"{student} 책 읽어봐!!")

