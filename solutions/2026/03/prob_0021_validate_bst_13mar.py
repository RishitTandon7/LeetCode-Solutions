def validateBST(root):
    def check(node, min_val=float('-inf'), max_val=float('inf')):
        if not node:
            return True
        if node.val <= min_val or node.val >= max_val:
            return False
        return (check(node.left, min_val, node.val) and 
                check(node.right, node.val, max_val))

    return check(root)