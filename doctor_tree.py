class DoctorNode:
     def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None



class DoctorTree:
    def __init__(self):
        self.root = None

    def insert(self, parent_name, doctor_name, side, current_node=None):
        if self.root is None:
            print("⚠️ No root doctor exists. Add root first.")
            return

        if current_node is None:
            current_node = self.root

        if current_node.name == parent_name:
            if side.lower() == "left":
                if current_node.left is None:
                    current_node.left = DoctorNode(doctor_name)
                    print(f"✅ {doctor_name} added to the LEFT of {parent_name}")
                else:
                    print(f"⚠️ LEFT of {parent_name} is already occupied.")
            elif side.lower() == "right":
                if current_node.right is None:
                    current_node.right = DoctorNode(doctor_name)
                    print(f"✅ {doctor_name} added to the RIGHT of {parent_name}")
                else:
                    print(f"⚠️ RIGHT of {parent_name} is already occupied.")
            else:
                print("⚠️ Invalid side. Choose 'left' or 'right'.")
            return

        if current_node.left:
            self.insert(parent_name, doctor_name, side, current_node.left)
        if current_node.right:
            self.insert(parent_name, doctor_name, side, current_node.right)

    def preorder(self, node):
        if node is None:
            return []
        return [node.name] + self.preorder(node.left) + self.preorder(node.right)

    def inorder(self, node):
        if node is None:
            return []
        return self.inorder(node.left) + [node.name] + self.inorder(node.right)

    def postorder(self, node):
        if node is None:
            return []
        return self.postorder(node.left) + self.postorder(node.right) + [node.name]





# Test your DoctorTree and DoctorNode classes here
if __name__ == "__main__":
    tree = DoctorTree()
    tree.root = DoctorNode("Dr. Croft")
    tree.insert("Dr. Croft", "Dr. Goldsmith", "right")
    tree.insert("Dr. Croft", "Dr. Phan", "left")
    tree.insert("Dr. Phan", "Dr. Carson", "right")
    tree.insert("Dr. Phan", "Dr. Morgan", "left")

    print(tree.preorder(tree.root))   # ['Dr. Croft', 'Dr. Phan', 'Dr. Morgan', 'Dr. Carson', 'Dr. Goldsmith']
    print(tree.inorder(tree.root))    # ['Dr. Morgan', 'Dr. Phan', 'Dr. Carson', 'Dr. Croft', 'Dr. Goldsmith']
    print(tree.postorder(tree.root))  # ['Dr. Morgan', 'Dr. Carson', 'Dr. Phan', 'Dr. Goldsmith', 'Dr. Croft']
