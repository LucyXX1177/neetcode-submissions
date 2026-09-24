class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:    
        # 一个重要的条件是后面的车超过前面的车之后就不能继续加速了：
        # A car can not pass another car ahead of it. 
        # It can only catch up to another car and then drive at the same speed as the car ahead of it.
        # 目前的position是乱序排列的, 没有任何的顺序
        # 是否构成fleet: 是距离远的车能够在target距离内追上距离近的车 (需要倒叙，先算距离近的车)
        car_pair=sorted(zip(position,speed),reverse=True) # 这里的reverse是按照zip里面的第一个元素的排序
        fleet=0
        front_time=0
        for i in range(len(car_pair)):
            (pos,carSpeed)=car_pair[i]
            time_req=(target-pos)/carSpeed
            if time_req>front_time:
                # 追不上前方车队，形成新车队
                fleet+=1
                front_time=time_req
            
        return fleet


            
    
            

