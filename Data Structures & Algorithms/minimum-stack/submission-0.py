class MinStack:

    def __init__(self):
        self.mainstack=[]
        self.minimumstack=[]

    def push(self, val: int) -> None:
        self.mainstack.append(val)
        val=min(val,self.minimumstack[-1] if self.minimumstack else val)
        self.minimumstack.append(val)

    def pop(self) -> None:
        self.mainstack.pop()
        self.minimumstack.pop()

    def top(self) -> int:
        return self.mainstack[-1]

    def getMin(self) -> int:
        return self.minimumstack[-1]
