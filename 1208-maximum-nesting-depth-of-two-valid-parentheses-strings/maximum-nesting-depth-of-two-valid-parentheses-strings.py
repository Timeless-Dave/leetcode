class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        # Assign '(' to alternate groups, and ')' to the opposite of what '(' would get at that index
        return [i % 2 if char == ')' else 1 - (i % 2) for i, char in enumerate(seq)]