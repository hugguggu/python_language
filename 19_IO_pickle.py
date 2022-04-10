

import pickle


# 파일 열기
profile_file = open("profile.pickle", "wb")

profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}

print(profile)


# 파일에 저장
pickle.dump(profile, profile_file)
profile_file.close()


# 파일 열기
profile_file = open("profile.pickle", "rb")

# 파일에서 가져오기
profile = pickle.load(profile_file)

print(profile)

profile_file.close