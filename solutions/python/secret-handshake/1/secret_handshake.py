def commands(binary_str):
    actions = []

    # read last 5 bits (pad with zeros if shorter)
    bits = binary_str[-5:].zfill(5)

    # bit positions from rightmost to left
    if bits[-1] == "1":
        actions.append("wink")
    if bits[-2] == "1":
        actions.append("double blink")
    if bits[-3] == "1":
        actions.append("close your eyes")
    if bits[-4] == "1":
        actions.append("jump")

    # reverse bit (leftmost of the 5 bits)
    if bits[-5] == "1":
        actions.reverse()

    return actions

