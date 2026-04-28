class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i,j = 0, len(heights)-1
        print(i,j)
        max_area = 0
        while i<j:
            area = (j-i)*min(heights[i],heights[j])
            print(area)
            max_area = max(max_area,area)
            if heights[i] < heights[j]:
                i+=1
            else:
                j-=1
        return max_area        