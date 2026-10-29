import sys

# Increase recursion depth for deep trees
sys.setrecursionlimit(200000)

class SegmentTree:
    def __init__(self, n, init_vals):
        self.n = n
        self.tree = [0] * (4 * n)
        self.lazy = [0] * (4 * n)
        if init_vals:
            self._build(1, 0, n - 1, init_vals)

    def _build(self, node, l, r, vals):
        if l == r:
            self.tree[node] = vals[l]
            return
        mid = (l + r) // 2
        self._build(2 * node, l, mid, vals)
        self._build(2 * node + 1, mid + 1, r, vals)
        self.tree[node] = self.tree[2 * node] ^ self.tree[2 * node + 1]

    def _apply(self, node, val):
        self.tree[node] ^= val
        self.lazy[node] ^= val

    def _push(self, node):
        if self.lazy[node]:
            self._apply(2 * node, self.lazy[node])
            self._apply(2 * node + 1, self.lazy[node])
            self.lazy[node] = 0

    def update_range(self, node, l, r, ql, qr, val):
        if ql <= l and r <= qr:
            self._apply(node, val)
            return
        self._push(node)
        mid = (l + r) // 2
        if ql <= mid:
            self.update_range(2 * node, l, mid, ql, qr, val)
        if qr > mid:
            self.update_range(2 * node + 1, mid + 1, r, ql, qr, val)
        self.tree[node] = self.tree[2 * node] ^ self.tree[2 * node + 1]

    def query_range(self, node, l, r, ql, qr):
        if ql <= l and r <= qr:
            return self.tree[node]
        self._push(node)
        mid = (l + r) // 2
        res = 0
        if ql <= mid:
            res ^= self.query_range(2 * node, l, mid, ql, qr)
        if qr > mid:
            res ^= self.query_range(2 * node + 1, mid + 1, r, ql, qr)
        return res

class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        parent = [0] * n
        depth = [0] * n
        heavy = [-1] * n
        head = [0] * n
        pos = [0] * n
        sz = [0] * n
        cur_pos = 0

        # First DFS to compute subtree sizes, depths, parents, and heavy children
        def dfs1(u, p, d):
            parent[u] = p
            depth[u] = d
            sz[u] = 1
            max_sub = 0
            for v in adj[u]:
                if v != p:
                    dfs1(v, u, d + 1)
                    sz[u] += sz[v]
                    if sz[v] > max_sub:
                        max_sub = sz[v]
                        heavy[u] = v

        dfs1(0, -1, 0)

        # Second DFS to form heavy-light chains and assign segment positions
        def dfs2(u, h):
            nonlocal cur_pos
            head[u] = h
            pos[u] = cur_pos
            cur_pos += 1
            
            if heavy[u] != -1:
                dfs2(heavy[u], h)
            
            for v in adj[u]:
                if v != parent[u] and v != heavy[u]:
                    dfs2(v, v)

        dfs2(0, 0)

        # Initialize segment tree with bitmask values
        init_vals = [0] * n
        for i in range(n):
            init_vals[pos[i]] = 1 << (ord(s[i]) - ord('a'))

        seg_tree = SegmentTree(n, init_vals)

        # Helper to query path between u and v
        def query_path(u, v):
            res = 0
            while head[u] != head[v]:
                if depth[head[u]] > depth[head[v]]:
                    u, v = v, u
                res ^= seg_tree.query_range(1, 0, n - 1, pos[head[v]], pos[v])
                v = parent[head[v]]
            if depth[u] > depth[v]:
                u, v = v, u
            res ^= seg_tree.query_range(1, 0, n - 1, pos[u], pos[v])
            return res

        ans = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                ui = int(parts[1])
                new_c = parts[2]
                old_mask = 1 << (ord(s[ui]) - ord('a'))
                new_mask = 1 << (ord(new_c) - ord('a'))
                diff = old_mask ^ new_mask
                if diff:
                    s = s[:ui] + new_c + s[ui+1:]
                    # Since update is on a single node, we can directly toggle its value in the segment tree
                    seg_tree.update_range(1, 0, n - 1, pos[ui], pos[ui], diff)
            else:
                ui = int(parts[1])
                vi = int(parts[2])
                mask = query_path(ui, vi)
                # Check if at most one bit is set
                if (mask & (mask - 1)) == 0:
                    ans.append(True)
                else:
                    ans.append(False)

        return ans