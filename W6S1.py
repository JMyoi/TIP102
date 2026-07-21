def loop_length(playlist_head):
    slow = playlist_head
    fast = playlist_head
    cycle: bool = False
    while fast:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            cycle = True
            break 
    
    if cycle == False:
        return 0
    

    count = 0
    FirstMet = False
    curr = playlist_head

    # slow holds the node where both slow and fast meet
    # try traversing the cycle until you return back to slow?
    # slow is always == fast if there is a cycle, it is guaranteed that if there is a cycle they will always meet at some point.
    #Can you try running this I think it works!
    # 
    while curr is not fast:
        if curr != fast.next: # first meeting of start
            FirstMet = True
            curr = curr.next
            continue
        #i changed condition try one more time 1 again
        #ok whatevery lol, we tried, I will try this again another time
        # feel free to copy the code before i close the liveshare
        if FirstMet and curr is not fast:
            count +=1
        curr = curr.next

    return count