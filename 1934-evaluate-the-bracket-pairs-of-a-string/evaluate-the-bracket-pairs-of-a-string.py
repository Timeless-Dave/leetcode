class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        # Convert knowledge into a dictionary for O(1) lookups
        know_dict = {k: v for k, v in knowledge}
        
        ans = []
        curr_key = []
        in_bracket = False
        
        for char in s:
            if char == '(':
                in_bracket = True
            elif char == ')':
                in_bracket = False
                key = "".join(curr_key)
                # Append the known value or "?" if it doesn't exist
                ans.append(know_dict.get(key, "?"))
                curr_key = []  # Reset for the next key
            else:
                if in_bracket:
                    curr_key.append(char)
                else:
                    ans.append(char)
                    
        return "".join(ans)