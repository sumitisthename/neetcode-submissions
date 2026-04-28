class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res ={}
        count = 0
        output =[]
        for i in nums:
            if i in res:
                res[i] += 1
            else:
                res[i] = 1
        sorted_dict = sorted(res.items(), key = lambda items: items[1], reverse=True)
        for j in range(k):
            output.append(sorted_dict[j][0])
        return output