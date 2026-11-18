
class Solution:
    def solve(self, index, total, bracket, result, n):
        if index == len(bracket):
            if total == 0:
                result.append("".join(bracket))
            return

        if total < 0 or total > n:
            return

        bracket[index] = "("
        self.solve(index + 1, total + 1, bracket, result, n)

        bracket[index] = ")"
        self.solve(index + 1, total - 1, bracket, result, n)

    def generateParenthesis(self, n: int) -> list[str]:
        bracket = [""] * (2 * n)
        result = []
        self.solve(0, 0, bracket, result, n)
        return result
