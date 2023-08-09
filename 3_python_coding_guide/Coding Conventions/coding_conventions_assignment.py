# -*- coding: utf-8 -*-

import json


FILE_NAME = "./data/student_records.json"

def load_records():
    """
    Load student records from the JSON file.

    Returns:
        dict: Dictionary containing student records.
    """
    try:
        with open(FILE_NAME, 'r') as file:
            records = json.load(file)
    except FileNotFoundError:
        records = {}
    return records

def save_records(records):
    """
    Save student records to the JSON file.

    Args:
        records (dict): Dictionary containing student records.

    Returns:
        None
    """
    with open(FILE_NAME, 'w') as file:
        json.dump(records, file, indent=4)

def add_student(student_id, name, age, grade):
    """
    Add a new student to the records.

    Args:
        student_id (int): Student ID.
        name (str): Student name.
        age (int): Student age.
        grade (str): Student grade.

    Returns:
        None
    """
    records = load_records()
    records[student_id] = {"name": name, "age": age, "grade": grade}
    save_records(records)

def search_student_by_id(student_id):
    """
    Search for a student by student_id.

    Args:
        student_id (int): Student ID.

    Returns:
        dict: Dictionary containing student information (name, age, grade).
            Returns None if student not found.
    """
    records = load_records()
    student_id = int(student_id)
    return records.get(student_id)

def search_student_by_name(name):
    """
    Search for a student by name.

    Args:
        name (str): Student name.

    Returns:
        dict: Dictionary containing student information (name, age, grade).
            Returns None if student not found.
    """
    records = load_records()
    for student_id, info in records.items():
        if info["name"] == name:
            return {"name": info["name"], "age": info["age"], "grade": info["grade"]}
    return None

def update_student(student_id, age=None, grade=None):
    """
    Update a student's information by using student_id.

    Args:
        student_id (int): Student ID.
        age (int): New student age (optional).
        grade (str): New student grade (optional).

    Returns:
        None
    """
    records = load_records()
    if student_id in records:
        if age is not None:
            records[student_id]["age"] = age
        if grade is not None:
            records[student_id]["grade"] = grade
        save_records(records)

if __name__ == "__main__":
 
    add_student(1, "Raj Kumar Biswokarma", 24, "A")
    add_student(2, "Rabin Pokhrel", 23, "B")
    add_student(3, "Abhishek Adhikari", 25, "B")


    print(search_student_by_id(1))
    print(search_student_by_name("Raj Kumar Biswokarma"))

    update_student(1, age=21)
    print(search_student_by_id(1))
