class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        d = dict(knowledge)
        ans = []
        prev = 0
        
        while True:
            # Find the next opening bracket
            start = s.find('(', prev)
            if start == -1:
                # No more brackets, append the rest of the string and finish
                ans.append(s[prev:])
                break
                
            # Append the characters before the bracket
            ans.append(s[prev:start])
            
            # Find the closing bracket
            end = s.find(')', start + 1)
            
            # Lookup the key (slicing the string between the brackets)
            ans.append(d.get(s[start + 1:end], '?'))
            
            # Update the pointer for the next iteration
            prev = end + 1
            
        return "".join(ans)