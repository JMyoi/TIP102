#Check if array is sorted and rotated

def is_sorted_rotated(nums):
    decreasedAt = -1 # keeps track of where it started decreasing, only needed at last step to check if it's sorted. 
    decreasedCount = 0 # limit of only one decreased allowed between subsequent number or else return false
    if len(nums) <=1:
        return True;
    print(nums)
    for i, n in enumerate(nums):
        if i == 0:
            continue
        if nums[i-1] <= n:# ok, it's increasing
            continue
        elif decreasedAt == -1 and decreasedCount == 0: #else it's decareaseing, check if it has already decreased once, if not update
            decreasedAt = i # the index where it decreased
            decreasedCount +=1
        else: # already decreased before
            return False
    # if we made it out the loop, we have to check if it rotated by checkif first and last index.]\
    if nums[0] >= nums[-1] or decreasedCount == 0:
        return True
    return False


#
def count_pairs(nums, target):
    count = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] < target:
                count+=1
                
    return count



#subarray sum equals k