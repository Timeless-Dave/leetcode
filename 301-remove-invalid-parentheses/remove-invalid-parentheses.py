class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def is_valid(string: str) -> bool:
            count = 0
            for char in string:
                if char == '(':
                    count += 1
                elif char == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0

        queue = {s}
        while queue:
            # Filter all valid strings at the current level
            valid = [candidate for candidate in queue if is_valid(candidate)]
            if valid:
                return valid
            
            # Generate next level by removing one parenthesis at each index
            next_queue = set()
            for candidate in queue:
                for i, char in enumerate(candidate):
                    if char in '()':
                        next_queue.add(candidate[:i] + candidate[i + 1:])
            queue = next_queue

        return [""]