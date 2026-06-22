from collections import deque


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
#print(engagement_boost([-4, -1, 0, 3, 10]))
#print(engagement_boost([-7, -3, 2, 3, 11]))
            

#Nice job guys


"""
There are n users in a queue waiting to stream their favorite movies, where the 0th user is at the front of the queue and the (n - 1)th user is at the back of the queue.

You are given a 0-indexed integer array movies of length n where the number of movies that the ith user would like to stream is movies[i].

Each user takes exactly 1 second to stream a movie. A user can only stream 1 movie at a time and has to go back to the end of the queue (which happens instantaneously) in order to stream more movies. If a user does not have any movies left to stream, they will leave the queue.

Return the time taken for the user at position k (0-indexed) to finish streaming all their movies.

Initialize an empty queue.
Iterate over the movies list and append a tuple (i, movies[i]) to the queue where i is the user's index, and movies[i] is the number of movies they want to stream.
While there are still users in the queue:
Process each user by removing them from the front of the queue and icnremnting time by 1 for each movie streamed.
If the user is k and has just streamed their last movie, return the current time.
If the user still has movies left to stream, put them back at the end of the queue with one less movie.

"""

def time_required_to_stream(movies, k):
    moviesQueue: deque[tuple[int, int]] = deque()
    for i, movie in enumerate(movies):
        moviesQueue.append((i, movie))
    timeCount = 0
    while(moviesQueue):
        movie = moviesQueue.popleft()
        #decrement time of movie
        tempMovie = list(movie)
        tempMovie[1] -= 1
        movie = tuple(tempMovie)
        timeCount += 1
        if movie[1] != 0:
            moviesQueue.append(movie)
        elif movie[0] == k and movie[1] == 0:
            return timeCount
    

print(time_required_to_stream([2, 3, 2], 2)) 
print(time_required_to_stream([5, 1, 1, 1], 0)) 
