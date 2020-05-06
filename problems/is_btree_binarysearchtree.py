from adt_impl.binary_node import BinaryNode
from visualization import binary_tree_visualizer


def is_binary_tree_binary_search_tree(btree: BinaryNode):
    """Check if the given binary tree is a binary search tree or not.
    
    Arguments:
        btree {BinaryNode} -- Binary tree, implemented as recursive nodes, where the node class implements the __iter__ function for overriding the for x in operation.
    
    Returns:
        [type] -- True if the tree holds binary search tree properties, False otherwise.
    """
    prev = None
    for node in btree:
        if prev != None:
            if prev > node:
                return False
        prev = node
    return True


def generate_non_bs_tree_example() -> BinaryNode:
    non_bs_tree = BinaryNode(6)
    non_bs_tree.insert_left(3)
    non_bs_tree.left.insert_left(2)
    non_bs_tree.left.insert_right(4)
    non_bs_tree.insert_right(10)
    non_bs_tree.right.insert_left(5)
    non_bs_tree.right.insert_right(13)
    return non_bs_tree


def generate_bs_tree_example() -> BinaryNode:
    bs_tree = BinaryNode(6)
    bs_tree.insert_left(3)
    bs_tree.left.insert_left(2)
    bs_tree.left.insert_right(4)
    bs_tree.insert_right(10)
    bs_tree.right.insert_left(9)
    bs_tree.right.insert_right(13)
    return bs_tree


# TODO: Move to tests
if __name__ == "__main__":
    non_bs_tree = generate_non_bs_tree_example()
    bs_tree = generate_bs_tree_example()

    # Visualize to check how the trees looks like
    non_bs_dot = binary_tree_visualizer.visualize(non_bs_tree)
    non_bs_dot.view(
        filename="not a search binary_tree", directory="./visualization/examples/output"
    )

    bs_dot = binary_tree_visualizer.visualize(bs_tree)
    bs_dot.view(
        filename="a search binary_tree", directory="./visualization/examples/output"
    )

    assert is_binary_tree_binary_search_tree(non_bs_tree) == False
    assert is_binary_tree_binary_search_tree(bs_tree) == True
