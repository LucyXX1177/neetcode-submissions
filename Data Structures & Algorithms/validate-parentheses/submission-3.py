
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2==1:
            return False
        #使用Stack: 先进后出
        result_stack=[]
        for i in range(len(s)):
            if s[i]==")":
                if len(result_stack) == 0:
                    return False
                if result_stack[-1]=="(":
                    result_stack.pop(-1)
                else:
                    return False 
            elif s[i]=="]":
                if len(result_stack) == 0:
                    return False
                if result_stack[-1]=="[":
                    result_stack.pop(-1)

                else:
                    return False 
            elif s[i]=="}":
                if len(result_stack) == 0:
                    return False
                if result_stack[-1]=="{":
                    result_stack.pop(-1)
                else:
                    return False 
            else:
                result_stack.append(s[i])
            print(result_stack)
        if len(result_stack)!=0:
            return False
        return True


