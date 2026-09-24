class Solution:
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
            
            if curr_time < h or curr_time==h:
                final_list.append(mid)
                return self.binary_search(piles,h,mid-1,minimum,final_list)

            else:
                return self.binary_search(piles,h,maximum,mid+1,final_list)
                
            
        return final_list

    
    
        