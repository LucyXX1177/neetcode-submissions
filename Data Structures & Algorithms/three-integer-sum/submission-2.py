# 最直接的思路衔接 ==》从sort-array two sum的题目思路出发
# 固定一个first_index (最外围的for-loop)
# 然后后面的list按照left 和 right的二指针来移动
# 小于则移动left；大于则一定right
# 同时可能会出现duplicate element in results 
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results_list=[]
        nums.sort()
        for i in range (len(nums)-1):
            left_index,right_index=i+1,len(nums)-1
            while left_index < right_index:
                cur_sum=nums[i]+ nums[left_index] + nums[right_index]
                cur_combine=[ nums[i], nums[left_index]  ,nums[right_index]]
                if cur_sum ==0:
                    # 同时可能会出现duplicate element in results 
                    if cur_combine not in results_list:
                        results_list.append (cur_combine)
                    left_index += 1
                    right_index -= 1
                elif cur_sum <0:
                    left_index+=1
                else:
                    right_index-=1

        return results_list
                

                

                

            
        