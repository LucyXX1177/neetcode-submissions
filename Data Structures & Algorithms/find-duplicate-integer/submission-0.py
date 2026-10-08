class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        

        # 暴力解法
        # 先遍历然后用Dict储存起来key
        dict_result={}
        for i in range(len(nums)):
            if nums[i] not in dict_result:
                dict_result[nums[i]]=1
            else:
                result=nums[i]
                break
        return result
            

                
            
        
        