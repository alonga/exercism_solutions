class StackUnderflowError(Exception):
    def __init__(self, message):
        self.message = message


def evaluate(input_data):
    stack = []
    words = {}
    tokens = tokenize(input_data)

    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token == ':':
            name = tokens[i + 1].lower()
            if name.lstrip('-').isdigit():
                raise ValueError("illegal operation")

            definition = []
            i += 2
            while tokens[i] != ';':
                t = tokens[i].lower()
                # EARLY BINDING: expand existing words now
                if t in words:
                    definition.extend(words[t])
                else:
                    definition.append(t)
                i += 1

            words[name] = definition[:]  # Store expanded definition
        i += 1

    execute(tokens, stack, words, 0, len(tokens))
    return stack


def tokenize(lines):
    result = []
    for line in lines:
        result.extend(line.lower().split())
    return result


def execute(tokens, stack, words, start, end):
    i = start
    while i < end:
        token = tokens[i]

        if token == ':':  # Skip definitions during execution
            while tokens[i] != ';':
                i += 1
            i += 1
            continue

        if token.lstrip('-').isdigit():
            stack.append(int(token))

        elif token in words:
            execute(words[token], stack, words, 0, len(words[token]))

        else:
            perform_operation(token, stack)

        i += 1


def perform_operation(token, stack):
    if token == "dup":
        check_size(stack, 1)
        stack.append(stack[-1])

    elif token == "drop":
        check_size(stack, 1)
        stack.pop()

    elif token == "swap":
        check_size(stack, 2)
        stack[-1], stack[-2] = stack[-2], stack[-1]

    elif token == "over":
        check_size(stack, 2)
        stack.append(stack[-2])

    elif token in ['+', '-', '*', '/']:
        check_size(stack, 2)
        b = stack.pop()
        a = stack.pop()
        if token == '+':
            stack.append(a + b)
        elif token == '-':
            stack.append(a - b)
        elif token == '*':
            stack.append(a * b)
        elif token == '/':
            if b == 0:
                raise ZeroDivisionError("divide by zero")
            stack.append(int(a / b))  # truncated toward zero

    else:
        raise ValueError("undefined operation")


def check_size(stack, n):
    if len(stack) < n:
        raise StackUnderflowError("Insufficient number of items in stack")
