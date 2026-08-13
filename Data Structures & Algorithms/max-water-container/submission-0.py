class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1
        r = 0
        while i < j:
            c = min(heights[i] , heights[j]) * (j - i)
            r = max(r, c)
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return r