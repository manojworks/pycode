# class representing a node in a Binary Tree
class BinaryTreeNode:

    def __init__(self, el):
        self._element = el
        self._left = None
        self._right = None

    def element(self, val=None):
        if val is None:
            return self._element
        else:
            self._element = val

    def get_left_node(self):
        return self._left

    def set_left_node_val(self, val):
        self._left = BinaryTreeNode(val)
        return self._left

    def set_left_node(self, node):
        self._left = node

    def get_right_node(self):
        return self._right

    def set_right_node_val(self, val):
        self._right = BinaryTreeNode(val)

    def set_right_node(self, node):
        self._right = node

    def is_leaf(self):
        return self.get_left_node() is None and self.get_right_node() is None


# A class representing a Binary Tree
class BinaryTree:

    def __init__(self, val=None):
        if val is None:
            self._root = None
        else:
            n = BinaryTreeNode(val)
            self._root = n

    # add_node - add a node
    def add_node(self, val):
        if self._root is None:
            n = BinaryTreeNode(val)
            self._root = n
            return
        temp = self._root
        while True:
            if val <= temp.element():
                if temp.get_left_node() is not None:
                    temp = temp.get_left_node()
                else:
                    temp.set_left_node_val(val)
                    break
            else:
                if temp.get_right_node() is not None:
                    temp = temp.get_right_node()
                else:
                    temp.set_right_node_val(val)
                    break

    # Removes the left subtree of the root
    def remove_left_subtree(self, val):
        n, _ = self.find_node_and_parent(val)
        if n is not None:
            n.set_left_node_val(None)

    # Removes the right subtree of the root
    def remove_right_subtree(self, val):
        n, _ = self.find_node_and_parent(val)
        if n is not None:
            n.set_right_node_val(None)

    # Removes all elements from the tree
    def remove_all_elements(self):
        self._root = None

    # Determines if a particular element is in the tree
    def contains(self, val):
        return self.find(val) is not None

    # Returns a string representation of tree’s contents
    def __str__(self):
        ret_str = ""
        for el in self.inorder():
            ret_str += str(el)
            ret_str += ' '
        return ret_str

    # number of nodes in the tree
    def num_nodes(self):
        num_nodes = 0
        for _ in self.inorder():
            num_nodes += 1

        return num_nodes

    # root of the tree
    def get_root(self):
        return self._root

    # Returns an iterator for an inorder traversal
    def iterator_inorder(self, node):
        if node.get_left_node() is not None:
            yield from self.iterator_inorder(node.get_left_node())
        yield node
        if node.get_right_node() is not None:
            yield from self.iterator_inorder(node.get_right_node())

    # inorder traversal through the tee, returning the value
    def inorder(self):
        if self._root is not None:
            for p in self.iterator_inorder(self._root):
                yield p.element()

    # inorder traversal through the tee, returning the node
    def inorder_node(self):
        if self._root is not None:
            for p in self.iterator_inorder(self._root):
                yield p

    # Returns an iterator for a postorder traversal
    def iterator_postorder(self, node):
        if node.get_left_node() is not None:
            yield from self.iterator_postorder(node.get_left_node())
        if node.get_right_node() is not None:
            yield from self.iterator_postorder(node.get_right_node())
        yield node.element()

    # postorder traversal through the tee, returning the node
    def postorder(self):
        if self._root is not None:
            for p in self.iterator_postorder(self._root):
                yield p

    # Returns an iterator for a preorder traversal
    def iterator_preorder(self, node):
        yield node.element()
        if node.get_left_node() is not None:
            yield from self.iterator_preorder(node.get_left_node())
        if node.get_right_node() is not None:
            yield from self.iterator_preorder(node.get_right_node())

    # preorder traversal through the tee, returning the node
    def preorder(self):
        if self._root is not None:
            for p in self.iterator_preorder(self._root):
                yield p

    # Returns an iterator for a levelorder traversal
    def iterator_level_order(self):
        if self._root is None:
            return
        qu = QueueT()
        qu.enqueue(self._root)
        while not qu.is_empty():
            node = qu.dequeue()
            yield node.element()
            if node.get_left_node() is not None:
                qu.enqueue(node.get_left_node())
            if node.get_right_node() is not None:
                qu.enqueue(node.get_right_node())

    # Returns a reference to the specified target and its parent, if found
    def find_node_and_parent(self, val):

        temp = self._root
        par = temp

        while temp is not None and val != temp.element():
            if val < temp.element():
                par = temp
                temp = temp.get_left_node()
            else:
                par = temp
                temp = temp.get_right_node()

        if temp is not None and val == temp.element():
            return temp, par

        return None

    # Determines whether the tree is empty
    def is_empty(self):
        return self.num_nodes() == 0

    # Get minimum node in the tree
    def find_min(self):
        node_iter = self.iterator_inorder(self._root)
        node_min = next(node_iter)
        for node in self.inorder_node():
            if node.element() < node_min.element():
                node_min = node

        return node_min

    # Given two binary trees, return true if they are structurally identical -- they are made of
    # nodes with the same values arranged in the same way.
    def same_tree(self, other_tree):
        it_self = self.inorder()
        it_other = other_tree.inoder()

        while it_self is not None and it_other is not None:
            if next(it_self) != next(it_other):
                return False

    # depth of  the tree from the given node
    def depth(self, node):
        if node is None:
            return 0
        left_depth = self.depth(node.get_left_node())
        right_depth = self.depth((node.get_right_node()))
        return max(left_depth, right_depth) + 1

    # double tree
    def double_tree(self):
        double_bt = BinaryTree(None)
        for el in self.iterator_level_order():
            double_bt.add_node(el)
            double_bt.add_node(el)

        return double_bt

    # remove a node from the tree
    def remove_node(self, val):
        node, par = self.find_node_and_parent(val)

        # if the node is a leaf node
        if node.is_leaf():
            if par.get_left_node() is not None and par.get_left_node().element() == node.element():
                par.set_left_node(None)
            if par.get_right_node() is not None and par.get_right_node().element() == node.element():
                par.set_right_node(None)

        # if the node has only node - left
        if node.get_right_node() is None and node.get_left_node() is not None and node.element() == val:
            if par.get_left_node().element() == val:
                par.set_left_node(node.get_left_node())
            if par.get_right_node().element() == val:
                par.set_right_node(node.get_left_node())

        # if the node has only node - right
        if node.get_left_node() is None and node.get_right_node() is not None and node.element() == val:
            if par.get_left_node().element() == val:
                par.set_left_node(node.get_right_node())
            if par.get_right_node().element() == val:
                par.set_right_node(node.get_right_node())

        # if the node has two children - incomplete
        if node.get_left_node() is not None and node.get_right_node() is not None and node.element() == val:
            succ = node.get_right_node()
            succ_par = node
            while succ.get_left_node() is not None:
                succ_par = succ
                succ = succ.get_left_node()
            node.element(succ.element())
            succ_par.set_left_node(succ.get_right_node())

    # Change a tree so that the roles of the left and right pointers are swapped at every node.
    def mirror(self, node):
        if node is None:
            return

        self.mirror(node.get_left_node())
        self.mirror(node.get_right_node())

        temp = node.get_left_node()
        node.set_left_node(node.get_right_node())
        node.set_right_node(temp)


# driver code
def make_binary_tree():
    bt = BinaryTree(40)
    bt.add_node(3)
    bt.add_node(7)
    bt.add_node(2)
    bt.add_node(301)
    bt.add_node(70)
    bt.add_node(21)

    print(bt.remove_node(3))
###################################################
