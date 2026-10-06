class TimeMap:

    def __init__(self):
        self.inner=dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.inner:
            self.inner[key] = {}
        self.inner[key][timestamp]=value
        
    def get(self, key: str, timestamp: int) -> str:
        if key in self.inner:
            if timestamp in self.inner[key]:
                return self.inner[key][timestamp]
            else:
                # 提升time complexity的关键在于找到最靠近的一个timestamp
                # 怎么快速找到 predecessor，也就是 <= target 的最大 timestamp
                # 如何floor search 找到最大下界
                list_timestamp=list(self.inner[key].keys())
                left=0
                right=len(list_timestamp)-1
                res=-1
                while left <= right:
                    middle =(left+right)//2
                    if list_timestamp[middle]>timestamp:
                        right=middle -1 
                    elif list_timestamp[middle]<timestamp:
                        res=middle 
                        left=middle+1
                    else:
                       res=middle

                       break
                
                # 暴力的一个个的剪掉
                # while timestamp>0:
                #     timestamp-=1
                #     if timestamp in self.inner[key].keys():
                #         return self.inner[key][timestamp]
                # 当永远找不到的时候（没有更前面的时候）必须return"""
                if res==-1:
                    return ""
                
                return self.inner[key][list_timestamp[res]]
        # 如果key不存在也能够return ""
        else:
            return ""     

                


            
        
