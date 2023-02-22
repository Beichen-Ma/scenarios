def get_grade(score: int) -> str:
    """
    Calculates the grade of a student based on their score.

    Args:
    score (int): The score of the student.

    Returns:
    str: The grade of the student ('A', 'B', 'C', 'D', or 'E').
    """
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'E'
    return grade