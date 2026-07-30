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

    So instead of branching out, you've basically got two separate linked lists hanging off the root (🧁→🍪→🥐 on each side). Yes, the heights match (3 on each side), so it's technically height-balanced, but it's degenerate — no fanout, no real branching. If you kept extending it this way, lookups would be O(n) down a chain instead of O(log n) through a bushy tree, which defeats the whole point of using a tree instead of a list.

    A truly balanced tree at that depth would have 2, 4, then 8 nodes per level, not 2, 2, 2.
    """



    print("let's go")





    



baked_goods = ["🎂", "🥮", "🍩", None, None, "🥖", "🧁"] 
display1 = build_tree(baked_goods)

baked_goods = ["🥖", "🧁", "🧁", "🍪", None, None, "🍪", "🥐", None, None, "🥐"]
display2 = build_tree(baked_goods)


print(is_balanced(display1)) 
print(is_balanced(display2)) 


