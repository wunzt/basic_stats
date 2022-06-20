# Author: Thomas Wunz
# GitHub username: wunzt
# Date: 6/20/2022
# Description: Takes a list of students with grades and returns a list of the mean, median, and mode of the grades.

import statistics

class Student:
    """Represents a student with a name and grade."""

    def __init__(self, name, grade):
        """Creates a new student object with a name and grade."""
        self._name = name
        self._grade = grade

    def get_grade(self):
        """Returns student's grade."""
        return self._grade

def basic_stats(student_list):
    """Takes a list of student objects and returns a tuple containing the mean, median, and mode of all the grades."""

    grade_list = []

    for student in student_list:
        grade_list.append(student.get_grade())

    mean_val = statistics.mean(grade_list)
    median_val = statistics.median(grade_list)
    mode_val = statistics.mode(grade_list)

    return (mean_val, median_val, mode_val)