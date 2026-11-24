
class Solution:
    def backtrack(self, index, total, result, subset, nums, target):
        if total == 0:
            result.append(subset.copy())
            return

        if total < 0:
            return

        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i-1]:
                continue

            if nums[i] > total:
                break

            subset.append(nums[i])
            self.backtrack(i+1, total-nums[i], result, subset, nums, target)
            subset.pop()

    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        subset = []
        result = []

        self.backtrack(0, target, result, subset, candidates, target)

        return result
