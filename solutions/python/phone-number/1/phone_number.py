class PhoneNumber:
    def __init__(self, number):
        # Reject letters before anything else
        if any(c.isalpha() for c in number):
            raise ValueError("letters not permitted")

        # Reject punctuation symbols not allowed as separators
        if any(c in "@:!?" for c in number):
            raise ValueError("punctuations not permitted")

        # Keep only digits
        digits = "".join(c for c in number if c.isdigit())

        # Validate digit count
        if len(digits) < 10:
            raise ValueError("must not be fewer than 10 digits")
        if len(digits) > 11:
            raise ValueError("must not be greater than 11 digits")

        # 11 digits → must start with 1, otherwise error
        if len(digits) == 11:
            if digits[0] != "1":
                raise ValueError("11 digits must start with 1")
            digits = digits[1:]  # remove country code

        # Now exactly 10 digits: validate area & exchange codes
        area = digits[0]
        exchange = digits[3]

        if area == "0":
            raise ValueError("area code cannot start with zero")
        if area == "1":
            raise ValueError("area code cannot start with one")
        if exchange == "0":
            raise ValueError("exchange code cannot start with zero")
        if exchange == "1":
            raise ValueError("exchange code cannot start with one")

        self.number = digits
        self.area_code = digits[:3]

    def pretty(self):
        return f"({self.area_code})-{self.number[3:6]}-{self.number[6:10]}"
