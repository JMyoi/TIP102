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