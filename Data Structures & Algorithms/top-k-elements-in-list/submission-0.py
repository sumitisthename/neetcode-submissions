class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        main =[]
        for i in nums:
            if i in res:
                res[i]+=1
            else:
                res[i]=1
        sorted_dict = dict(sorted(res.items(),key= lambda item: item[1], reverse = True))
        for i in sorted_dict.keys():
            main.append(i)
        return main[:k]