#function2.py

#람다함수 : 이름없는 익명함수, 간단한 기능을 한 줄로 정의할 수 있음
g= lambda x, y : x*y
print(g(3,4))
print((lambda x:x*x)(3))
g2 = lambda x : x*8
print(g2(3))
print(globals())






