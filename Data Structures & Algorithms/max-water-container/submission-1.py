class Solution:
    def maxArea(self, heights: List[int]) -> int:
        container=0
        h1,h2 = 0,len(heights) -1
        while h1 < h2:
            area=(h2-h1)*min(heights[h1], heights [h2])
            container=max(area, container)
            if heights[h1]<heights[h2]:
                h1+=1
            else:
                h2-=1
        return container 
