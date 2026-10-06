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
                while timestamp>0:
                    timestamp-=1
                    if timestamp in self.inner[key].keys():
                        return self.inner[key][timestamp]
                # 当永远找不到的时候（没有更前面的时候）必须return"""
                return ""
        else:
            return ""     

                


            
        
