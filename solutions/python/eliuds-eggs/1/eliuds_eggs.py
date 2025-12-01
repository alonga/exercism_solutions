def egg_count(display_value):
    count = 0
    while display_value > 0:
        # If the least significant bit is 1, increment count
        if display_value % 2 == 1:
            count += 1
        # Shift number right by dividing by 2 (integer division)
        display_value //= 2
    return count

