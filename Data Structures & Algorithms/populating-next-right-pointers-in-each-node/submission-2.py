"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        '''

        BFS - stack 
        level by level traversal 
            add left, then right neighbor 
        
        for each level 
        
        pop node from stack 
        if stack.peek() make that the node's next
        if not , continue with the next ptr as null 
        
        return the root 

        '''
        if not root:
            return None

        # init deque 
        q = deque([root])


        # lvl by lvl traversal
        while q:
            k = len(q)
            while k:
                node = q.popleft()
                # assign next field 
                if k > 1:
                    node.next = q[0]
                if node.right and node.left:
                    q.append(node.left)
                    q.append(node.right)
                k -= 1
                
                

        return root
        # return root 