class BowlingGame:
    def __init__(self):
        self.rolls = []

    def roll(self, pins):
        # 1. Basic Pin/Type Validation
        if not isinstance(pins, int) or pins < 0 or pins > 10:
            raise ValueError("invalid pin count, negative roll, or pin count exceeds pins on the lane")

        # 2. Game End Validation
        if self._is_complete():
            raise ValueError("cannot roll after game is over")

        # 3. Frame-Specific Validation (Must happen BEFORE appending the roll)
        frame_index = self._current_frame_index()

        if frame_index < 9:
            self._validate_standard_frame(pins)
        else:
            self._validate_tenth_frame(pins)

        self.rolls.append(pins)

    def score(self):
        if not self._is_complete():
            raise ValueError("score cannot be taken until the end of the game")

        score = 0
        roll_index = 0

        for frame in range(10):
            if roll_index >= len(self.rolls):
                 # Safety break for corrupted rolls list, though is_complete should prevent this
                 break

            if self.rolls[roll_index] == 10:  # Strike
                # Score = 10 + next two rolls
                score += 10 + self.rolls[roll_index + 1] + self.rolls[roll_index + 2]
                roll_index += 1  # A strike consumes 1 roll
            
            elif self.rolls[roll_index] + self.rolls[roll_index + 1] == 10:  # Spare
                # Score = 10 + next one roll
                score += 10 + self.rolls[roll_index + 2]
                roll_index += 2 # A spare consumes 2 rolls
            
            else:  # Open Frame
                # Score = sum of two rolls
                score += self.rolls[roll_index] + self.rolls[roll_index + 1]
                roll_index += 2 # An open frame consumes 2 rolls

        return score

    # ───────────────── Private Helper Methods ───────────────── #

    def _current_frame_index(self):
        """Calculates the 0-based index of the frame currently being rolled."""
        frame = 0
        i = 0
        while frame < 9 and i < len(self.rolls):
            if self.rolls[i] == 10:
                i += 1
            else:
                i += 2
            frame += 1
        return frame

    def _validate_standard_frame(self, pins):
        """Validates the second roll in frames 1-9 (prevents 5 + 6 = 11)."""
        
        frame_start_index = 0
        frame = 0
        i = 0
        
        # Find the starting index (i) of the current frame
        while frame < 9 and i < len(self.rolls):
            frame_start_index = i
            if self.rolls[i] == 10:
                i += 1
            else:
                i += 2
            frame += 1

        # Check if this is the second roll of the current frame (i.e., rolls has only moved one ball past the frame_start_index)
        if len(self.rolls) == frame_start_index + 1:
            prev_roll = self.rolls[-1]
            # Check if the previous roll was NOT a strike and the current roll exceeds 10 total
            if prev_roll != 10 and prev_roll + pins > 10:
                raise ValueError("pin count exceeds pins on the lane")

    def _tenth_frame_rolls(self):
        """Returns the rolls made in the 10th frame."""
        i = 0
        for frame in range(9):
            if i >= len(self.rolls):
                # Should not happen if called correctly, but safety check
                return [] 
            
            if self.rolls[i] == 10:
                i += 1
            else:
                i += 2
        
        # i is now the index of the first roll of the 10th frame
        return self.rolls[i:]

    def _validate_tenth_frame(self, pins):
        """Validates rolls for the 10th frame."""
        ten = self._tenth_frame_rolls()

        # R1: No validation needed, already checked pins < 10

        if len(ten) == 1:
            # R2: Check for sum > 10 only if R1 was NOT a strike
            first = ten[0]
            if first != 10 and first + pins > 10:
                raise ValueError("pin count exceeds pins on the lane")
            return

        if len(ten) == 2:
            first, second = ten[0], ten[1]
            
            # R3 is allowed ONLY if R1 or (R1+R2) is a strike or spare
            if first + second < 10:
                # If it's an open frame (e.g., 5, 4), a third roll is illegal
                raise ValueError("cannot roll after game is over")

            # If R1 was a strike (10) and R2 was not (e.g., 10, 5), R3 must not exceed 10
            if first == 10 and second < 10 and second + pins > 10:
                raise ValueError("pin count exceeds pins on the lane")
            
            # If R1 was a strike (10) and R2 was also a strike (10), R3 can be anything (0-10) -> OK
            # If R1+R2 was a spare (e.g., 5, 5), R3 can be anything (0-10) -> OK
            return

    def _is_complete(self):
        """Checks if the game has ended (10 frames completed)."""
        if self._current_frame_index() < 9:
            return False

        ten = self._tenth_frame_rolls()
        if len(ten) < 2:
            return False

        first, second = ten[0], ten[1]

        # If it's a Strike (10) or Spare (sum of two is 10), a bonus third roll is required
        if first == 10 or first + second == 10:
            return len(ten) == 3

        # Otherwise, for an open frame, only 2 rolls are allowed
        return len(ten) == 2