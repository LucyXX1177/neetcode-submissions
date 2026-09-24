class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_num=len(matrix)
        col_num=len(matrix[0])

        left=0
        right=row_num*col_num-1
        mid =int((left+right+1)//2)
        return self.binarySearch(left,right,matrix,target,row_num,col_num)

    def binarySearch(self,left,right,matrix,target,row_num,col_num):
        
        if left>right:
            return False 
        else:
            mid =int((left+right+1)//2)
            mid_column=int(mid%col_num)
            mid_row=int(mid//col_num)
            mid_value=matrix[mid_row][mid_column]
            if mid_value==target:
                return True
            elif mid_value<target:
                return self.binarySearch(mid+1,right,matrix,target,row_num,col_num)
            else:
                return self.binarySearch(left,mid-1,matrix,target,row_num,col_num)
        
            

        
        
    
    
    
    '''
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 这里先讲2D变成1D-List (严格收尾greater==>必然是sorted List)
        sum_list=[]
        for i in range(len(matrix)):
            sum_list+=matrix[i]# (从这里就不符合题目的要求了==> 复杂度直接O（m*n）
        left=0
        right=len(sum_list)-1
        return self.search(left,right,sum_list,target)

    def search(self,left,right,lst,target):
        mid=int((left+right)/2)
        
        if left>right:
            # 因为可能出现只有one-element:left==right时
            # 则left==right会报错
            return False 
        else:
            if lst[mid]==target:
                return True 
            elif lst[mid]<target:
                return self.search(mid+1,right,lst,target)
            else:
                return self.search(left,mid-1,lst,target)
        
        return False 
    '''