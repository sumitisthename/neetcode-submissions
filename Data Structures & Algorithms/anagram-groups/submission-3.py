class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for i in strs:
            sorted_str = ''.join(sorted(i))
            if sorted_str not in res:
                res[sorted_str] = []
            res[sorted_str].append(i)
        lst = []
        for j in res.values():
            lst.append(j)
        return lst