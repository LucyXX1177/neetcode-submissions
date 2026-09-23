class Solution:
    def isPalindrome(self, s: str) -> bool:
        left=0
        right=len(s)-1
        alphaunmeric_all='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
        while left<right:
            if s[left] not in alphaunmeric_all:
                left+=1
                continue
            elif s[right] not in alphaunmeric_all:
                right-=1    
                continue
            else:
                if s[left].lower() != s[right].lower():
                    
                    return False 
                else:
                    left+=1
                    right-=1
        return True
        