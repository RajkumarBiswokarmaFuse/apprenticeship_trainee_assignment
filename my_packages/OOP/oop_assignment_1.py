"""
    Assignment that demonstates a Object Oriented Programming.
"""


class University:
    """This is a universit class."""

    def __init__(self, name, location):
        self._name = name
        self._location = location
        self._departments = []

    def add_department(self, department):
        """This function adds a department."""
        self._departments.append(department)

    def get_name(self):
        """This function gets a name of a university"""
        return self._name

    def get_location(self):
        """This function gets a location of a university."""
        return self._location

    def get_departments(self):
        """This function gets a departments of a university."""
        return self._departments

    def display_details(self):
        """This function dispays a details of university."""
        print(f"University Name: {self._name}")
        print(f"Location: {self._location}")
        print("Departments:")
        for department in self._departments:
            print(f" - {department.get_name()}")
        print("")


class Department(University):

    """This is a Department class which
    inherits the property of University Class.
    """

    def __init__(self, name, location, head):
        super().__init__(name, location)
        self._head = head
        self._courses_offered = []

    def add_course(self, course):
        """This function adds course in department."""
        self._courses_offered.append(course)

    def get_head(self):
        """This function gets a head  of the department."""
        return self._head

    def get_courses_offered(self):
        """This function gets course offered  in department."""
        return self._courses_offered

    def display_details(self):
        print(f"Department Name: {self._name}")
        print(f"Head of Department: {self._head}")
        print("Courses Offered:")
        for course in self._courses_offered:
            print(f" - {course}")
        print("")


# Example usage:

def main():
    """This is a main Function."""
    # Create a University
    university = University("Tribhuwan University", "Kathmandu")

    # Create Departments
    dept1 = Department("Computer Science", "Science Building", "Dr. Jhatka")
    dept2 = Department("Electrical Engineering",
                       "Engineering Building", "Dr. Electrician")

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


if __name__ == "__main__":
    main()
