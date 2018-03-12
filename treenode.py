class treenode():
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

   
class traversal():
    def __init__(self):
        self.path = []

    def preorder(self, treenode):
        if treenode:
            self.path.append(treenode)
            self.preorder(treenode.left)
            self.preorder(treenode.right)

    def inorder(self, treenode):
        if treenode:
            self.inorder(treenode.left)
            self.path.append(treenode)
            self.inorder(treenode.right)

    def postorder(self, treenode):
        if treenode:
            self.postorder(treenode.left)
            self.postorder(treenode.right)
            self.path.append(treenode)
