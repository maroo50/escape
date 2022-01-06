class Cls:
    x, y = 10, 20

    def chg(self):
        temp = self.x
        self.x = self.y
        self.y = temp


a = Cls()
print(a.x, a.y)
a.chg()
print(a.x, a.y)

# 클래스 Cls x 10, y 20
# a 클래스 안에 x = 10 y = 20 임
# a,chg 함수를 했을 때 temp = x 10 이고, y는 x에들어가 x 는 20이되고 y는 10이됨
