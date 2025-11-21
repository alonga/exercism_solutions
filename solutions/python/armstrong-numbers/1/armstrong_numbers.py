def is_armstrong_number(number):
    power = len(str(number))
    total = 0
    n=number
    while n > 0:
        digit = n % 10
        total += digit ** power
        n //= 10

    if total == number:
       return True
    else:
        return False
    
    
