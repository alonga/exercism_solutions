def equilateral(sides):
    if check_lengths(sides) == False:
        return False
    side1 = sides[0]
    side2 = sides[1]
    side3 = sides[2]
    all_equal = (side1 == side2 == side3)
    return all_equal

def isosceles(sides):
    if check_lengths(sides) == False:
        return False
    side1 = sides[0]
    side2 = sides[1]
    side3 = sides[2]

    if (side1 in (side2, side3)) or (side2 == side3):
        return True
    else:
        return False

def scalene(sides):
    if check_lengths(sides) == False:
        return False
    side1 = sides[0]
    side2 = sides[1]
    side3 = sides[2]
    all_unequal = (side1 != side2 != side3 != side1)
    return all_unequal


def check_lengths(sides):
    if 0 in sides:
        return False
    elif (sides[0] + sides[1] >= sides[2]) and (sides[2] + sides[0] >= sides[1]) and (sides[1] + sides[2] >=sides[0]):
        return True
    else:
        return False