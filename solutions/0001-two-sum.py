"""
1. Two Sum (Easy)
https://leetcode.com/problems/two-sum/

Problem: Given a list of integers and a target, return the indices of the two
numbers that add up to the target (exactly one valid pair exists).

Approach: One pass with a hash map from value -> index. For each number, check
whether its complement (target - num) has already been seen.

Time: O(n)   Space: O(n)
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            if target - num in seen:
                return [seen[target - num], i]
            seen[num] = i
        return []


if __name__ == "__main__":
    s = Solution()
    assert s.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert s.twoSum([3, 2, 4], 6) == [1, 2]
    assert s.twoSum([3, 3], 6) == [0, 1]
    assert s.twoSum([-1, -2, -3, -4, -5], -8) == [2, 4]
    print("All tests passed.")
