class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # 还是left & right双指针
        # 针对的是目前的
        max_area=0
        left=0
        right=len(heights)-1
        while left!=right:
            current_area=(right-left)*min(heights[right],heights[left])
            max_area=max(max_area,current_area)
            
            if heights[left]<heights[right]:
                left+=1
                
            else:
                right-=1
                
        
        return max_area
            
            
            


        