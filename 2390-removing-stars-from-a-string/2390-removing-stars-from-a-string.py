class Solution:
    def removeStars(self, s: str) -> str:
        stack=[]
        for ch in s:
            if ch=="*":
                if stack:
                    stack.pop()
            else:
                stack.append(ch)
        k="".join(stack)
        return k
