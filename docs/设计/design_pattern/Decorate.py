# 装饰模式
"""
模式特点：动态地为对象增加额外的职责
程序实例：展示一个人一件一件穿衣服的过程
"""
class Person:
    def __init__(self,tname):
        self.name = tname
    def show(self):
       print("dressed %s" %(self.name))

class Finery(Person): # 服饰
    componet = None
    def __init__(self):
        pass
    def decorate(self,ct):
        self.componet = ct
    def show(self):
        if(self.componet!=None):
            self.componet.show()

class TShirts(Finery):
    def __init__(self):
        pass
    def show(self):
        print("Big T-shirt ", end='')
        self.componet.show()

class BigTrouser(Finery):
    def __init__(self):
        pass
    def show(self):
        print("Big Trouser ", end='')
        self.componet.show()

class Slipper(Finery):
    def __init__(self):
        pass
    def show(self):
        print("Slipper ", end='')
        self.componet.show()

if __name__ == "__main__":
    p = Person("somebody")
    # 准备大裤衩、T恤、拖鞋
    bt = BigTrouser()
    ts = TShirts()
    sl = Slipper()
    # 开始穿
    bt.decorate(p)
    ts.decorate(bt)
    sl.decorate(ts)
    
    sl.show() # 穿着顺序与装饰顺序相反？