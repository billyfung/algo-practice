# input is a binary tree


class BinaryTreeNode:
    def __init__(self, value):
        self.value = None
        self.left = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

    def is_balanced(tree_root):
        # check tree to ensure that difference between depths of any two leaf nodes no greater than one
        # only two distinct leaf depths, at most 1 apart
        # we use DFS because we will hit leaves first, allowing us to check faster
        depths = []
        # used to store (node, depth)
        nodes = [(tree_root, 0)]

        while len(nodes):
            # pop a node,depth from stack
            node, depth = nodes.pop()
            if (not node.left) and (not node.right):
                # leaf is found
                if depth not in depths:
                    depths.append(depth)
                    if (len(depth) > 2) or (len(depths) == 2 and abs(depths[0] - depths[1]) > 1):
                        return False
            else:
                if node.left:
                    nodes.append((node.left, depth + 1))
                if node.right:
                    nodes.append((node.right, depth + 1))
        return True

    def is_bst(tree_root):
        # checks that it is a binary search tree
        # left tree values < right tree values
        # so check nodes to make sure they are smaller than ancestor on right
        # keep track of lower bound and upper bound that node must be in
        stack = [(tree_root, -9999999, 9999999)]
        # DFS
        while len(stack):
            node, lower_bound, upper_bound = stack.pop()
            if (node.value<lower_bound) or (node.value>upper_bound):
                return False

            if node.left:
                # this node must be less than
                stack.append((node.left, lower_bound, node.value))
            if node.right:
                # this node must be greater
                stack.append((node.right, node.value, upper_bound))

        return True

    def find_largest(tree_root):
        # find the largest value in a BST
        # should walk down right side to get largest value
        current = tree_root
        while current:
            if not current.right:
                return current
            current = current.right

    def find_2nd_largest(tree_root):
        if not(tree_root.left or tree_root.right):
            raise Exception("Not a tree")

        current = tree_root

        while current:
            # 3 different cases for 2nd largest
            # has left subtree only, so current is largest
            # 2nd largest is largest in left tree
            if current.left and not current.right:
                return find_largest(current.left)

            # case: there is right child but right child has no children
            # largest must be on right, then current is 2nd largest
            if current.right and not current.left.right and not current.right.right:
                return current.value

            # case: there is a right subtree with children, so largest and 2nd largest must be in there 
            current = current.right



