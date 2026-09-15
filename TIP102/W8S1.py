from collections import deque 
import operator

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def print_tree(root):
    if not root:
        return "Empty"
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    print(result)


"""
Problem 1. 


"""


root = TreeNode("Trunk")

root.left = TreeNode("Mcintosh")
root.right = TreeNode("Granny Smith")

root.left.left = TreeNode("Fuji")
root.left.right = TreeNode("Opal")

root.right.left = TreeNode("Crab")
root.right.right = TreeNode("Gala")


# Using print_tree() included at the top of this page
#print_tree(root)


"""
Problem 2

"""

def calculate_yield(root):
    ops = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv
    }   
    
    op1 = root.left.val
    op2 = root.right.val
    
    return ops[root.val](op1,op2)
    

apple_tree = TreeNode("+", TreeNode(7), TreeNode(5))
#print(calculate_yield(apple_tree))


"""
Problem 3
"""

def right_vine(root):
    result = []
    curr = root
    while curr:
        result.append(curr.val)
        curr = curr.right

    return result




"""
Problem 4

"""
def right_vine_rec(root):
    result = []

    def rightVine(node):
        #base case
        if not node:
            return result
        
        result.append(node.val)
        rightVine(node.right)

    rightVine(root)
    return result


ivy1 = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

ivy2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))

#print(right_vine_rec(ivy1))
#print(right_vine_rec(ivy2))

"""
Problem 5
"""


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def count_leaves(root):

    #dfs algo 

    s = [root]
    count = 0
    while s: 

        node = s.pop()

        if node.left:
            s.append(node.left)
        
        if node.right:
            s.append(node.right)
        
        if not node.right and not node.left:
            count+=1

    return count


oak1 = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

oak2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))



#rint(count_leaves(oak1))
#print(count_leaves(oak2))


"""
Problem 6
"""

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def survey_tree(root):
    result = []

    def postOrder(node):
        #base case
        if not node:
            return
        
        result.append(node.val)
        postOrder(node.left)
        postOrder(node.right)
        
    
    postOrder(root)
    return result


magnolia = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

print(survey_tree(magnolia))