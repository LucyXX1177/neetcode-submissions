class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        unsolved_stack=[]
        result=len(temperatures)*[0]
        for i in range(len(temperatures)):
            curr_temp= temperatures [i] 
            while unsolved_stack!=[] and curr_temp > temperatures[unsolved_stack[-1]]:
                    result[unsolved_stack[-1]]=i-unsolved_stack[-1]
                    unsolved_stack.pop()        
            
            unsolved_stack.append(i)
        return result