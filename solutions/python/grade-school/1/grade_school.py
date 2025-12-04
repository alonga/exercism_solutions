class School:
    def __init__(self):
        self.students_by_grade = {}
        self._added_history = []  # store success/failure of every add

    def add_student(self, name, grade):
        # Initialize grade if missing
        if grade not in self.students_by_grade:
            self.students_by_grade[grade] = []

        # Check if student exists anywhere already
        if name in self.roster():
            self._added_history.append(False)
            return False

        # Add student successfully
        self.students_by_grade[grade].append(name)
        self._added_history.append(True)
        return True

    def added(self):
        # Return entire history list
        return self._added_history

    def grade(self, grade_number):
        return sorted(self.students_by_grade.get(grade_number, []))

    def roster(self):
        full_list = []
        for grade in sorted(self.students_by_grade):
            full_list.extend(sorted(self.students_by_grade[grade]))
        return full_list
