class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0
        r= len(numbers) - 1
        while l<r:
            tot = numbers[l] + numbers[r]
            if tot == target:
                res = [l+1,r+1]
                break
            elif tot < target:
                l+=1
            else:
                r-=1
        return res