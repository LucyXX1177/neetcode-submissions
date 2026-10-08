class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        

        # 这题可以把duplicte当作linkedlist里面的环形链表
        # 比如[1,3,3,2]
        # 当快指针到fast=nums[2]=3
        # 当慢指针到slow=nums[nums[0]]=nums[1]==3
        # 这两者类似于环形列表里面的相遇
        # 这里的slow就是针对的
        slow,fast=0,0
        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]
            if slow==fast:
                break
        
        # 两个速度一致的
        # 一个是在相遇点，一个是在starting-points
        # 两者相遇一定是在环的入口
        slow2=0
        while True:
            slow=nums[slow]
            slow2=nums[slow2]
            if slow==slow2:
                break
        return slow
            
