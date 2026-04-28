class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        for i in nums:
            if i in res:
                res[i]+=1
            else:
                res[i] = 1
        sorted_dict = dict(sorted(res.items(), key=lambda item: item[1], reverse=True))
        lst = []
        for j in sorted_dict.keys():
            lst.append(j)
        return sorted(lst[:k])
