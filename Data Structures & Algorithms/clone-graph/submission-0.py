"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        mapping = {}
        mapping[node] = Node(node.val)
        q = collections.deque([node])

        while q:
            cur = q.popleft()
            for nei in cur.neighbors:
                if nei not in mapping:
                    mapping[nei] = Node(nei.val)
                    q.append(nei)
                mapping[cur].neighbors.append(mapping[nei])
        return mapping[node]
        