# class Solution:
#     def isValid(self, s: str) -> bool:
#         # open , close = 0, 1

#         # if s[]

#         #two pointers, will start from 0 and 1.. if 0 is open, and 1 is a closing match, we pop the two, if 1 is a closing but not a match, we return fals, if 1 is open, then we move the two pointers, 1,2... and start with the check again....
       
#         # Quick check: if the length is odd, it's impossible to be valid
#         if len(s) % 2 != 0:
#             return False
            
#         # Convert string to a list so we can actually "pop" items out of it
#         s_list = list(s)
#         hashmap = {")": "(", "}": "{", "]": "["}
        
#         p0, p1 = 0, 1
        
#         # Keep going as long as p1 hasn't fallen off the edge of the shrinking list
#         while p1 < len(s_list):
            
#             # EDGE CASE: If p0 is ever pointing to a closing bracket, it's invalid
#             if s_list[p0] in hashmap:
#                 return False
                
#             # If p1 is pointing to an OPEN bracket, move both pointers forward
#             if s_list[p1] not in hashmap:
#                 p0 = p1
#                 p1 += 1
                
#             # If p1 is pointing to a CLOSING bracket
#             else:
#                 # Check if it matches the open bracket at p0
#                 if hashmap[s_list[p1]] == s_list[p0]:
#                     # MATCH! Pop them both out. 
#                     # CRITICAL: Always pop the higher index (p1) first. 
#                     # If you pop p0 first, everything shifts left and p1 points to the wrong thing!
#                     s_list.pop(p1)
#                     s_list.pop(p0)
                    
#                     # Restart the check from the beginning as you suggested
#                     p0, p1 = 0, 1
                    
#                 else:
#                     # Closing bracket, but NOT a match. Return False straight away.
#                     return False
                    
#         # If we successfully popped everything, the list will be empty
#         return len(s_list) == 0      
       
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
            
        s_list = list(s)
        hashmap = {")": "(", "}": "{", "]": "["}
        
        # write_ptr tracks where the next OPEN bracket should be saved
        write_ptr = 0 
        
        # read_ptr scans every character exactly once (O(N) time)
        for read_ptr in range(len(s_list)):
            char = s_list[read_ptr]
            
            # If it's an OPEN bracket, write it down and move write_ptr forward
            if char not in hashmap:
                s_list[write_ptr] = char
                write_ptr += 1
                
            # If it's a CLOSE bracket
            else:
                # Check if there is a previously written open bracket to match with
                # write_ptr - 1 is the most recently seen open bracket
                if write_ptr > 0 and s_list[write_ptr - 1] == hashmap[char]:
                    # MATCH! Step the write pointer back. 
                    # This effectively "deletes" the open bracket without shifting any lists!
                    write_ptr -= 1
                else:
                    return False
                    
        # If write_ptr is back to 0, all brackets were matched and canceled out
        return write_ptr == 0      
       
       
       
       
       
       
       
       
       
       
       
       
        # stack=[]

        # hashmap={")":"(", "}":"{", "]":"["}



        # for char in s:
        #     if char == "(" or char == "{" or char == "[":
        #         stack.append(char)
        #     elif char == ")" or char==  "}" or char == "]":
        #         if len(stack) > 0:
        #             if hashmap[char] == stack[-1]:
        #                 stack.pop()
        #             else: return False
        #         else: return False
        #     else: return False
        # if len(stack) == 0:
        #     return True
        # else: return False
       