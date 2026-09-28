class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        
        for char in s:
            if char == ')':
                temp = []
                # Pop characters until we hit the opening parenthesis
                while stack and stack[-1] != '(':
                    temp.append(stack.pop())
                
                stack.pop() # Remove the '('
                
                # Add the reversed characters back to the stack
                stack.extend(temp)
            else:
                stack.append(char)
                
        return "".join(stack)