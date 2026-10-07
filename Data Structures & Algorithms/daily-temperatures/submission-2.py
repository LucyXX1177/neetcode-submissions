class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 用Stack来保存之前遍历的temperature他们的index
        # 单独的Stack来记录没有找到warmer temperature的index
        stack_record=[] # pairs:[temperature,index]
        result=len(temperatures)*[0]
        
        for i in range(len(temperatures)):  
            curr_temp=temperatures[i]
            while stack_record and stack_record[-1][0]<curr_temp:
                [prev_temp,prev_index]=stack_record.pop()
                result[prev_index]=i-prev_index
                
            stack_record.append([curr_temp,i])
            
        return result
