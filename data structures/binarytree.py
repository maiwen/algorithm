class binarytree:
    def __init__(self, node):
        self.key = node
        self.left = None
        self.right = None
    
    def insert_left(self, node):
        if self.left == None:
            self.left = binarytree(node)
        else:
            t = binarytree(node)
            t.left = self.left
            self.left = t
            
    def insert_right(self, node):
        if self.right == None:
            self.right = binarytree(node)
        else:
            t = binarytree(node)
            t.right = self.right
            self.right = t
            
    def get_right_child(self):
        return self.right
    def get_left_child(self):
        return self.left
    def set_root_val(self, obj):
        self.key = obj
    def get_root_val(self):
        return self.key
    
r = binarytree('a')
print(r.get_root_val())
print(r.get_left_child())
r.insert_left('b')
print(r.get_left_child())
print(r.get_left_child().get_root_val())
r.insert_right('c')
print(r.get_right_child())
print(r.get_right_child().get_root_val())
r.get_right_child().set_root_val('hello')
print(r.get_right_child().get_root_val())