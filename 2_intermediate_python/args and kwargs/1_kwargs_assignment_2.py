# Create a function create_student_report that takes the student's
# name as the first argument, the student's age as the second argument, and an
# arbitrary number of keyword arguments for the subjects and their respective
# scores. The function should return a dictionary with the student's information and a
# list of subjects along with their scores.


def create_student_report(name,age,**kwargs):
    """
        Creates a student report with the given name, age, and subject scores.

        Parameters:
            name : str
                The name of the student.

            age : int
                The age of the student.

            **kwargs : keyword arguments
                Keyword arguments representing subjects and their corresponding scores.

            Returns:
                dict
                    A dictionary containing the student's name, age, and a list of subjects with their respective scores.def create_student_report(name,age,**kwargs):
    """
    information ={'student_name': name,
                'student_age' : age,
                'subjects' :[]}
    for subject,score in kwargs.items():
        information['subjects'].append({'subject': subject, 'score': score})
        
    return information

def main():
    print(create_student_report("Raj",28,math = 30, science = 40))
    print(create_student_report("XYZ",26,css = 30,english = 60, html = 80))

if __name__ == "__main__":
    main()