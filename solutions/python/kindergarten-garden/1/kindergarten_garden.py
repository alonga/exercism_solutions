class Garden:
    DEFAULT_STUDENTS = [
        "Alice", "Bob", "Charlie", "David",
        "Eve", "Fred", "Ginny", "Harriet",
        "Ileana", "Joseph", "Kincaid", "Larry"
    ]

    PLANTS = {
        'V': "Violets",
        'R': "Radishes",
        'C': "Clover",
        'G': "Grass"
    }

    def __init__(self, diagram, students=None):
        self.rows = diagram.splitlines()
        self.students = sorted(students) if students else self.DEFAULT_STUDENTS

    def plants(self, student_name):
        index = self.students.index(student_name) * 2
        result = [
            self.PLANTS[self.rows[0][index]],
            self.PLANTS[self.rows[0][index + 1]],
            self.PLANTS[self.rows[1][index]],
            self.PLANTS[self.rows[1][index + 1]]
        ]
        return result
