class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        n=len(temperatures)
        res=[0]*n
        for i in range(n):
            if not stack:
                stack.append(i)
            else:
                if temperatures[stack[-1]]>= temperatures[i]:
                    stack.append(i)
                else:
                    while stack and temperatures[stack[-1]] < temperatures[i]: 
                        previndex=stack.pop()
                        currentindex=i
                        res[previndex]=currentindex-previndex
                    stack.append(i)
        return res



                