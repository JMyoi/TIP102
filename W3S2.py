
"""
You are managing the budget for a global expedition, where the cost of supplies is represented by an integer array costs, where costs[i] is the cost of the ith supply item.

There is a special discount available during the expedition. If you purchase the ith item, you will receive a discount equivalent to costs[j], where j is the minimum index such that j > i and costs[j] <= costs[i]. If no such j exists, you will not receive any discount.

Return an integer array final_costs where final_costs[i] is the final cost you will pay for the ith supply item, considering the special discount.

Monotonic stack problem, Find Next smallest element
this solution below is n^2
"""
def final_supply_costs(costs):
    DiscountedCosts:list[int] = []
    for i, cost in enumerate(costs):
        discounted: bool = False
        for j in range(i+1, len(costs), 1):
            if costs[j] <= cost:
                DiscountedCosts.append(cost - costs[j])
                discounted = True
                break
        if not discounted:
            DiscountedCosts.append(cost)
    return DiscountedCosts

print(final_supply_costs([8, 4, 6, 2, 3])) 
print(final_supply_costs([1, 2, 3, 4, 5])) 
print(final_supply_costs([10, 1, 1, 6])) 

def final_supply_costs_MS(costs):
    final = list(costs)        # start with full price; we'll subtract discounts we find
    stack = []                 # holds indices still waiting for a discount
    for j, cost in enumerate(costs):
        # cost is the candidate discount for any waiting index whose value >= cost
        while stack and costs[stack[-1]] >= cost:
            i = stack.pop()
            final[i] = costs[i] - cost
        stack.append(j)
    return final               # indices left on the stack keep full price
