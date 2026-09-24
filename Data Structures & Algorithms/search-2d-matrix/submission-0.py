class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 这里先讲2D变成1D-List (严格收尾greater==>必然是sorted List)
        sum_list=[]
        for i in range(len(matrix)):
            sum_list+=matrix[i]
        left=0
        right=len(sum_list)-1
        return self.search(left,right,sum_list,target)

    def search(self,left,right,lst,target):
        mid=int((left+right)/2)
        
        if left>right:
            # 因为可能出现只有one-element:left==right时
            # 则left==right 
            return False 
        else:
            if lst[mid]==target:
                return True 
            elif lst[mid]<target:
                return self.search(mid+1,right,lst,target)
            else:
                return self.search(left,mid-1,lst,target)
        
        return False 