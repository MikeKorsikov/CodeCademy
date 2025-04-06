# review

class Student:
    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.grades = []
        self.attendance = {}  # Dictionary to track attendance {date: attended (bool)}

    def add_grade(self, grade):
        if isinstance(grade, Grade):  # Check if grade is of type Grade
            self.grades.append(grade)
        # Otherwise, do nothing

    def get_average(self):
        if not self.grades:  # If no grades, return 0
            return 0
        return sum(grade.score for grade in self.grades) / len(self.grades)

    def mark_attendance(self, date, attended=True):
        self.attendance[date] = attended  # Mark attendance for a date

    def attendance_percentage(self):
        if not self.attendance:  # If no attendance records, return 0
            return 0
        return (sum(self.attendance.values()) / len(self.attendance)) * 100


class Grade:
    minimum_passing = 65  # Class variable (shared by all instances)

    def __init__(self, score):
        self.score = score

    def is_passing(self):
        return self.score >= Grade.minimum_passing


# Creating student instances
roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)

# Adding grades to students
pieter.add_grade(Grade(100))  # Passing grade
pieter.add_grade(Grade(45))  # Failing grade
roger.add_grade(Grade(75))   # Passing grade
sandro.add_grade(Grade(90))  # Passing grade

# Marking attendance
pieter.mark_attendance("2023-10-01", True)   # Attended
pieter.mark_attendance("2023-10-02", False)  # Absent
pieter.mark_attendance("2023-10-03", True)   # Attended

roger.mark_attendance("2023-10-01", True)
roger.mark_attendance("2023-10-02", True)

# Demonstrating functionality
print(f"{pieter.name}'s Grades:")
for grade in pieter.grades:
    print(f"  - Score: {grade.score}, Passing: {grade.is_passing()}")

print(f"\n{pieter.name}'s Average Grade: {pieter.get_average():.2f}")  # (100 + 45) / 2 = 72.5
print(f"{pieter.name}'s Attendance: {pieter.attendance_percentage():.2f}%")  # 2/3 days = 66.67%

print(f"\n{roger.name}'s Average Grade: {roger.get_average()}")  # Only 75
print(f"{roger.name}'s Attendance: {roger.attendance_percentage()}%")  # 2/2 days = 100%

print(f"\n{sandro.name}'s Grades:")
for grade in sandro.grades:
    print(f"  - Score: {grade.score}, Passing: {grade.is_passing()}")  # Only 90 (passing)