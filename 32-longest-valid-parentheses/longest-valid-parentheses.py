class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left = right = max_len = 0
        
        # Left to Right pass
        for char in s:
            if char == '(':
                left += 1
            else:
                right += 1
            
            if left == right:
                max_len = max(max_len, 2 * right)
            elif right > left:
                # Invalid state: more ')' than '('
                left = right = 0
                
        left = right = 0
        
        # Right to Left pass
        for char in reversed(s):
            if char == '(':
                left += 1
            else:
                right += 1
            
            if left == right:
                max_len = max(max_len, 2 * left)
            elif left > right:
                # Invalid state: more '(' than ')' when going backwards
                left = right = 0
                
        return max_len