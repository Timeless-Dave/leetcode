class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        queue = [expression]
        res = set()
        
        while queue:
            curr = queue.pop(0)
            
            # If there are no braces, it's a fully expanded word
            if '{' not in curr:
                res.add(curr)
                continue
            
            # Find the first closing brace
            right = curr.find('}')
            # Find the corresponding innermost opening brace
            left = curr.rfind('{', 0, right)
            
            # Split the string into three parts: before, inside, and after the brace
            before = curr[:left]
            after = curr[right+1:]
            inside = curr[left+1:right].split(',')
            
            # Expand the current brace and add new combinations to the queue
            for item in inside:
                queue.append(before + item + after)
                
        # Return sorted unique words
        return sorted(list(res))