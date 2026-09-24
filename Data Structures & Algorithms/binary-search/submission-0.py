class Solution:

    def binary_search(self,left,right,nums,target) -> int:
        if left>right:
            return -1 
        else:
            mid=int((left+right)//2)
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                return self.binary_search(left,mid-1,nums,target)
            else:
                return self.binary_search(mid+1,right,nums,target)
            

    def search(self, nums: List[int], target: int) -> int:
        # 前提是目前的nums 已经是sorted version 
        # Recursive:
        # 这里是二分是binary sort index list ==>而不是具体的list-value
        return self.binary_search(0,len(nums)-1,nums,target)

        
        