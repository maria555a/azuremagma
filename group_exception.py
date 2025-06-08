class GroupLimitation(Exception):
    pass
class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.age} years old, {self.gender}"


class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"Student: {super().__str__()}, Record Book: {self.record_book}"

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.record_book == other.record_book
        return False

    def __hash__(self):
        return hash(self.record_book)

class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if not isinstance(student, Student):
            return
        if len(self.group) >= 10:
            raise GroupLimitation("There cannot be more than 10 students in a group.")
        self.group.add(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = '\n'.join(str(student) for student in self.group)
        return f'Group Number: {self.number}\n{all_students}'


if __name__ == "__main__":
    gr = Group('PD1')

    for i in range(10):
        st = Student('Male' if i % 2 == 0 else 'Female', 20 + i, f'FirstName{i}', f'LastName{i}', f'RB{i}')
        gr.add_student(st)

    print("Group after adding 10 students:")
    print(gr)

    try:
        extra_student = Student('Male', 22, 'Extra', 'Student', 'RB10')
        gr.add_student(extra_student)
    except GroupLimitation as exception:
        print("\nException when adding an 11th student:")
        print(exception)

