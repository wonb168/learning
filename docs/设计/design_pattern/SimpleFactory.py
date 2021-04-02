# 简单工厂模式

class Operation:
    def GetResult(self):
        pass

class OperationAdd(Operation):
    def GetResult(self):
        return self.op1+self.op2


class OperationSub(Operation):
    def GetResult(self):
        return self.op1-self.op2


class OperationMul(Operation):
    def GetResult(self):
        return self.op1*self.op2


class OperationDiv(Operation):
    def GetResult(self):
        try:
            result = self.op1/self.op2
            return result
        except:
            print("error:divided by zero.")
            return 0

class OperationUndef(Operation):
    def GetResult(self):
        print("Undefine operation.")
        return 0

class OperationFactory:
    operation = {}
    operation["+"] = OperationAdd();
    operation["-"] = OperationSub();
    operation["*"] = OperationMul();
    operation["/"] = OperationDiv();
    def createOperation(self,ch):        
        if ch in self.operation:
            op = self.operation[ch]
        else:
            op = OperationUndef()
        return op

if __name__ == "__main__":
    op = input("operator: ")
    opa = input("a: ")
    opb = input("b: ")
    factory = OperationFactory()
    cal = factory.createOperation(op)
    cal.op1 = float(opa)
    cal.op2 = float(opb)
    print(cal.GetResult())