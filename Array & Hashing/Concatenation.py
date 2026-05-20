from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums
    
    def getConcatenationOnePass(self, nums: List[int]) -> List[int]:
        size = len(nums)
        ans = [0] * (2*size)
        
        for i, num in enumerate(nums):
            ans[i] = ans[i + size] = num
        return ans
   
# Example usage:
solution = Solution()
print(solution.getConcatenation([1, 2, 3]))
print(solution.getConcatenationOnePass([1, 2, 3]))