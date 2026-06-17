def is_valid_post_format(posts):
  stack = []
  top = ""
  mapping = {")": "(", "}": "{", "]": "["}  
  for post in posts:
    if post in "([{":
        stack.append(post)
    elif post in ")]}":
        if not stack:
            return False
        top = stack.pop()
        if mapping.get(post) != top:
            return False
  return len(stack) == 0


#print(is_valid_post_format("()"))
#print(is_valid_post_format("()[]{}")) 
#print(is_valid_post_format("(]"))


def reverse_comments_queue(comments):
    stack = []
    loop = len(comments)
    for i in range(loop):
        stack.append(comments.pop())
    return stack

#print(reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing."]))
#print(reverse_comments_queue(["First!", "Interesting read.", "Well written."]))

def is_symmetrical_title(title):
    left = 0
    right = len(title) - 1
    title = title.lower()
    while left < right:
        if not title[left].isalnum():
            left += 1
            continue
        if not title[right].isalnum():
            right -= 1
            continue
        if title[left] != title[right]:
            return False
        left += 1
        right -= 1
    return True

#print(is_symmetrical_title("A Santa at NASA"))
#print(is_symmetrical_title("Social Media")) 

def engagement_boost2(engagements):
    squared_engagements = []
    
    for i in range(len(engagements)):
        squared_engagement = engagements[i] * engagements[i]
        squared_engagements.append((squared_engagement, i))
    
    squared_engagements.sort(reverse=True)
    
    result = [0] * len(engagements)
    position = len(engagements) - 1
    
    for square, original_index in squared_engagements:
        result[position] = square
        position -= 1
    
    return result


def engagement_boost(engagements):
    squared = []
    left = 0
    right = len(engagements) - 1
    l2, r2 = 0, 0
    
    while left <= right:
        l2, r2 = engagements[left]**2 , engagements[right]**2
        if left == right:  
            squared.append(l2)
        else:
            squared.append(l2)
            squared.append(r2)
        left += 1
        right -= 1
        
    return sorted(squared)
print(engagement_boost([-4, -1, 0, 3, 10]))
print(engagement_boost([-7, -3, 2, 3, 11]))
            

#Nice job guys
