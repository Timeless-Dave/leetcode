class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        d = dict(knowledge)
        
        # Split once to separate out the keys
        parts = s.split('(')
        
        # The first part is always standard text (before any bracket)
        res = [parts[0]]
        
        for part in parts[1:]:
            # Split exactly once at the closing bracket
            key, rest = part.split(')')
            
            # Append the dictionary lookup and the rest of the string separately
            # This completely avoids using the `+` operator, saving memory overhead.
            res.append(d.get(key, '?'))
            res.append(rest)
            
        return "".join(res)