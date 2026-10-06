class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 理解成left and right双指针
        # 当遇到了相同的character则开始移动左指针，直到set里面不存在replicates
        curr_set=set()
        left=0
        max_length=0

        for i in range(len(s)):
            while s[i] in curr_set:
                curr_set.remove(s[left])
                left+=1
            curr_set.add(s[i])
            max_length=max(max_length,len(curr_set))
        return max_length 


            