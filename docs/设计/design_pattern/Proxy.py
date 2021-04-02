# 代理模式
# 举例：找人帮忙追女生，代理和追求者都有送礼物的方法，礼物实际是真实追求者送的
class Interface :
    def giveGift(self):
        return 0

class Persuit(Interface): 
    def giveGift(self):
        print("Give Gift.")

class Proxy(Interface):
    def giveGift(self):
        self.real = Persuit()
        self.real.giveGift()

if __name__ == "__main__":
    p = Proxy()
    p.giveGift()