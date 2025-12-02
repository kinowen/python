#클래스1

#1. 클래스 정의
class Person:
    #초기화 메소드
    def __init__(self):
        self.name = "default name"
    def print(self):
        #print("My Name is {0}".format(self.name))
        print(f"My Name is {self.name}")

#2. 인스턴스 생성
p1 = Person()

#3. 메소드 호출
p1.print()