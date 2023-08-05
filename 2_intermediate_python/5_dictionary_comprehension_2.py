# Given a dictionary with students' names as keys and
# their respective scores as values, create a new dictionary that contains only the
# students who scored more than 80 using dictionary comprehension

def student_dic(dict_):
    """
    Create a new dictionary with students who scored higher than 80.

    Args:
        dict_ (dict): The input dictionary with student names as keys and their corresponding scores.

    Returns:
        dict: A new dictionary containing only students with scores greater than 80.

    """
   
    new_dict = {names: scores for names, scores in dict_.items() if scores > 80}
    return new_dict

def main():
    print(student_dic({"Raj":50,"Kumar":90,"Biswokarma":85}))
    print(student_dic({"R":90,"B":80,"C": 87}))

if __name__ == "__main__":
    main()
