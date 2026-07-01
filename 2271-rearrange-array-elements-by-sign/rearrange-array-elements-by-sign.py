class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        pos, neg = 0, 1

        for num in nums:
            if num >= 0:
                result[pos] = num
                pos += 2
            else:
                result[neg] = num
                neg += 2

        return result