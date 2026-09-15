from collections import deque

class TreeNode():
     def __init__(self, value, left=None, right=None):
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
#----------------------------------#
# Problem 1
"""
U:
Input: BST, Output: Integer - # of odd values
Output: count all the odd nodes 
Edge Cases: none

M: BST

P:
    -


def count_odd_splits(root):
    
    if root is None:
        return 0
    
    if root.val % 2 != 0:
        return 1 + count_odd_splits(root.left) + count_odd_splits(root.right)
    else:
        return 0 + count_odd_splits(root.left) + count_odd_splits(root.right)
    

"""

"""
      2
     / \
    /   \
   3     5
  / \     \
 6   7     12
 """

"""

# Using build_tree() function included at top of page
values = [2, 3, 5, 6, 7, None, 12]
monstera = build_tree(values)

print(count_odd_splits(monstera))
print(count_odd_splits(None))
"""
#----------------------------------#
# Problem 2
"""
U:
Input:
Output:
Edge Cases:

M: BST 

P:

def find_flower(inventory, name):
    if inventory is None:
        return False
    
    if inventory.val == name:
        return True
    elif name < inventory.val:
        return find_flower(inventory.left, name)
    else: 
        return find_flower(inventory.right, name)

"""
"""
         Rose
        /    \
      Lilac   Tulip
     /  \       \
  Daisy  Lily  Violet
 """
"""

# using build_tree() function at top of page
values = ["Rose", "Lilac", "Tulip", "Daisy", "Lily", None, "Violet"]

garden = build_tree(values)

#print(find_flower(garden, "Lilac"))  
#print(find_flower(garden, "Sunflower")) 
"""
#----------------------------------#
# Problem 3
"""
def non_bst_find_flower(root, name):
    if root is None:
        return False
    
    if root.val == name:
        return True

    return non_bst_find_flower(root.left, name) or non_bst_find_flower(root.right, name)

"""
#----------------------------------#
# Problem 4
"""
def add_plant(collection, name):
    
    if collection.left is None and collection.right is None:
        if name < collection.val:
            collection.left = TreeNode(name)
            return collection
        else:
            collection.right = TreeNode(name)
            return collection

    if name < collection.val:
        add_plant(collection.left, name)
    else:
        add_plant(collection.right, name)
        



values = ["Money Tree", "Fiddle Leaf Fig", "Snake Plant"]
collection = build_tree(values)
add_plant(collection, "Aloe")


# Using print_tree() function at the top of page
print_tree(collection)
"""
#----------------------------------#
# Problem 5
def sort_plants(collection):
    pass

values = [(3, "Monstera"), (1, "Pothos"), (5, "Witchcraft Orchid"), None, (2, "Spider Plant"), (4, "Hoya Motoskei")]
collection = build_tree(values)

print(sort_plants(collection))
