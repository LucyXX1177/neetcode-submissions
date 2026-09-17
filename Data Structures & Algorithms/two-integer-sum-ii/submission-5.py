# hint 1: 这是一个已经被sorted in non-decreaing order的array
# 按照左和右来操作
# 从left最小 + right最大
# 如果比target小，说明left 太小
# 如果比target大，说明right太大
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left,right=0,len(numbers)-1
        while left!=right:
            if numbers[left] + numbers[right]==target:
                return [left+1,right+1]
            elif numbers[left] + numbers[right] < target:
                left+=1
            elif numbers[left] + numbers[right] > target:
                right-=1
            

        
      