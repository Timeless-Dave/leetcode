import math

class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        
        def helper(arr):
            if len(arr) <= 2:
                return 1
            
            root = arr[0]
            left = [x for x in arr if x < root]
            right = [x for x in arr if x > root]
            
            # Combinatorics: choose len(left) positions out of len(left) + len(right)
            ways_comb = math.comb(len(left) + len(right), len(left))
            
            # Recursively compute ways for left and right subtrees
            ways_left = helper(left)
            ways_right = helper(right)
            
            return (ways_comb * ways_left * ways_right) % MOD

        # Subtract 1 because we want *reorderings* (excluding the original array)
        return (helper(nums) - 1) % MOD