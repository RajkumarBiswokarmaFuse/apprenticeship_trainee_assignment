# Create a Python class to represent a University. The university should have
# attributes like name, location, and a list of departments. Implement encapsulation to
# protect the internal data of the University class. Create a Department class that
# inherits from the University class. The Department class should have attributes like
# department name, head of the department, and a list of courses offered. Implement
# polymorphism by defining a common method for both the University and
# Department classes to display their details.

class University:
    def __init__(self, name, location):
        self._name = name
        self._location = location
        self._departments = []

    def add_department(self, department):
        self._departments.append(department)

    def get_name(self):
        return self._name

    def get_location(self):
        return self._location

    def get_departments(self):
        return self._departments

    def display_details(self):
        print(f"University Name: {self._name}")
        print(f"Location: {self._location}")
        print("Departments:")
        for department in self._departments:
            print(f" - {department.get_name()}")
        print("")


class Department(University):
    def __init__(self, name, location, head):
        super().__init__(name, location)
        self._head = head
        self._courses_offered = []

    def add_course(self, course):
        self._courses_offered.append(course)

    def get_head(self):
        return self._head

    def get_courses_offered(self):
        return self._courses_offered

    def display_details(self):
        print(f"Department Name: {self._name}")
        print(f"Head of Department: {self._head}")
        print("Courses Offered:")
        for course in self._courses_offered:
            print(f" - {course}")
        print("")


# Example usage:

# Create a University
university = University("Tribhuwan University", "Kathmandu")

# Create Departments
dept1 = Department("Computer Science", "Science Building", "Dr. Jhatka")
dept2 = Department("Electrical Engineering", "Engineering Building", "Dr. Electrician")

# Add courses to departments
dept1.add_course("Introduction to Computer")
dept1.add_course("Data Structures and Algorithms")
dept2.add_course("Circuit Analysis")
dept2.add_course("Digital Signal Processing")

# Add departments to the university
university.add_department(dept1)
university.add_department(dept2)

# Display university and department details
university.display_details()
for department in university.get_departments():
    department.display_details()
