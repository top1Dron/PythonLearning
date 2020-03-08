class SchoolMember:
    """Represents all people in school."""

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('Created SchoolMember: {0}'.format(self.name))

    def tell(self):
        """gets info about SchoolMember"""
        print('Name: {0}\nAge: {1}'.format(self.name, self.age))


class Teacher(SchoolMember):
    """Represents teacher."""

    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('Created Teacher: {0}'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print("Salary: {0}\n".format(self.salary))


class Student(SchoolMember):
    """Represents student."""

    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('Created Student: {0}'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print("Marks: {0}".format(self.marks))


teacher = Teacher('Mrs. Shrividya', 40, 30000)
student = Student('Dron', 19, [99, 100, 85, 90, 83, 80, 100, 95])

print()

members = [teacher, student]
for member in members:
    member.tell()  # works as for teacher and for students
