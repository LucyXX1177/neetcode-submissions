class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        len_list=len(nums)
        occur=[]
        for i in range(len_list):
            if nums[i] not in occur:
                occur.append(nums[i])
            else:
                return True

        return False
