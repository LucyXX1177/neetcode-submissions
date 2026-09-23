class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 每个位置的答案 = 左边所有数字的乘积×右边所有数字的乘积
        # 【2，3，4，5，6】

        result=[1]*len(nums)
        
        # 先记住每个index的左边都是什么
        prefix=1
        for i in range(len(nums)):
            result[i]=prefix
            prefix*=nums[i]
        
        # 再记住每个index的右边都是什么
        suffix=1
        for i in range(len(nums)-1,-1,-1):
            result[i]*=suffix
            suffix*=nums[i]
        
        return result
            