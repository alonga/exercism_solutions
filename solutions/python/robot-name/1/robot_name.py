import random
import string


class Robot:
    # Class-level registry to ensure uniqueness
    used_names = set()

    def __init__(self):
        self.name = self._generate_unique_name()

    def reset(self):
        self.name = self._generate_unique_name()

    @classmethod
    def _generate_unique_name(cls):
        while True:
            letters = ''.join(random.choice(string.ascii_uppercase) for _ in range(2))
            digits = ''.join(random.choice(string.digits) for _ in range(3))
            new_name = letters + digits

            if new_name not in cls.used_names:
                cls.used_names.add(new_name)
                return new_name

