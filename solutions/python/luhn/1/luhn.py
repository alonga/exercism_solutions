class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        # Remove all spaces
        num = self.card_num.replace(" ", "")

        # Must be more than 1 digit
        if len(num) <= 1:
            return False

        # Must contain only digits
        if not num.isdigit():
            return False

        # Luhn checksum
        digits = [int(ch) for ch in num]

        # Reverse index and double every second digit
        for i in range(len(digits) - 2, -1, -2):
            doubled = digits[i] * 2
            if doubled > 9:
                doubled -= 9
            digits[i] = doubled

        # Valid if sum % 10 == 0
        return sum(digits) % 10 == 0
