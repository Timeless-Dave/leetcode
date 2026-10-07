class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        # Count misplaced '(' and ')'
        rem_l = 0
        rem_r = 0
        for ch in s:
            if ch == '(':
                rem_l += 1
            elif ch == ')':
                if rem_l > 0:
                    rem_l -= 1
                else:
                    rem_r += 1

        result = set()

        def backtrack(index: int, open_count: int, rem_l: int, rem_r: int, path: list[str]):
            # If invalid prefix balance, prune
            if open_count < 0:
                return

            # Base condition
            if index == len(s):
                if rem_l == 0 and rem_r == 0 and open_count == 0:
                    result.add("".join(path))
                return

            ch = s[index]

            # Option 1: Remove the character (if it is a bracket and removals left)
            if ch == '(' and rem_l > 0:
                backtrack(index + 1, open_count, rem_l - 1, rem_r, path)
            elif ch == ')' and rem_r > 0:
                backtrack(index + 1, open_count, rem_l, rem_r - 1, path)

            # Option 2: Keep the character
            path.append(ch)
            if ch == '(':
                backtrack(index + 1, open_count + 1, rem_l, rem_r, path)
            elif ch == ')':
                backtrack(index + 1, open_count - 1, rem_l, rem_r, path)
            else:
                backtrack(index + 1, open_count, rem_l, rem_r, path)
            path.pop()

        backtrack(0, 0, rem_l, rem_r, [])
        return list(result)