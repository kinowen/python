
#분기구문연습.py
# 입력된 문자열을 int 함수를 사용해서 형변환
score = int(input("점수를 입력:"))

if 90 <= score <= 100:
    grade = "A"
elif 80 <= score < 90:
    grade = "B"
elif 70 <= score < 80:
    grade = "C"
else:
    grade = "D"

print("등급은 ", grade)