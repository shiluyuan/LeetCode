"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”

        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4
For example, the lowest common ancestor (LCA) of nodes 5 and 1 is 3. Another example is LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

"""
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        stack = [root]
        parent = {root: None}
        while p not in parent or q not in parent:
            node = stack.pop()
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent[p]
        while q not in ancestors:
            q = parent[q]
        return q

#recursion:
class Solution1(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        if not root or root==p or root==q:
            return root
            
        if self.isnode(p,q):
            return p
        if self.isnode(q,p):
            return q
            
        if self.isnode(root.left,p) and self.isnode(root.left,q):
            return self.lowestCommonAncestor(root.left, p, q)
        elif self.isnode(root.right,p) and self.isnode(root.right,q):
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
                
        
    def isnode(self,mother,child):
        if mother:
            if mother==child:
                return True
            else:
                return self.isnode(mother.left,child) or self.isnode(mother.right,child)
        return False