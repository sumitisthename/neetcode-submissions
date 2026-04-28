class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        n = len(heights)
        r = n-1
        max_ar = 0
        while l<r:
            print(l,r)
            max_area = (r-l)*min(heights[l],heights[r])
            max_ar = max(max_ar,max_area)
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1 
            print(max_area)
        return max_ar