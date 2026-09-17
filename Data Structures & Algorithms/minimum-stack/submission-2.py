# 想要达到O（1）每次call minimum 随时取出的话
# 则必须要使用两个stack
# 而且是记录每一次当前做minimum决策时候的最终选择

class MinStack:

    def __init__(self):
        self.ownstack=[]
        self.current_min=[]
        

    def push(self, val: int) -> None:
        if len(self.ownstack)==0:
            self.ownstack.append(val)
            self.current_min.append(val)
        else:
            self.ownstack.append(val)
            # 这里是容易犯错的
            # 不是丢弃掉之前的min，而是记录每一次比大小的结果

            self.current_min.append(min(val,self.current_min[-1]))

        
    def pop(self) -> None:
        result=self.ownstack.pop()
        self.current_min.pop()
        return result
        

    def top(self) -> int:
        return self.ownstack[-1]
        

    def getMin(self) -> int:
        return self.current_min[-1]
        
