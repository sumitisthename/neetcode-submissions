class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res ={}
        for i in strs:
            key = sorted(i)
            key = ''.join(key)
            if key not in res:
                res[key]=[]
            res[key].append(i)
        return list(res.values())