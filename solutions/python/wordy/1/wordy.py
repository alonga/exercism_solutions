def answer(question):
    if not question.startswith("What is ") or not question.endswith("?"):
        raise ValueError("syntax error")

    text = question[8:-1].strip()

    text = (text.replace("multiplied by", "multiplied_by")
                .replace("divided by", "divided_by"))

    tokens = text.split()
    if not tokens:
        raise ValueError("syntax error")

    # First token must be a number
    try:
        result = int(tokens[0])
    except:
        raise ValueError("syntax error")

    allowed_ops = ("plus", "minus", "multiplied_by", "divided_by")

    i = 1
    while i < len(tokens):
        # Must have operator here
        op = tokens[i]
        if op not in allowed_ops:
            # If it's a number → syntax error
            if op.lstrip("-").isdigit():
                raise ValueError("syntax error")
            else:
                raise ValueError("unknown operation")

        # Must have RHS number next
        if i + 1 >= len(tokens):
            raise ValueError("syntax error")
        rhs_str = tokens[i + 1]
        try:
            rhs = int(rhs_str)
        except:
            raise ValueError("syntax error")

        # Apply operator
        if op == "plus":
            result += rhs
        elif op == "minus":
            result -= rhs
        elif op == "multiplied_by":
            result *= rhs
        elif op == "divided_by":
            result //= rhs

        i += 2

    return result
