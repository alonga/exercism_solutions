"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    """Round all provided student scores.

    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """
    # Use a list comprehension to apply round() to every item and return a new list.
    return [round(score) for score in student_scores]

# Note: If you specifically wanted to modify the list in-place (as your original code suggested), 
# the fix would be:
# for i in range(len(student_scores)):
#    student_scores[i] = round(student_scores[i])
# return student_scores

def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    """
    # Python treats 'True' as 1 and 'False' as 0.
    # The sum() function automatically counts how many times the condition is True.
    return sum(score <= 40 for score in student_scores)


def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    :param student_scores: list - of integer scores.
    :param threshold: int - threshold to cross to be the "best" score.
    :return: list - of integer scores that are at or above the "best" threshold.
    """
    
    # Use a list comprehension to filter the scores. 
    # The condition is 'score >= threshold' (at or above).
    return [score for score in student_scores if score >= threshold]



def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: int - value of highest exam score.
    :return: list - of lower threshold scores for each D-A letter grade interval.
    """
    
    # 1. Calculate the total point range available for D, C, B, and A grades.
    # The failing grade is <= 40, so the usable range starts at 41.
    point_range = highest - 40
    
    # 2. Divide this range by 4 (the number of intervals) to find the size of each grade level.
    # Integer division (//) is used since scores must be whole numbers.
    interval_size = point_range // 4
    
    # 3. Establish the minimum score for the 'D' grade.
    d_min = 41  # Since F is <= 40, the lowest D is 41
    
    # 4. Calculate the subsequent lower thresholds.
    c_min = d_min + interval_size
    b_min = c_min + interval_size
    a_min = b_min + interval_size
    
    # 5. Return the list in the required order: [D, C, B, A]
    return [d_min, c_min, b_min, a_min]


def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in descending order."""
    rankings = []
    for i in range(len(student_scores)):
        rank = i + 1
        rankings.append(f"{rank}. {student_names[i]}: {student_scores[i]}")
    return rankings


def perfect_score(student_info):
    """Return the first [name, 100] pair found in the list, or [] if none exists."""
    for name, score in student_info:
        if score == 100:
            return [name, score]
    return []

