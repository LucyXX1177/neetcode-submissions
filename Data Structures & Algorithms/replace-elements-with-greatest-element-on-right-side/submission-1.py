class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        len_arr=len(arr)
        result=[0]*len_arr
        max=arr[len_arr-1]
        for i in range (len_arr-1, -1,-1):
            if arr[i]<=max:
                result[i]=max

            elif arr[i]>max:
                result[i]=max
                max=arr[i]

        result[-1]=-1
        return result

            
        