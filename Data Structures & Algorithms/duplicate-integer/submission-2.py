class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # 方法1：放在单独的list里面
        len_list=len(nums)
        occur=[]
        for i in range(len_list):
            if nums[i] not in occur:
                occur.append(nums[i])
            else:
                return True

        return False
        # 方法2： 比较set之间的lengths
        return False if len(set(nums))==len(nums) else True
