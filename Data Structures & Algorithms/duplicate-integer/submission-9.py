class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        if nums ==[]:
            status = False
        for i in nums:
            if i in dict:
                dict[i]+=1
            else:
                dict[i]=1
        for i in dict.values():
            if i > 1:
                status = True
                break
            else:
                status = False

        return status
        
         