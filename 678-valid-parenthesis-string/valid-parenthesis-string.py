class Solution:
    def checkValidString(self, s: str) -> bool:
        min_open = 0  # Minimum possible number of open parentheses
        max_open = 0  # Maximum possible number of open parentheses
        
        for char in s:
            if char == '(':
                min_open += 1
                max_open += 1
            elif char == ')':
                min_open = max(0, min_open - 1)
                max_open -= 1
            else:  # char == '*'
                min_open = max(0, min_open - 1) # Treat '*' as ')' or empty
                max_open += 1                   # Treat '*' as '('
            
            # If the maximum possible open parentheses is less than 0, 
            # it means there are too many ')' that cannot be matched.
            if max_open < 0:
                return False
                
        # If min_open is 0, it means we can successfully match all '('
        return min_open == 0