class Solution:
    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        pair = [0] * n
        stack = []
        
        # Step 1: Find and store the matching parenthesis pairs
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                j = stack.pop()
                pair[i] = j
                pair[j] = i
                
        # Step 2: Traverse the string and build the result
        res = []
        i = 0
        direction = 1 # 1 means forward, -1 means backward
        
        while i < n:
            if s[i] == '(' or s[i] == ')':
                # Teleport to the matching parenthesis and reverse direction
                i = pair[i]
                direction = -direction
            else:
                res.append(s[i])
            
            i += direction
            
        return "".join(res)