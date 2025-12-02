
# function1.py

#1) 함수정의
def setValue(newValue):
    x = newValue
    print("함수내부:", x)

#2) 함수호출
result = setValue(5)
print(result)

#3) 함수정의
def swap(x, y):
    return y, x

#4) 함수호출
result = swap(3, 4)
print(result)



#5) 함수인자의 기본값을 명시하는 방법
print("---기본값을 명시")
def times(a=10, b=20):
    return a*b
print(times())
print(times(5))
print(times(5,6))

#6) 함수인자의 키워드로 인자값을 넘기는 방법
print("--키워드인자--")
def connectURI(server, port):
    strUrl = "https://" + server + ":" + port
    return strUrl
print(connectURI("naver.com", "80"))
print(connectURI(port="800", server="naver.com"))
# __으로 시작하는 변수들은 파이선 내부 변수/함수들
print(dir())
print(globals())


#7) 가변인자
def union(*ar):
    result=[]
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result

print(union("HAM", "EGG"))
print(union("HAM", "EGG", "SPAM"))