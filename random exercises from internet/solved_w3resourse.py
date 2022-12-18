from SDA_studies.Autoestudio import solved_internet_exercises as sie
from math import ceil
import random
import logging

logging.basicConfig(level=logging.DEBUG)


class w3resourse():
    # 1. Write a Python function that takes a sequence of numbers and determines if all the numbers are different
    # from each other.
    num_list = sie.SomeExercises.Create_Random_List(6, 0, 6)

    def different_numbers(num_list):
        unique = True
        for num in num_list:
            if num_list.count(num) > 1:
                return False
        return unique

    # 2. Write a Python program to create all possible strings by using 'a', 'e', 'i', 'o', 'u'. Use the characters
    # exactly once

    def possible_strings(string):
        list_of_str = []
        original = string
        word = ''.join(string)

        while word not in list_of_str:
            list_of_str.append(word)
            string = original
            random.shuffle(string)
            word = ''.join(string)

        return list_of_str

    # string = ['a', 'e', 'i', 'o', 'u']
    # print(w3resourse.possible_strings(string))

    # 3. Write a Python program to remove and print every third number from a list of numbers until the list becomes
    # empty.

    def every_third_number(self):
        num_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]

        while len(num_list) > 0:
            to_pop = ceil(len(num_list) / 3)


num_list = sie.SomeExercises.Create_Random_List(9, 0, 100)
to_pop = sie.SomeOtherExcersices.divisors(len(num_list))
# = ceil(len(num_list)/3)
logging.debug(to_pop)
