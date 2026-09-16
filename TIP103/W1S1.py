
"""
Understand:

edge cases:
    empty list, return -1
    target string is empty

plan:

    empty list, return -1

    iterate through the list, comparing each element with the target
        if it's found, return that index
    
    return -1

"""

def linear_search(items, target):

    if not items:
        return -1

    for i, n, in enumerate(items):
        if n == target:
            return i

    return -1
    
items = ['haycorn', 'haycorn', 'haycorn', 'hunny',  'haycorn']
target = 'hunny'
#print(linear_search(items, target))

items = ['bed', 'blue jacket', 'red shirt', 'hunny']
target = 'red balloon'
#print(linear_search(items, target))


# Problem 2

"""
understand:

    tigger starts at 1
    incriment if element is "bouncy" or "flouncy"
    decrement if element is "trouncy" or "pouncy"

    edge cases:
        operations empty, return 1

Plan:

    keep a tigger variable assigned at 1
    if operation is empty return 1

    iterate through operations list
        process that element using if else,
        add or subtract depending on element

    return tigger

"""

def final_value_after_operations(operations):

    tigger = 1
    if not operations:
        return tigger

    for op in operations:
        if op == "bouncy" or op == "flouncy":
            tigger+=1
        elif op == "trouncy" or op == "pouncy":
            tigger-=1

    return tigger

operations = ["trouncy", "flouncy", "flouncy"]
#print(final_value_after_operations(operations))

operations = ["bouncy", "bouncy", "flouncy"]
#print(final_value_after_operations(operations))

"""
understand:


plan:

    convert the word to a list
        convert every character to lowercase
        .lower()?
    
        iterate through the list of characters
            if t, remove that 
            if i, remove
            if g,
                check next element, if that is a g,
                remove both 
            if e, 
                check next element, if that is r
                remove both
    
        combine the list back into a string, 
            result = "".join(lst)

"""

def tiggerfy(word):
    word = word.lower()
    wordsLst = list(word)

    for i, w in enumerate(wordsLst):
        if w == "t":
            wordsLst.remove("t")
        elif w == "i":
            wordsLst.remove("i")
        elif w == "g":
            if i == len(wordsLst):
                break
            if wordsLst[i+1]  == "g":
                wordsLst.remove("g")
                wordsLst.remove("g")
        elif w == "e":
            if i == len(wordsLst):
                break
            if wordsLst[i+1]  == "r":
                wordsLst.remove("g")
                wordsLst.remove("g")
    word = "".join(wordsLst)
    return word
            

word = "Trigger"
print(tiggerfy(word))

word = "eggplant"
print(tiggerfy(word))

word = "Choir"
print(tiggerfy(word))