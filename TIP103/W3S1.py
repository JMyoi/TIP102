


"""
recurse down every layer, sandwitch[1]
if that layers is the last lyer meaning that there are no more layers after it
then return base case 1
as we come back up we add 1
"""
def count_layers(sandwich):
    if len(sandwich) == 1:
        return 1
    return count_layers(sandwich[1]) + 1
     

sandwich1 = ["bread", ["lettuce", ["tomato", ["bread"]]]]
sandwich2 = ["bread", ["cheese", ["ham", ["mustard", ["bread"]]]]]

print(count_layers(sandwich1))
print(count_layers(sandwich2))


def reverse_orders(orders):
    reversed = []
    orders = orders.split(" ")
    print(orders)
    reversed = recReverseorder(orders, reversed)
    reversed = " ".join(reversed)
    return reversed

def recReverseorder(orders, revOrders):
    print(f"orders: {orders}, reverse orders: {revOrders}")
    if len(orders) == 1:
        revOrders.append(orders[0])
        return revOrders
    recReverseorder(orders[1:], revOrders)
    print(f"orders: {orders}, reverse orders: {revOrders}")
    revOrders.append(orders[0])
    return revOrders


print(reverse_orders("Bagel Sandwich Coffee"))


#infix to postfix

def infix_to_postfix(tokens: str) -> list[str]:
    precedence = {'+' : 1, '-' : 1, '*' : 2, '/' : 2}
    out = [] # output array
    opStack = [] # operator stack

    for t in tokens:
        if t == '(':
            opStack.append(t)
        elif t == ')':
            while opStack[-1] != '(':
                out.append(opStack.pop())
            opStack.pop() # pop the open parentheses
        elif t in precedence: # if t is an operator
            if not opStack or opStack[-1] == '(': # if stack is empty or we did not hit a wall.
                opStack.append(t)
            elif precedence[opStack[-1]] >= precedence[t]:
                while opStack and opStack[-1] != '(' and precedence[opStack[-1]] >= precedence[t]:
                    out.append(opStack.pop())
                opStack.append(t)
            elif precedence[opStack[-1]] < precedence[t]:
                opStack.append(t)
        else: # push all numbers to output
            out.append(t)
    while opStack:
        out.append(opStack.pop())

    return out

print(infix_to_postfix("5".split()), "expected: ['5']")
print(infix_to_postfix("1 + 2".split()), "expected: ['1', '2', '+']")
print(infix_to_postfix("3 + 4 * 2".split()), "expected: ['3', '4', '2', '*', '+']")
print(infix_to_postfix("3 * 4 + 2".split()), "expected: ['3', '4', '*', '2', '+']")
print(infix_to_postfix("5 - 3 - 1".split()), "expected: ['5', '3', '-', '1', '-']")
print(infix_to_postfix("8 / 4 / 2".split()), "expected: ['8', '4', '/', '2', '/']")
print(infix_to_postfix("1 + 2 * 3 / 4".split()), "expected: ['1', '2', '3', '*', '4', '/', '+']")
print(infix_to_postfix("( 1 + 2 )".split()), "expected: ['1', '2', '+']")
print(infix_to_postfix("( 3 + 4 ) * 2".split()), "expected: ['3', '4', '+', '2', '*']")
print(infix_to_postfix("2 * ( 3 + 4 ) - 5".split()), "expected: ['2', '3', '4', '+', '*', '5', '-']")
print(infix_to_postfix("( ( 1 + 2 ) * ( 3 - 4 ) ) / 5".split()), "expected: ['1', '2', '+', '3', '4', '-', '*', '5', '/']")
print(infix_to_postfix("12 + 34 * 5".split()), "expected: ['12', '34', '5', '*', '+']")


# evaluate reverse polish notation / postfix evaluation

def postfix_eval(token: list[str]) -> int:

    stack = []
    for t in token:
        if t in "/*-+":
            right = stack.pop()
            left = stack.pop()
            if t == '/': stack.append(int(left / right)) #truncate towards 0
            elif t == '*': stack.append(left * right)
            elif t == '-': stack.append(left - right)
            elif t == '+': stack.append(left + right)
        else:
            stack.append(int(t))
    return stack.pop()

print(postfix_eval(infix_to_postfix("5".split())), "expected: ['5']")
print(postfix_eval(infix_to_postfix("1 + 2".split())), "expected: ['1', '2', '+']")
print(postfix_eval(infix_to_postfix("3 + 4 * 2".split())), "expected: ['3', '4', '2', '*', '+']")
print(postfix_eval(infix_to_postfix("3 * 4 + 2".split())), "expected: ['3', '4', '*', '2', '+']")