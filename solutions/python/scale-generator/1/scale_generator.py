class Scale:
    # Chromatic scales as note name "alphabets"
    SHARP_NOTES = [
        "C", "C#", "D", "D#", "E", "F",
        "F#", "G", "G#", "A", "A#", "B"
    ]

    FLAT_NOTES = [
        "C", "Db", "D", "Eb", "E", "F",
        "Gb", "G", "Ab", "A", "Bb", "B"
    ]

    # Tonics that should use FLAT notation (raw, as passed to __init__)
    FLAT_KEYS = {
        "F", "Bb", "Eb", "Ab", "Db", "Gb",   # major
        "d", "g", "c", "f", "bb", "eb"       # minor
    }

    # Interval steps in semitones
    INTERVAL_STEPS = {
        "m": 1,   # minor second (half step)
        "M": 2,   # major second (whole step)
        "A": 3,   # augmented second
    }

    def __init__(self, tonic):
        # Decide flats or sharps based on the *original* tonic string
        if tonic in self.FLAT_KEYS:
            self._notes = self.FLAT_NOTES
        else:
            self._notes = self.SHARP_NOTES

        # Normalize tonic for indexing: first letter uppercase, rest as-is
        # e.g. "c#" -> "C#", "bb" -> "Bb"
        self.tonic = tonic[0].upper() + tonic[1:]

    def chromatic(self):
        """Return the 12-note chromatic scale starting from the tonic."""
        start = self._notes.index(self.tonic)
        return self._notes[start:] + self._notes[:start]

    def interval(self, intervals):
        """
        Build a scale from the tonic following the given interval pattern.
        intervals: string like "MMmMMMm"
        """
        chroma = self.chromatic()
        idx = 0
        result = [chroma[idx]]  # start on tonic

        for symbol in intervals:
            step = self.INTERVAL_STEPS[symbol]
            idx = (idx + step) % 12
            result.append(chroma[idx])

        return result
