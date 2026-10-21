class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack=[]
        for ch in s:
            if ch=='#':
                if stack:
                    stack.pop() 
            else:
                stack.append(ch)
        k=[]
        for ch in t:
            if ch=='#':
                if k:
                    k.pop() 
            else:
                k.append(ch)
        return stack==k
        