class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []

        def backtrack(current_string, left_count, right_count):
            # Base case: if the string length is 2*n, we've formed a valid combination
            if len(current_string) == 2 * n:
                res.append(current_string)
                return
            
            # We can add a left parenthesis if we haven't used all 'n' of them
            if left_count < n:
                backtrack(current_string + "(", left_count + 1, right_count)
            
            # We can add a right parenthesis only if it has a matching left one
            if right_count < left_count:
                backtrack(current_string + ")", left_count, right_count + 1)

        backtrack("", 0, 0)
        return res