class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_len = 0
        # Initialize stack with -1 to handle valid substrings starting at index 0
        stack = [-1] 
        
        for i, char in enumerate(s):
            if char == '(':
                # Push the index of the open parenthesis
                stack.append(i)
            else:
                # Pop the top element for a matching close parenthesis
                stack.pop()
                
                if not stack:
                    # If the stack is empty, it means we have an unmatched ')'
                    # Push its index to serve as the new base for future valid strings
                    stack.append(i)
                else:
                    # The length is the current index minus the index at the top of the stack
                    max_len = max(max_len, i - stack[-1])
                    
        return max_len