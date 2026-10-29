from collections import deque
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        max_area=float('-inf')
        for i in range(len(heights)):
            if len(stack)==0:
                stack.append(i)
                continue
            if heights[stack[-1]]<heights[i]:
                stack.append(i)
            else:
                nsi=i
                while stack and heights[stack[-1]]> heights[i]:
                    elem=heights[stack.pop()]
                    psi=stack[-1] if stack else -1
                    #print("evaluating ",heights[i])
                    
                    area=elem*((nsi-psi)-1)
                    #print(area)
                    max_area=max(area,max_area)
                stack.append(i)

        n=len(heights)
        while stack:
            nsi=n
            elem=heights[stack.pop()]
            psi=stack[-1] if stack else -1
            #print("evaluating ",heights[i])
            area=elem*((nsi-psi)-1)
            max_area=max(area,max_area)

        return max_area

        
