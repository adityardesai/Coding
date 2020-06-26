class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def dfs_helper(root, result_so_far):

    if not root:
        return 0

    result_so_far = 10 * result_so_far + root.val

    if not root.left and not root.right:
        return result_so_far

    return dfs_helper(root.left, result_so_far) + dfs_helper(
        root.right, result_so_far)


def find_sum_of_path_numbers(root):
    if not root:
        return 0

    return dfs_helper(root, 0)


def main():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)
    print("Total Sum of Path Numbers: " + str(find_sum_of_path_numbers(root)))


main()
