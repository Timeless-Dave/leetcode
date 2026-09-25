class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        stack = []
        union_set = set()
        current_product = {""}
        
        for char in expression:
            if char == '{':
                # Push current state to stack and reset for the new block
                stack.append((union_set, current_product))
                union_set = set()
                current_product = {""}
                
            elif char == '}':
                # Resolve the inner group (union of what we've accumulated)
                inner_group = union_set.union(current_product)
                
                # Pop the previous state
                prev_union, prev_product = stack.pop()
                union_set = prev_union
                
                # Multiply the previous product by the resolved inner group
                current_product = {p + c for p in prev_product for c in inner_group}
                
            elif char == ',':
                # Commas separate unions, so add to union_set and reset product
                union_set.update(current_product)
                current_product = {""}
                
            else:
                # It's a letter, simply concatenate it to all items in current_product
                current_product = {p + char for p in current_product}
                
        # Final union of the top-level items
        final_set = union_set.union(current_product)
        
        return sorted(list(final_set))