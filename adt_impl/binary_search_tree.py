from __future__ import annotations
from adt_impl.binary_search_tree_node import BSTNode


class BinarySearchTree:
    """Implement a binary search tree, where the keys that are less than their parent key are found in the left subtree, and keys that are greater than the parent key are found in the right subtree.
    The skeleton of the implementation is based on this great free Runestone Academy resource at https://runestone.academy/runestone/books/published/pythonds/Trees/SearchTreeImplementation.html
    """

    def __init__(self):
        self.root: BSTNode = None
        self.size = 0

    def __len__(self) -> int:
        """Return the total number of nodes in the BST.
        
        Returns:
            int -- No.of nodes
        """
        return self.size

    def __iter__(self) -> BSTNode:
        """Implement the "for x in" operation for the iteration of the BST.
        
        Returns:
            BSTNode -- The current node for the iterated step.
        """
        return self.root.__iter__()

    def __getitem__(self, key: object) -> object:
        """Implement indexing for the BST.
        
        Arguments:
            key {object} -- Key to search for the object in the BST.
        
        Returns:
            object -- Stored object associated with the key.
        """
        return self.get(key)

    def __setitem__(self, key: object, val: object) -> None:
        """Overload the [] operator for the BST.
        
        Arguments:
            key {object} -- Key to associate the object to store.
            val {object} -- Object to store in the BST.
        """
        self.put(key, val)

    def __contains__(self, key: object) -> bool:
        """Implement the `in` operation for the BST.
        
        Arguments:
            key {object} -- Associated key for the object to check. 
        
        Returns:
            bool -- True if the key is in the BST, False otherwise.
        """
        return True if self._get(key, self.root) else False

    def __delitem__(self, key: object) -> None:
        """Clean up the BST references when a key-val pair is removed with the `del` keyword. 
        
        Arguments:
            key {object} -- Associated key for the deleted object.
        """
        self.remove(key)

    def _put(self, key: object, val: object, current_node: BSTNode) -> None:
        """Add a key-value pair to the BST.
        
        Arguments:
            key {object} -- Key to associate with the value
            val {object} -- Value to associate with the key
            current_node {BSTNode} -- Starting point node to explore where to insert the new key
        """
        if key < current_node.key:  # explore the left sub
            if current_node.left:
                self._put(key, val, current_node.left)
            else:
                current_node.left = BSTNode(key, val, parent=current_node)
        else:  # explore the right sub
            if current_node.right:
                self._put(key, val, current_node.right)
            else:
                current_node.right = BSTNode(key, val, parent=current_node)

    def put(self, key: object, val: object) -> None:
        """Add a key-value pair to the BST.
        
        Arguments:
            key {object} -- Key to associate with the value
            val {object} -- Value to associate with the key
        
        """
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = BSTNode(key, val)
        self.size += 1

    def _get(self, key: object, current_node: BSTNode) -> BSTNode:
        """Get the payload related with the key in the BST.
        
        Arguments:
            key {object} -- The key to fetch the value pair
            current_node {BSTNode} -- The node to start the search from.
        
        Returns:
            BSTNode -- Node with the related key if the key exists, None otherwise.
        """
        if not current_node:
            return None
        elif current_node.key == key:
            return current_node
        elif key < current_node.key:
            return self._get(key, current_node.left)
        else:
            return self._get(key, current_node.right)

    def get(self, key: object) -> BSTNode:
        """Get the payload related with the key in the BST.
        
        Arguments:
            key {object} -- The key to fetch the value pair
        
        Returns:
            BSTNode -- Node with the related key if the key exists, None otherwise.
        """
        if self.root:
            res = self._get(key, self.root)
            return res.val if res else None
        else:
            return None

    def _remove(self, current_node: BSTNode) -> None:
        """Remove the given node from the BST.
        Handle 3 cases:
        1. Node to remove has no children, i.e. "is leaf" => Delete the node and remove the references to this node in the parent.
        2. Node to remove has only one child => Put the child in place of the parent
            2. 1. If this only child is the left child:
                2. 1. 1. If the node to remove is a LEFT child itself, the orphaned child becomes the LEFT child of node-to-remove's parent.
                2. 1. 2. If the node to remove is a RIGHT child itself, the orphaned child becomes the RIGHT child of node to remove's parent.
                2. 1. 3. If the node to remove is not a child, it means that it's the root. So this orphaned child becomes the new root of the tree.
            2. 2 If this only child is the right child, the same rules apply: 
                2. 2. 1. If the node to remove is a LEFT child itself, the orphaned child becomes the LEFT child of node-to-remove's parent.
                2. 2. 2.  If the node to remove is a RIGHT child itself, the orphaned child becomes the RIGHT child of node to remove's parent.
                2. 2. 3. If the node to remove is not a child, it means that it's the root. So this orphaned child becomes the new root of the tree.
        3. Node to remove has two children => 
            - Find the next largest value in the tree (i.e. the successor). 
            - Remove this successor node from the tree first. This successor with the next largest key is guaranteed to have at most 1 child. Removing the successor follows the same rules as outlined in case #2 above.
            - Take the successor's key-value and replace it on the place of the node-to-remove.
        Arguments:
            current_node {BSTNode} -- Node to remove.
        """
        if current_node.is_leaf():  # Case 1
            if current_node == current_node.parent.left:
                current_node.parent.left = None
            else:
                current_node.parent.right = None
        elif current_node.has_both_children():  # Case 3
            succ = current_node.find_successor()
            succ.splice_out()
            current_node.key = succ.key
            current_node.payload = succ.val
        else:  # Case 2
            if current_node.left:  # Case 2.1
                if current_node.is_left():  # Case 2.1.1.
                    current_node.left.parent = current_node.parent
                    current_node.parent.left = current_node.left
                elif current_node.is_right():  # Case 2.1.2
                    current_node.left.parent = current_node.parent
                    current_node.parent.right = current_node.left
                else:  # Case 2.1.3
                    current_node.replace(
                        current_node.left.key,
                        current_node.left.val,
                        current_node.left.left,
                        current_node.left.right,
                    )
            else:
                if current_node.is_left():  # Case 2.2.1
                    current_node.right.parent = current_node.parent
                    current_node.parent.left = current_node.right
                elif current_node.is_right():  # Case 2.2.2
                    current_node.right.parent = current_node.parent
                    current_node.parent.rightChild = current_node.right
                else:  # Case 2.2.3
                    current_node.replace(
                        current_node.right.key,
                        current_node.right.val,
                        current_node.right.left,
                        current_node.right.right,
                    )

    ERR_NONEXISTING_KEY = "The key to delete does not exist."

    def remove(self, key: object) -> None:
        """Remove the given key from the BST or raise an exception if the key is not there.
        
        Arguments:
            key {object} -- Key to remove
        
        Raises:
            KeyError: When the key to remove does not exist in the BST.
        """
        if self.size > 1:
            to_remove = self._get(key, self.root)
            if to_remove:
                self._remove(to_remove)
                self.size = self.size - 1
            else:
                raise KeyError(ERR_NONEXISTING_KEY)
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError(ERR_NONEXISTING_KEY)
