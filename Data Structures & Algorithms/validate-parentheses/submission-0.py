class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        pairs = {')': '(', '}': '{', ']': '['}
        stack = []

        for char in s:
            if char in pairs.keys():
                # char is a closing bracket
                if not stack or stack[-1] != pairs[char]:
                    return False
                else:
                    stack.pop()
            else:
                # char is an opening bracket
                stack.append(char)

        return len(stack) == 0