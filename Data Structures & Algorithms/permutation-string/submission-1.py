class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # 1) 暴力解法：使用dictionary 先重新统计字符
        # 2) 滑动窗口解法：移除左侧，加入右侧
        # 写法参考：
        # window[c] = window.get(c, 0) + 1
        # window.get(c, 0)	如果 c 存在，返回对应的 value；否则返回 0
        
        s1_dict={}
        for i in range(len(s1)):
            s1_dict[s1[i]]=s1_dict.get(s1[i],0)+1 
        
        left=0
        window={}
        for right in range (len(s2)):

            # 目前的curr_right character
            curr=s2[right]
            # 目前的记录的window
            window[curr]=window.get(curr,0)+1 

            #然后如果到达临界长度
            if right - left + 1 > len(s1):
                # 先剔除目前的left部分
                window[s2[left]]-=1
                # 如果彻底等于0，则直接删除key
                if window[s2[left]]==0:
                    del window[s2[left]]
                
                # 重新更新left指针
                left+=1 

            if window == s1_dict:
                return True 
        return False 

            






