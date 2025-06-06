class Tree:
    def __init__(self, node):
        self.node = node
        self.children = [Tree(child) for child in node.get('children', [])]

    def get_element_by_id(self, target_id):
        # Check current node
        if self.node.get('id') == target_id:
            return self.node

        # Recursively check children
        for child in self.children:
            result = child.get_element_by_id(target_id)
            if result is not None:
                return result

        # If not found
        return None

