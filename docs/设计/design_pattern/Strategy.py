# 策略模式
# 收银父类，各策略一个子类，实现具体的收银

class CashSuper:
    def AcceptCash(self,money):
        return 0.00

class CashNormal(CashSuper):
    def AcceptCash(self,money):
        return money

class CashRebate(CashSuper):
    discount = 0
    def __init__(self,ds):
        self.discount = ds
    def AcceptCash(self,money):
        money=money * self.discount
        return money

class CashReturn(CashSuper):
    total = 0;
    ret = 0;
    def __init__(self,t,r):
        self.total = t
        self.ret = r
    def AcceptCash(self,money):
        if (money>=self.total):
            return money - self.ret
        else:
            return money

class CashContext:
    def __init__(self,ctype): #根据不同打折类型实例化不同的策略类
        self.cs=CashNormal()
        if ctype ==1:
            self.cs = CashNormal()
        elif ctype==2:
            self.cs = CashRebate(0.8)
        elif ctype==3:
            self.cs = CashReturn(300,100)
        else:
            print("Undefine type. Use normal mode.")
            # self.cs = CashNormal()
    def GetResult(self,money):
        return self.cs.AcceptCash(money)

if __name__ == "__main__": #瘦客户端
    money = float(input("money:"))
    ctype = int(input("type:[1]for normal,[2]for 80% discount [3]for 300 -100.\n"))
    # 实例化策略子类
    cc=CashContext(ctype) 
    # 获取收银金额
    money=cc.GetResult(money)
    print("you will pay:%.2f" %(money)) #%d