class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 这里和之前的two-sum不相同：unsorted + number repetition 
        # 用seem 字典来保存之前遍历过的numbers
        seem={}
        for i in range(len(nums)):
            complement=target-nums[i]
            if complement in seem:
                return sorted([i,seem[complement]])
            seem[nums[i]]=i