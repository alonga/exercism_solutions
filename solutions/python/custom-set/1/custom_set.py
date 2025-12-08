class CustomSet:
    def __init__(self, elements=None):
        self._elements = []
        if elements:
            for e in elements:
                if e not in self._elements:
                    self._elements.append(e)

    def isempty(self):
        return len(self._elements) == 0

    def __contains__(self, element):
        return element in self._elements

    def issubset(self, other):
        return all(e in other._elements for e in self._elements)

    def isdisjoint(self, other):
        return all(e not in other._elements for e in self._elements)

    def __eq__(self, other):
        if len(self._elements) != len(other._elements):
            return False
        return self.issubset(other)

    def add(self, element):
        if element not in self._elements:
            self._elements.append(element)
        return self

    def intersection(self, other):
        return CustomSet([e for e in self._elements if e in other._elements])

    def __sub__(self, other):
        return CustomSet([e for e in self._elements if e not in other._elements])

    def __add__(self, other):
        # union
        result = CustomSet(self._elements.copy())
        for e in other._elements:
            if e not in result._elements:
                result._elements.append(e)
        return result
