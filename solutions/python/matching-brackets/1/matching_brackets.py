def is_paired(input_string):
    pairs = {')': '(', ']': '[', '}': '{'}
    stack = []

    for ch in input_string:
        if ch in pairs.values():          # opening bracket
            stack.append(ch)
        elif ch in pairs:                 # closing bracket
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()

    return len(stack) == 0

