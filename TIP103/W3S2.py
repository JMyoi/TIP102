"""

3 5 2 1 4

1 2 3 5 4

"""

from collections import deque

def blueprint_approval(blueprints):
    
    blueprints.sort() # nlog(n)

    Q = deque()

    for print in blueprints: # O(n)
        Q.append(print)
    result = []

    while Q: # O(2n)
        result.append(Q.popleft())

    return result
    
print(blueprint_approval([3, 5, 2, 1, 4])) 
print(blueprint_approval([7, 4, 6, 2, 5])) 


"""


[10, 5, 8, 3, 7, 2, 9]

example 2
3   3   1
7   7   5   6

"""

def build_skyscrapers(floors):
    skyscraper = []
    skyscraperCount = 0

    for floor in floors: #O(n)
        if not skyscraper:
            skyscraper.append(floor)
            skyscraperCount+=1
        elif skyscraper[-1] >= floor:
            skyscraper.append(floor)
        else:
            skyscraper = [floor]
            skyscraperCount += 1


    return skyscraperCount

print(build_skyscrapers([10, 5, 8, 3, 7, 2, 9])) 
print(build_skyscrapers([7, 3, 7, 3, 5, 1, 6]))  
print(build_skyscrapers([8, 6, 4, 7, 5, 3, 2])) 

