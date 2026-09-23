class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # 还是left & right双指针
        # 每次只考虑是否移动最短边
        # 只要左边或者右边的最短边还在，它之后任何更靠里的右边柱子组成的面积，都不可能超过这一次
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
            
            
            


        