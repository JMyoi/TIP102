"""
    freq = Counter(code)

    for key, values in freq.items():
        freq[key]-=1
        seen = set(freq.values())
        print(seen)
        #happy path removing the correct one, only 1 element in the set
        if len(seen) == 1:
            return True
        freq[key]+=1

    return False

make the freq map from the string

a: 1
r: 1
g: 1
h: 2, remove 1
return true

for every value in kv pair, decrement and check if balanced

2nd solution after building the frequency map, find the max frequency and decrement it,
    if it's happy path then all values will be same after that
any other case where the elements are not the same means 
    you cannot remove one element to make it balanced   

"""
from collections import Counter

def can_make_balanced(code):
    freq = Counter(code)
    Max = max(freq.values())
    for k in freq:
        if freq[k] == Max:
            freq[k]-=1
    Seen = freq.values()
    if len(Seen) == 1:
        return True
    return False
        
code1 = "arghh"
code2 = "haha"

print(can_make_balanced(code1)) 
print(can_make_balanced(code2)) 