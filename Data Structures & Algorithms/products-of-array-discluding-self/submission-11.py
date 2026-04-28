class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        final = []
        
        # Iterate through each element of the array
        for i in range(n):
            prod = 1
            # Nested loop to multiply all elements except nums[i]
            for j in range(n):
                if i != j:
                    prod *= nums[j]
            final.append(prod)
        
        return final
