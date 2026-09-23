class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=sorted(nums)
        count_len=1
        if nums==[]:
            return 0
        result=[]
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]-1:
                count_len+=1 
            elif nums[i]==nums[i+1]:   
                continue
            elif nums[i] != nums[i+1]-1:
                result.append(count_len)
                count_len=1
        result.append(count_len)

        return max(result)
        