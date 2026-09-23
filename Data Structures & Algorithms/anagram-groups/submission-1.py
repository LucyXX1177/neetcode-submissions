class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result_dict={}
        final_list=[]
        for i in range(len(strs)):
            # 注意不能直接使用set(str)因为会直接删除重复的字符e.g. abb 和 ab 
            key_str = ''.join(sorted(strs[i]))
            if key_str not in result_dict:
                result_dict [key_str ]=[strs[i]]
            
            else:
                result_dict [key_str].append(strs[i])
        
        return list(result_dict.values())
                
        