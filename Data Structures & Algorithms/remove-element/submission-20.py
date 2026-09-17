class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        result_index=0

        for i in range(len(nums)):
            if nums[i]!=val:
                nums[result_index]=nums[i]
                result_index+=1

        return result_index 
 