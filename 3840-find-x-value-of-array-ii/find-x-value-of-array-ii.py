from typing import List

class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        
        # Find next power of 2 for the segment tree size
        N = 1
        while N < n:
            N <<= 1
            
        # prod[i] stores the total product of the range modulo k
        prod = [1] * (2 * N)
        # cnt[i][x] stores the number of valid prefixes in the range that evaluate to x modulo k
        cnt = [[0] * k for _ in range(2 * N)]
        
        # Initialize leaves
        for i in range(n):
            v = nums[i] % k
            prod[N + i] = v
            cnt[N + i][v] = 1
            
        # Build the tree initially
        for i in range(N - 1, 0, -1):
            left = 2 * i
            right = left + 1
            pL = prod[left]
            prod[i] = (pL * prod[right]) % k
            
            for x in range(k):
                cnt[i][x] = cnt[left][x]
            for x in range(k):
                c = cnt[right][x]
                if c:
                    cnt[i][(pL * x) % k] += c
                    
        def update(idx: int, val: int):
            node = N + idx
            v = val % k
            
            # Update leaf
            prod[node] = v
            for i in range(k):
                cnt[node][i] = 0
            cnt[node][v] = 1
            
            # Update ancestors
            node //= 2
            while node > 0:
                left = 2 * node
                right = left + 1
                pL = prod[left]
                prod[node] = (pL * prod[right]) % k
                
                # A prefix of the parent is either a prefix of the left child...
                for i in range(k):
                    cnt[node][i] = cnt[left][i]
                # ...or the entire left child combined with a prefix of the right child
                for x in range(k):
                    c = cnt[right][x]
                    if c:
                        cnt[node][(pL * x) % k] += c
                node //= 2
                
        def query(L: int, R: int) -> List[int]:
            L += N
            R += N
            left_nodes = []
            right_nodes = []
            
            # Identify the nodes that cover the query range
            while L <= R:
                if L % 2 == 1:
                    left_nodes.append(L)
                    L += 1
                if R % 2 == 0:
                    right_nodes.append(R)
                    R -= 1
                L //= 2
                R //= 2
                
            curr_prod = 1
            curr_cnt = [0] * k
            
            # Process left-to-right to maintain proper prefix ordering
            for node in left_nodes:
                for x in range(k):
                    c = cnt[node][x]
                    if c:
                        curr_cnt[(curr_prod * x) % k] += c
                curr_prod = (curr_prod * prod[node]) % k
                
            for node in reversed(right_nodes):
                for x in range(k):
                    c = cnt[node][x]
                    if c:
                        curr_cnt[(curr_prod * x) % k] += c
                curr_prod = (curr_prod * prod[node]) % k
                
            return curr_cnt
            
        ans = []
        for idx, val, start, xi in queries:
            update(idx, val)
            # The query essentially asks us to find frequencies over the range [start, n-1]
            ans.append(query(start, n - 1)[xi])
            
        return ans