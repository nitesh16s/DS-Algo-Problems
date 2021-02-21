def is_valid(expr):
    lefty = '({['
    righty = ')}]'
    stack = []

    def is_empty(stack):
        return len(stack) == 0

    for x in expr:
        if x in lefty:
            stack.append(x)
        if x in righty:
            if is_empty(stack):
                return False
            if righty.index(x) != lefty.index(stack.pop()):
                return False
    return is_empty(stack)

print(is_valid('{{{{}}}}'))
