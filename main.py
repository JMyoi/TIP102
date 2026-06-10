import random

# question 1
def reverse_sentence(sentence):
    arr = sentence.split();
    arr.reverse();
    result = " ".join(arr);
    return result;
    
sentence = "tubby"
#print(reverse_sentence(sentence))


# Question 2

def goldilocks_approved(nums):
    if len(nums) > 2: 
        MAX = max(nums);
        MIN = min(nums);
        nums.remove(MAX);
        nums.remove(MIN);
        index = random.randint(0, len(nums)-1);
        return nums[index];
    else:
        return -1;

nums = [2, 1, 3]
#print(goldilocks_approved(nums))


#Question 3


def delete_minimum_elements(hunny_jar_sizes):
    SortedJar = []
    while len(hunny_jar_sizes) > 0:
        smallest = min(hunny_jar_sizes);
        SortedJar.append(smallest);
        hunny_jar_sizes.remove(smallest);
    return SortedJar;

hunny_jar_sizes = [5, 2, 1, 8, 2]
#print(delete_minimum_elements(hunny_jar_sizes))


#Question 4
def sum_of_digits(num):
    num = str(num);
    accum = 0;
    for n in num: 
        accum += int(n);
    return accum;


num = 423
#print(sum_of_digits(num))

#Question 5
def final_value_after_operations(operations): 
    tigger = 1 
    
    for operation in operations: 
        match operation: 
            case "bouncy": 
                print("in Bouncy") 
                tigger += 1
            case "flouny": 
                print("in flouny") 
                tigger += 1
            case "trouncy": 
                print("in trouncy") 
                tigger -= 1
            case "pouncy": 
                print("in pouncy") 
                tigger -= 1
                
    # This must be indented aligned with the 'for' keyword
    return tigger 


operations = ["trouncy", "flouncy", "flouncy"]
#print(final_value_after_operations(operations))

print("There were: ", 3, " people at the park\n")