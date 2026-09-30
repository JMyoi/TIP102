# You are planning a cross-country road trip in an electric vehicle (EV). 
# You are currently at the start of a long highway (index 0)
# Your goal is to reach the final charging hub located at the last index of the array.

# Each element in the integer array battery_life represents your maximum driving range
# (in miles/indices) from that particular position. 
# For example, if you are at battery_life[i] = 3, 
# you can "jump" or drive to any index from i + 1 up to i + 3.

# Return true if you can reach the final charging hub, or false otherwise.

# Example 1:

# Input: battery_life = [2, 3, 1, 1, 4]
# Output: true
# Explanation: Start at index 0 (range = 2). You can drive to index 1. 
# At index 1, your range is 3. You can drive directly to the last index (index 4).
# Example 2:

# Input: battery_life = [3, 2, 1, 0, 4]
# Output: false
# Explanation: No matter what, you will always arrive at index 3. 
# However, its range is 0, which means you're stuck at a "dead" charging
# station and can never reach the final hub.
# Constraints:

# 1 <= battery_life.length <= 10^4
# 0 <= battery_life[i] <= 10^5


def can_reach_destination(battery_life):
    # track max distance
    max_reach = 0

    # move through the array
    for i in range(len(battery_life)):
        if i > max_reach:
            return False;
    
        # for each item update the max distance we can travel based on the
        # amount of fuel available at each stop.
        max_reach = max(max_reach, i + battery_life[i])

        if max_reach >= len(battery_life) - 1:
            return True
 
    # if the max distance takes us to the end of
    # the array or further, then we return true (otherwise false)
    if max_reach >= len(battery_life) - 1:
        return True
    return False


"""
Problem 1: Transpose Matrix
U:

P:
i tracks row,
j track column,

original matrix = n x m
new Transpose matrix = m x n

make another array to hold the transpose, m x n

loop through each row, i 
loop throgh col j 
put that as the column of the output array.

new_arr[j][i] = matrix[i][j]

"""


def transpose(matrix):

    num_rows = len(matrix)
    num_cols = len(matrix[0])
    #print(f"row: {num_rows}, cols: {num_cols}")

    new_matrix = [[0 for _ in range(num_rows)] for _ in range(num_cols)]
    #print(new_matrix)

    # rows
    for i in range(num_rows): 
        # col
        for j in range(num_cols):
            new_matrix[j][i] = matrix[i][j]

    return new_matrix
   

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

#print(transpose(matrix))

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

#print(transpose(matrix))

"""
Problem 2:

Understand:
    two pointers to reverse the list of string.

Plan:
    keep 2 pointers
    left = 0
    right = len(lst) - 1

    while left < right
        swap left and right

"""

def reverse_list(lst):
    left = 0
    right = len(lst) - 1

    while left < right:
        lst[left],lst[right] = lst[right],lst[left]
        left+=1
        right-=1
    
    return lst

lst = ["pooh", "christopher robin", "piglet", "roo", "eeyore"]
print(reverse_list(lst))

"""
problem 3:
Understand:
    given a list of items, remove any duplicates 
    must be done in place
    return the length of final array

    
Plan:
    check each element with every other element.
    

"""

def remove_dupes(items):


    pass

    
items = ["extract of malt", "haycorns", "honey", "thistle", "thistle"]
remove_dupes(items)

items = ["extract of malt", "haycorns", "honey", "thistle"]
remove_dupes(items)