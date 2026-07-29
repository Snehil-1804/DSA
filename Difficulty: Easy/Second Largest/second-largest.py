class Solution:
    def getSecondLargest(self, arr):
        # code here
        largest=-1
        second_largest=-1
        for i in range(len(arr)):
            if arr[i]>largest:
                second_largest=largest
                largest=arr[i]
            elif arr[i]>second_largest and largest!=arr[i]:
                second_largest=arr[i]
        return second_largest