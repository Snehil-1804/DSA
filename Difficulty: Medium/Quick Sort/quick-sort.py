class Solution:
    def quickSort(self, arr, low, high):    
        if low >= high:
            return
        
        pivot_idx = self.partition(arr, low, high)
        self.quickSort(arr, low, pivot_idx - 1)
        self.quickSort(arr, pivot_idx + 1, high)

    def partition(self, arr, low, high):
        pivot = arr[high]
        pos = low
        for i in range(low, high + 1):
            if arr[i] <= pivot:
                arr[pos], arr[i] = arr[i], arr[pos]
                pos += 1
        return pos - 1