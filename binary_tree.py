class BinaryTreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    @staticmethod
    def print_all_recursive(root):
        if not root:
            return
        print(root.val)
        BinaryTree.print_all(root.left)
        BinaryTree.print_all(root.right)

    @staticmethod
    def print_all(root):
        if not root:
            return
        s = [root]
        while s:
            cur = s.pop()
            print(cur.val)
            if cur.left:
                s.append(cur.left)
            if cur.right:
                s.append(cur.right)       
