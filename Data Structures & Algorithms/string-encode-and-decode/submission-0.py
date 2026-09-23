class Solution:
    #理解1：这题不能传入任何的encoded-string以外的string
    # 就是不能用单独的列表来进行recording 
    # 同时注意这里encode/decode 输入和输出的都只能是str不能是别的
    # 极端案例：
    # 必须length写在最前面 + 特殊的标识符i.e. ‘#’ 标识着开始读取这个str
    # 例如：1231#abcdef.....代表着：1231  #  后面1231个字符

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append("#")
            res.append(s)
        return "".join(res)
            

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            # 统计当前的length的具体数值（不一定是个位数）
            length = int(s[i:j])
            # 统计当前的length的长度
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j

        return res



            

