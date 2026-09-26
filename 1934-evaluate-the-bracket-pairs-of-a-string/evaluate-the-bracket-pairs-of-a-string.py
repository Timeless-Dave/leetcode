class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        # dict() is slightly faster and more memory-efficient than a comprehension
        d = dict(knowledge) 
        
        # Split the string by the opening bracket
        parts = s.split('(')
        
        # Process every part that came after an opening bracket
        for i in range(1, len(parts)):
            key, rest = parts[i].split(')')
            # Replace the part in-place to save memory
            parts[i] = d.get(key, '?') + rest 
            
        return "".join(parts)