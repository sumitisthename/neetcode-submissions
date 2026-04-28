class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums = sorted(set(nums))
        n = len(nums)
        res = {}
        count = 1
        i = 0
        if n > 0:
            for i in range(n-1):
                j = i+1
                if nums[i] == nums[j] -1:
                    count +=1
                    #i+=1
                else:
                    count = 1
                res[nums[i]] = count

            res[nums[-1]] = count
        print(res)
        if nums == []:
            mac = 0
        elif nums == [0]:
            mac = 1
        else:
            mac = max(list(res.values()))

        print(res)
        return mac

        