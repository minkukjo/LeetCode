# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        adj = defaultdict(list)

        q = []
        q.append(root)

        while q:
            node = q.pop()

            if node.left:
                adj[node.val].append(node.left.val)
                adj[node.left.val].append(node.val)
                q.append(node.left)
            if node.right:
                adj[node.val].append(node.right.val)
                adj[node.right.val].append(node.val)
                q.append(node.right)
        
        
        distance = defaultdict(int)
        q_distance = []
        q_distance.append(target.val)

        while q_distance:
            parent = q_distance.pop()

            for adj_node in adj[parent]:
                if adj_node not in distance:
                    distance[adj_node] = distance[parent] + 1
                    q_distance.append(adj_node)
        ans = []
        print(distance)
        for key, value in distance.items():
            if value == k:
                ans.append(key)
        return ans



            

