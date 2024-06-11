#
# James A. Chase
# 061024
#
from typing import List, Dict


class Solution:
    @staticmethod
    def two_sum(nums: List[int], target: int) -> List[int]:
        m: Dict[int, int] = {}
        for idx, num in enumerate(nums):
            if target - num in m:
                return [m[target - num], idx]
            m[num] = idx


if __name__ == '__main__':
    assert False, 'This is a class file. Import its contents into another file.'
