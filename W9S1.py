from collections import deque 

# Tree Node class
class TreeNode:
  def __init__(self, value, key=None, left=None, right=None):
      self.key = key
      self.val = value
      self.left = left
      self.right = right

def build_tree(values):
  if not values:
      return None

  def get_key_value(item):
      if isinstance(item, tuple):
          return item[0], item[1]
      else:
          return None, item

  key, value = get_key_value(values[0])
  root = TreeNode(value, key)
  queue = deque([root])
  index = 1

  while queue:
      node = queue.popleft()
      if index < len(values) and values[index] is not None:
          left_key, left_value = get_key_value(values[index])
          node.left = TreeNode(left_value, left_key)
          queue.append(node.left)
      index += 1
      if index < len(values) and values[index] is not None:
          right_key, right_value = get_key_value(values[index])
          node.right = TreeNode(right_value, right_key)
          queue.append(node.right)
      index += 1

  return root

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
Problem 1: Merging Cookie Orders
Understand:
    overlap tree 1 onto tree 2, and sum the nodes if the nodes overlap, 
    if they don't just add it as a new node.
plan:
    base case: if both are None, return
    if order 1 and order2 are valid
        sum the node and add it to the tree.
    if order 1 is valid and order 2 is None, 
        add order 1 node to the new tree. 
    if order 1 is None and order 2 is valid,
        add order 2 node to the new tree
"""
def merge_orders(order1, order2):
    if not order1 and not order2:
        return None
    elif not order2:
        return order1
    elif not order1:
        return order2
    
    merged = TreeNode(order1.val + order2.val)

    merged.left = merge_orders(order1.left, order2.left)
    merged.right = merge_orders(order1.right, order2.right)

    return merged
    


# Using build_tree() function included at top of page
cookies1 = [1, 3, 2, 5]
cookies2 = [2, 1, 3, None, 4, None, 7]
order1 = build_tree(cookies1)
order2 = build_tree(cookies2)

# Using print_tree() function included at top of page
print_tree(merge_orders(order1, order2))


""""
Problem 2: Croquembouche
ou are designing a delicious croquembouche (a French dessert composed of a cone-shaped tower of cream puffs 😋), 
for a couple's wedding. They want the cream puffs to have a variety of flavors. You've finished your design and 
want to send it to the couple for review.

Given a root of a binary tree design where each node in the tree represents a cream puff in the croquembouche, 
that prints a list of the flavors (vals) of each cream puff in level order (i.e., from left to right, level by level).

Note: The build_tree() and print_tree() functions both use variations of a level order traversal. To get the most out of this problem,
 we recommend that you reference these functions as little as possible while implementing your solution.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated
 time complexity. Assume the input tree is balanced when calculating time complexity.


 
Understand:
    Input: The binary tree root 
    Output: Each flavor level by level from left to right

Plan:
    Go through each level and print out each flavor from left to right using a queue

"""

class Puff():
     def __init__(self, flavor, left=None, right=None):
        self.val = flavor
        self.left = left
        self.right = right

def print_design(design):
    if design is None:
        return []
    result = []
    queue = deque([design])
    while queue:
        # { } [A] B
        node = deque.popleft()
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result


croquembouche = Puff("Vanilla", 
                    Puff("Chocolate", Puff("Vanilla"), Puff("Matcha")), 
                    Puff("Strawberry"))
print_design(croquembouche)

