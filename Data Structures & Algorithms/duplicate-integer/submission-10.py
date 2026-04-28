class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        status = False
        seen = set()
        for i in nums:
            if i in seen:
                status = True
            else:
                seen.add(i)
        return status