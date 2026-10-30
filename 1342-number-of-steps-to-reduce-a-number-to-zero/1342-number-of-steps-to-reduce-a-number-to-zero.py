class Solution:
    def numberOfSteps(self, num: int) -> int:
        count=0
        for i in range (num):
            if num %2==0:
                num=num//2
            elif num %2!=0:
                k=num=num-1
            count+=1
            if num==0:
                break
        return count

        