# Given two string arrays word1 and word2, return True if the two arrays represent the same string, and False otherwise

def are_equivalent(word1: list[str], word2: list[str]) -> bool:
    return ''.join(word1) == ''.join(word2)

word1 = ["bat", "man"]
word2 = ["b", "atman"]
#print(are_equivalent(word1, word2))

word1 = ["alfred", "pennyworth"]
word2 = ["alfredpenny", "word"]
#print(are_equivalent(word1, word2))

word1  = ["cat", "wom", "an"]
word2 = ["catwoman"]
#print(are_equivalent(word1, word2))


#Implement a function count_evens() that accepts a list of strings lst as a parameter. The function should return the number of strings with an even length in the list.


def count_evens(lst: list[str]) -> int:
    numEvens: int = 0
    for s in lst:
        if len(s) % 2 == 0:
            numEvens+=1
    return numEvens

lst = ["na", "nana", "nanana", "batman", "!"]
#print(count_evens(lst))

lst = ["the", "joker", "robin"]
#print(count_evens(lst))

lst = ["you", "either", "die", "a", "hero", "or", "you", "live", "long", "enough", "to", "see", "yourself", "become", "the", "villain"]
#print(count_evens(lst))


# Write a function remove_name() to keep Batman's secret identity hidden. The function accepts a list of names people and a string secret_identity and should return the list with any instances of secret_identity removed. The list must be modified in place; you may not create any new lists as part of your solution. Relative order of the remaining elements must be maintained.

def remove_name(people: list[str], secret_identity: str) -> list[str]:
    for i in range(len(people)-1, -1, -1):
        print(i)
        if people[i] == secret_identity:
            people.pop(i)
    return people

people = ['Batman', 'Superman', 'Bruce Wayne', 'The Riddler', 'Bruce Wayne']
secret_identity = 'Bruce Wayne'
#print(remove_name(people, secret_identity))

#Given a non-negative integer n, write a function count_digits() that returns the number of digits in n. You may not cast n to a string.

def count_digits(n: int) -> int:
    count = 0;
    while n // 10 != 0: #while it is not hte last digit
        count+=1
        n //= 10 # extract the last digit
    return count+1# for last digit


n = 964
# print(count_digits(n))

#Write a function move_zeroes that accepts an integer array nums and returns a new list with all 0s moved to the end of list. The relative order of the non-zero elements in the original list should be maintained.

def move_zeroes(lst: list[int]) -> list[ing]:
    for i, n in enumerate(lst):
        if n == 0:
            lst.pop(i)
            lst.append(0)
    return lst

lst = [1, 0, 2, 0, 3, 0]
#print(move_zeroes(lst))


#Given a string s, reverse only all the vowels in the string and return it.
#The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases and more than once.

def isVowel(c: str) -> bool:
    if c.lower() == 'a' or c.lower() == 'e' or c.lower() == 'i' or c.lower() == 'o' or c.lower() == 'u':
        return True
    else:
        return False
    

def reverse_vowels(s: str) -> str:
    chars: list[str] = list(s) # convert into array of characters
    print(f"chars: {chars}")
    l: int = 0; 
    r: int = len(chars)-1
    while l < r: 
        if isVowel(chars[l]) and isVowel(chars[r]):
            temp = chars[l]
            chars[l] = chars[r]
            chars[r] = temp
            l+=1
            r-=1
        if not isVowel(chars[l]):
            l+=1
        if not isVowel(chars[r]):
            r-=1
    return ''.join(chars)
    
s = "robin"
#print(reverse_vowels(s))

s = "BATgirl"
#print(reverse_vowels(s))

s = "batman"
#print(reverse_vowels(s))

"""
Batman is going on a scouting trip, surveying an area where he thinks Harley Quinn might commit her next crime spree. The area has many hills with different heights and Batman wants to find the tallest one to get the best vantage point. His scout trip consists of n + 1 points at different altitudes. Batman starts his trip at point 0 with altitude 0.

Write a function highest_altitude() that accepts an integer array gain of length n where gain[i] is the net gain in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). Return the highest altitude of a point.
"""

#prefix sum problem, running total
def highest_altitude(gain: list[int]) -> int:
    # go through the gain list and calculate the altitude at each step, keeping track of the hightest altitude found, 
    highest: int = 0
    altitude: int = 0
    for level in gain:
        altitude += level
        if altitude > highest:
            highest = altitude
    return highest

gain = [-5, 1, 5, 0, -7]
#print(highest_altitude(gain))

gain = [-4, -3, -2, -1, 4, 3, 2]
#print(highest_altitude(gain))


# Left and Right Sum Differences
'''
Given a 0-indexed integer array nums, write a function left_right_difference that returns a 0-indexed integer array answer where:

len(answer) == len(nums)
answer[i] = left_sum[i] - right_sum[i]
Where:

left_sum[i] is the sum of elements to the left of the index i in the array nums. If there is no such element, left_sum[i] = 0
right_sum[i] is the sum of elements to the right of the index i in the array nums. If there is no such element, right_sum[i] = 0
'''

def left_right_difference(nums: list[int]) -> list[int]:
    difference: list[int] = []
    for i, num in enumerate(nums):
        leftSum: int = 0
        rightSum: int = 0
        #use slice syntax to get left and right arrays
        left = nums[:i]
        right = nums[i+1:]
        leftSum = sum(left) 
        rightSum = sum(right)
        difference.append(leftSum - rightSum)
    return difference

nums = [10, 4, 8, 3]
#print(left_right_difference(nums))

nums = [1]
#print(left_right_difference(nums))

# Common Cause

def common_elements(lst1: list[str], lst2: list[str]) -> list[str]:
    outList: list[str] = []
    for s1 in lst1:
        for s2 in lst2:
            if s1 == s2: 
                outList.append(s1)

    return outList

lst1 = ["super strength", "super speed", "x-ray vision"]
lst2 = ["super speed", "time travel", "dimensional travel"]
print(common_elements(lst1, lst2))

lst1 = ["super strength", "super speed", "x-ray vision"]
lst2 = ["martial arts", "stealth", "master detective"]
print(common_elements(lst1, lst2))


