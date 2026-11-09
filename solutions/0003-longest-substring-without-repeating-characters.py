"""
3. Longest Substring Without Repeating Characters (Medium)
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Problem: Find the length of the longest contiguous stretch of a string in which
no character appears more than once.

Approach: Sliding window. Track the last index of each character; when a
repeat falls inside the window, move the left edge just past it.

Time: O(n)   Space: O(min(n, alphabet))
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = {}
        left = best = 0
        for right, ch in enumerate(s):
            if ch in last and last[ch] >= left:
                left = last[ch] + 1
            last[ch] = right
            best = max(best, right - left + 1)
        return best


if __name__ == "__main__":
    s = Solution()
    assert s.lengthOfLongestSubstring("abcabcbb") == 3
    assert s.lengthOfLongestSubstring("bbbbb") == 1
    assert s.lengthOfLongestSubstring("pwwkew") == 3
    assert s.lengthOfLongestSubstring("") == 0
    assert s.lengthOfLongestSubstring("abba") == 2
    assert s.lengthOfLongestSubstring(" ") == 1
    print("All tests passed.")
