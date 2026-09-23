class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums_stack=[]
        operate_stack=[]

        for i in range(len(tokens)):
            if tokens[i] not in ['+', '-', '*','/']:
                nums_stack.append(int(tokens[i]))
            elif tokens[i]=='+':
                nums1=nums_stack.pop(-1)
                nums2=nums_stack.pop(-1)
                result=nums1+nums2
                nums_stack.append(result)
            elif tokens[i]=='*':
                nums1=nums_stack.pop(-1)
                nums2=nums_stack.pop(-1)
                result=nums1 * nums2
                nums_stack.append(result)
            elif tokens[i]=='-':
                nums1=nums_stack.pop(-1)
                nums2=nums_stack.pop(-1)
                result=nums2-nums1
                nums_stack.append(result)
            elif tokens[i]=='/':
                nums1=nums_stack.pop(-1)
                nums2=nums_stack.pop(-1)
                result=int(nums2/nums1)

                nums_stack.append(result)
            
        return nums_stack[-1]

        