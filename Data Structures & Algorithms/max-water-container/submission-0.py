class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxi = 0

        lefty = 0 
        righty = len(heights) - 1

        while lefty != righty: 
            width = righty - lefty
            hight = min(heights[lefty],heights[righty])
            area = width * hight
            maxi = max(maxi,area)
            if hight == heights[lefty]:
                lefty += 1
            else:
                righty -= 1
        return maxi
