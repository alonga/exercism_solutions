class Allergies:

    ALLERGENS = [
        ("eggs", 1),
        ("peanuts", 2),
        ("shellfish", 4),
        ("strawberries", 8),
        ("tomatoes", 16),
        ("chocolate", 32),
        ("pollen", 64),
        ("cats", 128),
    ]

    def __init__(self, score):
        # Only keep the 8 relevant bits
        self.score = score & 255

    def allergic_to(self, item):
        score_value = next(value for name, value in self.ALLERGENS if name == item)
        return (self.score & score_value) != 0

    @property
    def lst(self):
        return [name for name, value in self.ALLERGENS if (self.score & value)]
