class BinaryTreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    @staticmethod
    def inorder_tree_walk(root):
        s = []
        node = root
        while node or s:
            if node:
                s.append(node)
                node = node.left
            else:
                cur = s.pop()
                print(cur)
                node = cur.right

    @staticmethod
    def preorder_tree_walk(root):
        s = []
        node = root
        while node or s:
            if node:
                print(node)
                s.append(node.right)
                node = node.left
            else:
                node = s.pop()

    @staticmethod
    def postorder_tree_walk(root):
        s = []
        node = root
        last = None
        while node or s:
            if node:
                s.append(node)
                node = node.left
            else:
                cur = s[0]
                if cur.right and last != cur.right:
                    node = cur.right
                else:
                    print(cur)
                    last = s.pop()

