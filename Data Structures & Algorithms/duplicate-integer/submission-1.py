class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        count = 1
        for i in nums:
            if i in dict:
                count+=1
                dict[i] = count
            else:
                dict[i] = count
        if nums == []:
            status = False
        for x in dict.values():
            print(x)
            if x>1:
                status = True
                break
            else:
                status = False
        return status
         