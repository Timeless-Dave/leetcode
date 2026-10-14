class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        # Check if the sum is within the valid range of digits (0 to 9 * num)
        if sum < 0 or sum > 9 * num:
            return ""
        
        # We need `num` digits, initialized to 0
        res = [0] * num
        
        # Greedily assign 9 to the leftmost positions as much as possible
        for i in range(num):
            if sum >= 9:
                res[i] = 9
                sum -= 9
            else:
                res[i] = sum
                sum = 0
                break
                
        return "".join(map(str, res))