class Student:
    def _init_(self, name):
        self.name = name
        self.grades = []
    
    def add_grade(self, grade):
        self.grades.append(grade)
    
    def calculate_gpa(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

# Function to display GPA for all students
def display_gpa(students):
    for student in students:
        gpa = student.calculate_gpa()
        print(f"{student.name}'s GPA: {gpa:.2f}")

# Example usage
students = [
    Student("srujan"),
    Student("naveen"),
    Student("Chandana")
]

# Add some grades
students[0].add_grade(3.5)
students[0].add_grade(4.0)
students[1].add_grade(2.5)
students[1].add_grade(3.0)
students[2].add_grade(3.2)
students[2].add_grade(3.8)

# Display GPAs
display_gpa(students)