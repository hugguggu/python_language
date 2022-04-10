

import pickle

# with 사용시 close 필요 없음
with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))

with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("study hard")


with open("study.txt", "r") as study_file:
    print(study_file.read())