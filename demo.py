# demo.py

print("Hello VS Code")

# List [1,2,3] : 순서있음. 입력, 수정, 삭제, 검색 가능
# Tuple (1,2,3) : 순서있음. 내용변경 안됨 read-only
# Set {1,2,3} : 순서없음. 합집합, 교집합, 차집합 연산가능
# Dict {key1:value1, key2:value2} : 순서없음. 키를 사용해서 값을 꺼냄

#반복문 사용
#중단점 (Break Point)를 추가
for i in [1,2,3]:
    print(i)

a="python"
print(a[:-2])
print(a[-2:])
print(a[0:3])
print(a[:])
print(a*3)

strA="python"
strB="파이썬은 강력해"  # """ 개행 시 사용 → multiple line
strC="""
파이썬은
강력한
언어입니다
"""

print(len(strA))
print(len(strB))
print(strC)
print(strA[:])

# 리스트 메소드 연습
colors=["red","blue","green"]
colors.append("black")
colors.insert(1, "pink")
print(colors)
colors.remove("red")
print(colors)
colors.extend(["white","blue","yellow"])
colors.sort()
print(colors)
colors.reverse()
print(colors)

#숫자를 스트링으로 변경
print("abcd" + str(1234))


#Set 형식 연습
a={1,2,3,3}
b={3,4,4,5}
print(type(a))
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

#Tuple 형식 연습
tp = (10,20,30)
print(len(tp))
print(tp.index(20))
print(tp.count(10))

#함수 정의
def calc(a,b):
    return a+b, a*b
print(calc(3,4))
args=(5,6)
print(calc(*args))



