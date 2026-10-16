class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (4 * n)
        self.lazy = [0] * (4 * n)
        self.sum_val = [0] * (4 * n)
        self.MOD = 10**9 + 7

    def _push(self, node, l, r):
        if self.lazy[node] != 0:
            add = self.lazy[node]
            mid = (l + r) // 2
            
            # Left child update
            left = 2 * node
            length_left = mid - l + 1
            self.lazy[left] = (self.lazy[left] + add) % self.MOD
            # sum_val update: old_sum + 2 * add * old_tree + add^2 * length
            self.sum_val[left] = (self.sum_val[left] + 2 * add * self.tree[left] + add * add * length_left) % self.MOD
            self.tree[left] = (self.tree[left] + add * length_left) % self.MOD
            
            # Right child update
            right = 2 * node + 1
            length_right = r - mid
            self.lazy[right] = (self.lazy[right] + add) % self.MOD
            self.sum_val[right] = (self.sum_val[right] + 2 * add * self.tree[right] + add * add * length_right) % self.MOD
            self.tree[right] = (self.tree[right] + add * length_right) % self.MOD
            
            self.lazy[node] = 0

    def update(self, node, l, r, ql, qr, val):
        if ql > r or qr < l:
            return
        if ql <= l and r <= qr:
            length = r - l + 1
            self.lazy[node] = (self.lazy[node] + val) % self.MOD
            self.sum_val[node] = (self.sum_val[node] + 2 * val * self.tree[node] + val * val * length) % self.MOD
            self.tree[node] = (self.tree[node] + val * length) % self.MOD
            return
        
        self._push(node, l, r)
        mid = (l + r) // 2
        self.update(2 * node, l, mid, ql, qr, val)
        self.update(2 * node + 1, mid + 1, r, ql, qr, val)
        
        self.tree[node] = (self.tree[2 * node] + self.tree[2 * node + 1]) % self.MOD
        self.sum_val[node] = (self.sum_val[2 * node] + self.sum_val[2 * node + 1]) % self.MOD

    def query_sum(self, node, l, r, ql, qr):
        if ql > r or qr < l:
            return 0
        if ql <= l and r <= qr:
            return self.sum_val[node]
        
        self._push(node, l, r)
        mid = (l + r) // 2
        res = (self.query_sum(2 * node, l, mid, ql, qr) + 
               self.query_sum(2 * node + 1, mid + 1, r, ql, qr)) % self.MOD
        return res

class Solution:
    MOD = 10**9 + 7

    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        tree = SegmentTree(n)
        last_occurrence = {}
        
        total_sum = 0
        current_sum = 0
        
        for i, x in enumerate(nums):
            prev_idx = last_occurrence.get(x, -1)
            tree.update(1, 0, n - 1, prev_idx + 1, i, 1)
            last_occurrence[x] = i
            
            current_sum = tree.query_sum(1, 0, n - 1, 0, i)
            total_sum = (total_sum + current_sum) % self.MOD
            
        return total_sum