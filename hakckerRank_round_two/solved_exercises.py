import math

"""Sales by Match

There is a large pile of socks that must be paired by color. Given an array of integers representing the color of each 
sock, determine how many pairs of socks with matching colors there are.

Example
n = 7
ar = [1, 2, 1, 2, 1, 3, 2]

There is one pair of color 1 and one of color 2. There are three odd socks left, one of each color. The number of pairs 
is 2."""

n = 10
ar_ = [1, 1, 3, 1, 2, 1, 3, 3, 3, 3]


def sockMerchant(n, ar):
    str(n)
    pairs = 0
    for item in set(ar):
        amount = ar.count(item)
        pairs += math.floor(amount / 2)
    return pairs


"""Grading Students

HackerLand University has the following grading policy:

Every student receives a grade in the inclusive range from 0 to 100.
Any grade less than 40 is a failing grade.
Sam is a professor at the university and likes to round each student's grade according to these rules:

If the difference between the grade and the next multiple of 5 is less than 3, round grade up to the next multiple of 5.
If the value of grade is less than 38, no rounding occurs as the result will still be a failing grade.
Examples

grade = 84 round to 85 (85 - 84 is less than 3)
grade = 29 do not round (result is less than 40)
gradde = 57 do not round (60 - 57 is 3 or higher)
Given the initial value of  for each of Sam's  students, write code to automate the rounding process.

Sample Input 0
 4 
 73 67 38 33
 
Sample Output 0
75 67 40 33
"""

grades_ = [73, 67, 38, 33]


def gradingStudents(grades):
    new_grades = []
    """ grade = 84 round to 85 (85 - 84 is less than 3)
        grade = 29 do not round (result is less than 40)
        gradde = 57 do not round (60 - 57 is 3 or higher)"""
    for grade in grades:
        next_multiple_of_5 = int(math.floor((grade + 5) / 5) * 5)

        if grade < 38:
            new_grades.append(grade)
            # print(grade)
        elif next_multiple_of_5 - grade < 3:
            new_grades.append(next_multiple_of_5)
            # print(int(next_multiple_of_5))
        else:
            new_grades.append(grade)
            # print(grade)

    for item in new_grades:
        print(item)

    return new_grades


r"""Counting Valleys


An avid hiker keeps meticulous records of their hikes.During the last hike that took exactly steps, for every step it 
was noted if it was an uphill, , or a downhill, step.Hikes always start and end at sea level, and each step up or down 
represents a  unit change in altitude.We define the following terms:

A mountain is a sequence of consecutive steps above sea level, starting with a step up from sea level and ending with 
a step down to sea level. A valley is a sequence of consecutive steps below sea level, starting with a step down from 
sea level and ending with a step up to sea level. Given the sequence of up and down steps during a hike, 
find and print the number of valleys walked through. Example The hiker first enters a valley units deep.Then they 
climb out and up onto a mountain units high.Finally, the hiker returns to sea level and ends the hike. Function 
Description Complete the countingValleys function in the editor below. countingValleys has the following parameter(
s): int steps: the number of steps on the hike string path: a string describing the path Returns int: the number of 
valleys traversed Input Format The first line contains an integer, the number of steps in the hike. The second line 
contains a single string, of characters that describe the path. 

Explanation If we represent _ as sea level, a step up as /, and a step down as \, the hike can be drawn as: 


Sample Input 8 UDDDUDUU
Sample Output 1 

_ /\         _
    \       /
     \ / \ /
    
"""

steps_1 = 8
path_1 = "UDDDUDUU"
output_1 = r"""
_ /\         _
    \       /
     \ / \ /
"""

steps_2 = 12
path_2 = "DDUUDDUDUUUD"
output_2 = r"""
_          /\_
 \  /\    /
  \/  \/\/
"""

steps_3 = 9
path_3 = "DDDUUUUUUDDD"
output_3 = r"""
         /\
        /  \
_      /    \_
 \    /
  \  /
   \/  
"""


# -> OK
def just_count_valleys(path):

    level = 0
    in_a_valley = False
    valeys = 0

    # evaluate level of height
    for c in path:
        if c == "U":
            level += 1
        elif c == "D":
            level -= 1
        if not in_a_valley:
            if level < 0:
                in_a_valley = True
                valeys += 1

        if in_a_valley:
            if level >= 0:
                in_a_valley = False

    return valeys


def make_step_values(steps, path):
    first_step = [0, "_", 0]
    step_values = [first_step]
    level = 0
    index = 0
    anterior = level

    # evaluate level of height
    for c in path:
        if c == "U":
            anterior = level
            level += 1
        elif c == "D":
            level -= 1
            anterior = level

        index += 1
        step_values.append([index, c, anterior])
        anterior = level
    last_step = [steps + 1, "_", anterior]
    step_values.append(last_step)

    return step_values


def get_level(element):
    return element[2]


def order_path_to_print(element):
    return sorted(element, key=get_level, reverse=True)


def display_path_steps(ordered_list, print_on=True):
    graph = """"""

    different_levels = set()

    for item in ordered_list:
        different_levels.add(item[2])
    list(different_levels)
    different_levels = sorted(different_levels, reverse=True)

    for current_level in different_levels:
        used_spaces = 0

        for item in ordered_list:

            if item[2] == current_level:

                if item[1] == "U":
                    graph += " " * (item[0] - used_spaces) + "/"
                    used_spaces += (item[0] - used_spaces) + 1
                elif item[1] == "D":
                    graph += " " * (item[0] - used_spaces) + "\\"
                    used_spaces += (item[0] - used_spaces) + 1
                else:
                    graph += " " * (item[0] - used_spaces) + "_"
                    used_spaces += (item[0] - used_spaces) + 1
        graph += "\n"
    if print_on:
        print(graph)
    return graph


def countingValleys(steps, path):
    # find level of steps
    step_values = make_step_values(steps, path)

    # order by highest level
    ordered_list = order_path_to_print(step_values)

    # print path
    display_path_steps(ordered_list)

    valleys = just_count_valleys(path)
    print(valleys)
    return valleys


if __name__ == '__main__':
    # sockMerchant(n, ar_)
    # gradingStudents(grades_)
    # countingValleys(steps_1, path_1)
    # countingValleys(steps_2, path_2)
    # countingValleys(steps_3, path_3)

    # result1 = make_step_values(steps_1, path_1)
    # result2 = make_step_values(steps_2, path_2)
    # result3 = make_step_values(steps_3, path_3)

    # print("after valuate", path_1, path_2, path_3)
    # print(result1)
    # print(result2)
    # print(result3)

    # ordered_result1 = sorted(result1, key=get_level, reverse=True)
    # ordered_result2 = sorted(result2, key=get_level, reverse=True)
    # ordered_result3 = sorted(result3, key=get_level, reverse=True)

    # print("after ordered", path_1, path_2, path_3)
    # print(ordered_result1)
    # print(ordered_result2)
    # print(ordered_result3)

    # graph_1 = display_path_steps(ordered_result1)
    # graph_2 = display_path_steps(ordered_result2)
    # graph_3 = display_path_steps(ordered_result3)

    # print(graph_1)
    # print(graph_2)
    # print(graph_3)

    countingValleys(steps_1, path_1)
    countingValleys(steps_2, path_2)
    countingValleys(steps_3, path_3)
