class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_result={}

        for i in range(len(nums)):
           if nums[i] not in dict_result:
            dict_result[nums[i]]=1
           else:
            dict_result[nums[i]]+=1
        # 2. 根据 value（frequency）对 key 进行排序
        sorted_nums = sorted(
            dict_result,
            key=lambda x: dict_result[x],
            reverse=True
        )

        # 3. 取 frequency 最高的前 k 个数字
        return sorted_nums[:k]

        