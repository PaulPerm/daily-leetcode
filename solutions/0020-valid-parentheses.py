"""
20. Valid Parentheses
Difficulty: Easy
Link: https://leetcode.com/problems/valid-parentheses/

Summary:
    Given a string made up only of the bracket characters ()[]{}, decide
    whether every opener is closed by the matching bracket type in the
    correct nesting order.

Approach:
    Walk the string with a stack. Push each opening bracket. On a closing
    bracket, the top of the stack must be its matching opener; otherwise
    the string is invalid. At the end the stack must be empty.

Complexity:
    Time:  O(n) - one pass over the string.
    Space: O(n) - the stack can hold every character in the worst case.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")": "(", "]": "[", "}": "{"}
        stack = []
        for ch in s:
            if ch in pairs:
                if not stack or stack.pop() != pairs[ch]:
                    return False
            else:
                stack.append(ch)
        return not stack


if __name__ == "__main__":
    sol = Solution()
    assert sol.isValid("()") is True
    assert sol.isValid("()[]{}") is True
    assert sol.isValid("{[()]}") is True
    assert sol.isValid("(]") is False
    assert sol.isValid("([)]") is False
    assert sol.isValid("(") is False
    assert sol.isValid(")") is False
    assert sol.isValid("") is True
    print("All tests passed.")
