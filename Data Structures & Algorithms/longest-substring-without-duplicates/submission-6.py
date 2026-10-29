from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        q=deque()
        seen=set()
        max_length=0
        for c in s:
            if c not in seen:
                #print("appending",c)
                q.append(c)
                seen.add(c)
            else:
                max_length=max(max_length,len(q))
                #print("length",len(q))
                while c in seen:
                    v=q.popleft()
                    seen.remove(v)

                q.append(c)
                seen.add(c)
    

        max_length=max(max_length,len(q))
        return max_length