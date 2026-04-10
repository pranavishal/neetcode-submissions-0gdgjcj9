# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        ser_str = ""
        def preorder(node):
            nonlocal ser_str
            if not node:
                ser_str += ",N"
                return
            ser_str += "," + str(node.val)
            preorder(node.left)
            preorder(node.right)
        preorder(root)
        return ser_str[1:]

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        index = 0
        vals = data.split(',')
        def preorderBuild():
            nonlocal data
            nonlocal index
            if vals[index] == "N":
                index += 1
                return None
            
            node = TreeNode()
            node.val = int(vals[index])
            index += 1
            node.left = preorderBuild()
            node.right = preorderBuild()

            return node

        return preorderBuild()

