#
# James A. Chase
# 061024
#
from typing import List


class Solution:
    @staticmethod
    def two_sum(nums: List[int], target: int) -> List[int]:
        l: int = 0
        r: int = len(nums) - 1
        while l < r:
            if nums[l] + nums[r] == target:
                return [l, r]
            elif nums[l] + nums[r] < target:
                l += 1
            else:
                r -= 1


if __name__ == '__main__':
    solution = Solution()
