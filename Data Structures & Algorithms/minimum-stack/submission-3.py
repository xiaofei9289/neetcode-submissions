class MinStack:

    def __init__(self):
        self.stack=[]
        self.get_min=[]
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.get_min:
            self.get_min.append(val)
        else:
            self.get_min.append(min(val, self.get_min[-1]))


    def pop(self) -> None:
        self.stack.pop()
        self.get_min.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.get_min[-1]
