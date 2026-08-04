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


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

        

def is_balanced(display):


    """

    Because every node in it has exactly one child instead of two.

    Balance (in the AVL/BST sense) isn't just "same height on both sides" — it also assumes each node is reasonably filled with children. Here:

    🥖 → one 🧁 left, one 🧁 right (ok so far)
    but each 🧁 → only one 🍪 (not two)
    and each 🍪 → only one 🥐 (not two)

    So instead of branching out, you've basically got two separate linked lists hanging off the root (🧁→🍪→🥐 on each side). 
    Yes, the heights match (3 on each side), so it's technically height-balanced, but it's degenerate — no fanout, no real branching. 
    If you kept extending it this way, lookups would be O(n) down a chain instead of O(log n) through a bushy tree, which defeats the whole point of 
    using a tree instead of a list.

    A truly balanced tree at that depth would have 2, 4, then 8 nodes per level, not 2, 2, 2.
    """



    pass




    



baked_goods = ["🎂", "🥮", "🍩", None, None, "🥖", "🧁"] 
display1 = build_tree(baked_goods)

baked_goods = ["🥖", "🧁", "🧁", "🍪", None, None, "🍪", "🥐", None, None, "🥐"]
display2 = build_tree(baked_goods)


#print(is_balanced(display1)) 
#print(is_balanced(display2)) 

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def sum_each_days_orders(orders):
    """
    level order: BFS: Sum all the values at each level. push to resulting array
    
    """
    result = []
    if not orders:
        return result
        
    queue = deque([orders])
    

    while queue:
        levelsize = len(queue)
        levelSum = 0
        
        for i in range(levelsize):
            node = queue.popleft()
            levelSum += node.val

            if node.left: 
                queue.append(node.left)

            if node.right:
                queue.append(node.right)
                
        result.append(levelSum)

    return result




order_sizes = [4, 2, 6, 1, 3]
orders = build_tree(order_sizes)

#print(sum_each_days_orders(orders))



"""
Level order traversal
    if the level has one node, return 0 to the resulting array
    if it has more than one, find the max and min of that level
    take the absolute difference, abs(max - min)
    push that value to result array

"""


def sweet_difference(chocolates):
    result = []
    if not chocolates:
        return result

    queue = deque([chocolates])

    while queue: 
        levelsize = len(queue)
        levelArray =[]
        
        for _ in range(levelsize):
            node = queue.popleft()
            levelArray.append(node.val)

            if node.left: 
                queue.append(node.left)

            if node.right: 
                queue.append(node.right)

        minChocolate = min(levelArray)
        maxChocolate = max(levelArray)
        absDiff = maxChocolate - minChocolate
        result.append(absDiff)
    return result


# Using build_tree() function included at top of page
sweetness_levels1 = [3, 9, 20, None, None, 15, 7]
chocolate_box1 = build_tree(sweetness_levels1)


sweetness_levels2 = [1, 2, 3, 4, 5, None, 6]
chocolate_box2 = build_tree(sweetness_levels2)

print(sweet_difference(chocolate_box1))  
print(sweet_difference(chocolate_box2))  



"""
have a helper funciton
    takes in 2 nodes
    N1 and N2
    it checks if the children of N1 can be swapped to be children of N2
    if yes return true
    if not return false.
    
"""
def can_rearrange_orders(order1, order2):
    #null smore smore null ##edge case
    # bfs on both trees.
    
    #cheks if node 1's children can be swapped to be node2's children
    def CanSwap(node1, node2):
        if node1.left.val == node2.right.val and node1.right.val == node2.left.val:
            return True
        return False


    pass




# Using build_tree() function included at top of page
flavors1 = ["Red Velvet", "Vanilla", "Lemon", "Ube", "Almond", "Chai", "Carrot", 
            None, None, None, None, "Chai", "Maple", None, "Smore"]
flavors2 = ["Red Velvet", "Lemon", "Vanilla", "Carrot", "Chai", "Almond", "Ube", "Smore", None, "Maple", "Chai"]
order1 = build_tree(flavors1)
order2 = build_tree(flavors2)

can_rearrange_orders(order1, order2)

