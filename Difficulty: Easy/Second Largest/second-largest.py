class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        n=len(arr)
        largest=-1
        sec_largest=-1
        for i in range(0,n):
            if arr[i]>largest:
                sec_largest=largest
                largest=arr[i]
            elif arr[i]>sec_largest and arr[i]!=largest:
                sec_largest=arr[i]
            # elif arr[i]==sec_largest:
            #     return -1
        return sec_largest