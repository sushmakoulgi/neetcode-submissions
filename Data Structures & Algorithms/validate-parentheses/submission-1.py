from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack=deque()
        d={
            "[":"]",
            "{":"}",
            "(":")"
        }
        for item in s:
            if item not in d.values():
                stack.append(item)
            else:
                if stack and  item==d[stack[-1]]:
                    stack.pop()
                else:
                    return False
        if len(stack)==0:
            return True
        return False #in case some are still pending to be matched
        