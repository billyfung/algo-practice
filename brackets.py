# checking for parentheses


def parChecker(inputString):
    stack = []
    pairs = { "}": "{", "]": "[", ")": "(",}
    balanced = True
    for character in inputString:
        if balanced:
            if character in "([{":
                stack.append(character)
            else:
                if len(stack) == 0:
                    balanced = False
                else:
                    top = stack.pop()
                    if not pairs.has_key(character):
                        balanced = False
    if balanced and (len(stack)==0):
        return True
    else:
        return  False

print(parChecker('(((([()))))'))
