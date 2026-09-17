class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      len_s,len_t=len(s),len(t)
      dict_s,dict_t={},{}
      if len_s!=len_t:
        return False
      else:
        for i in range(len_s):
            if s[i] not in dict_s:
                dict_s[s[i]] = 1
                if t[i] not in dict_t:
                    dict_t[t[i]] = 1
                else:
                    dict_t[t[i]]+=1
            else:
                dict_s[s[i]]+=1
                if t[i] not in dict_t:
                    dict_t[t[i]] = 1
                else:
                    dict_t[t[i]]+=1



      return True if dict_s==dict_t else False

