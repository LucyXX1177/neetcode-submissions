
# 这里和stack的关系是==>需要python构造stack吗？
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        result=[]
        for i in range(len(operations)):
            
            if operations[i] =="+":
                cur_num=result[-1]+result[-2]
                result.append(cur_num)
            elif operations[i] =="D":
                curr_double=result[-1]*2
                result.append(curr_double)
            elif operations[i] =="C":
                result.pop(-1)
            else:
                result.append(int(operations[i]))
        sum_result=sum(result)
        return sum_result


        