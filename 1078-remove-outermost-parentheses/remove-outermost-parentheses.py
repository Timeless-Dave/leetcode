class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = []
        opened = 0
        
        for char in s:
            if char == '(':
                # Only include '(' if it's not the outermost opening parenthesis
                if opened > 0:
                    res.append(char)
                opened += 1
            else:
                opened -= 1
                # Only include ')' if it's not the outermost closing parenthesis
                if opened > 0:
                    res.append(char)
                    
        return "".join(res)