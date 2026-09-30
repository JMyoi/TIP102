"""

keep a freq map of how often a number appears.

counts = {
    1:1,
    3:2,
    2:3,
    5:1,
    7:1
}
"""


# def find_balanced_subsequence(art_pieces):
#     counts = {}

#     for piece in art_pieces:
#         counts[piece] = counts.get(piece, 0) + 1

#     max_length = 0

#     for x in counts:
#         if x + 1 in counts:
#             current = counts[x] + counts[x + 1] 
#             if current > max_length:
#                 max_length = current

#     return max_length


# art_pieces1 = [1,3,2,2,5,2,3,7]
# art_pieces2 = [1,2,3,4]
# art_pieces3 = [1,1,1,1]

# print(find_balanced_subsequence(art_pieces1))
# print(find_balanced_subsequence(art_pieces2))
# print(find_balanced_subsequence(art_pieces3))

"""


art_pieces = [1, 3, 3, 2]
n = len(art_pieces) = 4

if len(art_pieces) =! max(art_pieces) + 1:
    return False

convert list into a se

seen = set(art_pieces)
    seen = {1,2,3}
check if len(seen) == n-1

max of seen appears twice in art_pieces, does 3 appear twice


[2,1,3]

2,1,3

2 - 7, 7

len 7


"""


# def is_authentic_collection(art_pieces):

#     if len(art_pieces) != max(art_pieces) + 1 and min(art_pieces) != 1:
#         return False

#     seen = set(art_pieces) 
#     if len(seen) != len(art_pieces) - 1:
#         return False

#     biggest = max(art_pieces)
#     if art_pieces.count(biggest) == 2:
#         return True
#     return False
    

# collection1 = [2, 1, 3]
# collection2 = [1, 3, 3, 2]
# collection3 = [1, 1]

# print(is_authentic_collection(collection1))
# print(is_authentic_collection(collection2))
# print(is_authentic_collection(collection3))

'''
use a dictionary to keep count of the elements in collection
count the frequencies of the elements in collection

find the largest count of elements
set largest count to length of rows

do another for loop to populate row array

'''
def organize_exhibition(collection):
    counts = {}

    for value in collection:
        if value in counts:
            counts[value] += 1
        else:
            counts[value] = 1

    nums_rows = max(counts.values())
    rows = [[] for _ in range(num_rows)]

    for value in counts:


    [list("O'Keefe", "Kahlo", "Picasso",, "Warhol"), list("O'Keefe",Kahlo" ), list("O'Keef)]


collection1 = ["O'Keefe", "Kahlo", "Picasso", "O'Keefe", "Warhol", 
              "Kahlo", "O'Keefe"]

collection2 = ["Kusama", "Monet", "Ofili", "Banksy"]

print(organize_exhibition(collection1))
print(organize_exhibition(collection2))