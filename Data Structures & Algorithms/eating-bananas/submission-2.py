class Solution:

    # 二分法左右指针写法
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left,right=1,max(piles)
        result_speed=right
        while left <= right:
            middle=int((left+right)/2)
            curr_hour=0
            for i in piles:
                curr_hour+=math.ceil(i/middle)
            if curr_hour<=h:
                result_speed=middle
                right=middle-1
            else:
                left=middle+1
        return result_speed

            
    

    # 二分法递归写法
    '''
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # 最大能够取到的rate就是piles里面的最大值,大于max值则没有意义，都不如max值
        # 则所有可能的答案是从integer(1~max),所以用二分法在这个list里面找
        maximum_rate=max(piles)
        minimum_rate=1 
        final_list=[]
        self.binary_search(piles,h,maximum_rate,minimum_rate,final_list)
        
        return min(final_list)

    def binary_search(self,piles,h,maximum,minimum,final_list):
        if maximum<minimum:
            return final_list
        else:
            mid=int((maximum+minimum)/2)
            curr_time=0
            for i in range(len(piles)):
                if piles[i]%mid==0:
                    curr_time+=(piles[i]//mid)
                else:
                    curr_time+=((piles[i]//mid)+1)

            # 这里如果mid_rate已经达标：则直接查找左边更加slow_rate
            if curr_time < h or curr_time==h:
                final_list.append(mid)
                
                return self.binary_search(piles,h,mid-1,minimum,final_list)
            # 反之必须找更大的rate,往右边找，必须找更加大的rate 
            else:
                return self.binary_search(piles,h,maximum,mid+1,final_list)
                
            
        return final_list
        '''
    
    
        