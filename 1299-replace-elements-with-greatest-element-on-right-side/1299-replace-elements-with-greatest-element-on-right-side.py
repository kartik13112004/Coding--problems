class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        largest=arr[-1]
        arr[-1]=-1
        for i in range (len(arr)-2,-1,-1):
            current=arr[i]
            arr[i]=largest
            if current > largest:
                largest=current
        return arr

        
        