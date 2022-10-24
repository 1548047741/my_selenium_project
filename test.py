from typing import *


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]

        return []


test = Solution()
Nums = [2, 7, 11, 15]
Target = 9
result = test.twoSum(Nums, Target)
print(result)
