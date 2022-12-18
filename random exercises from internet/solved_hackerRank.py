class Numbers:
    """We add a Leap Day on February 29, almost every four years. The leap day is an extra, or intercalary day and we add
    it to the shortest month of the year, February. In the Gregorian calendar three criteria must be taken into account
    to identify leap years:

    The year can be evenly divided by 4, is a leap year, unless: The year can be evenly divided by 100, it is NOT a leap
    year, unless: The year is also evenly divisible by 400. Then it is a leap year. This means that in the Gregorian
    calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap
    years.Source

    You are given the year, and you have to write a function to check if the year is leap or not.
    Note that you have to complete the function and remaining code is given as template."""

    @staticmethod
    def leap_year(year):
        leap = False
        if year % 4 == 0:
            leap = True
            if year % 100 == 0:
                leap = False
                if year % 400 == 0:
                    leap = True

        return leap

    """Task
    
    You are given a n X m integer array matrix with space separated elements ( n= rows and  m= columns).
    Your task is to print the transpose and flatten results."""

    """
    import numpy
    #transpose
    
    my_array = numpy.array([[1,2,3],
                            [4,5,6]])
    print numpy.transpose(my_array)
    
    #Output
    [[1 4]
     [2 5]
     [3 6]]
    
    
    # flatten
    my_array = numpy.array([[1,2,3], [4,5,6]])
    print my_array.flatten()
    
    #Output
    [1 2 3 4 5 6]"""

    """Let's learn about list comprehensions! You are given three integers x, y, and z representing the dimensions of a 
    cuboid along with an integer n. You have to print a list of all possible coordinates given by (i, j, k) on a 3D grid 
    where the sum of i + j + k is not equal to n. Here, 
    
    Input Format
    
    Four integers x, y, z and n each on four separate lines, respectively."""

    @staticmethod
    def list_comprehension(x, y, z, n):
        print([[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if ((i + j + k) != n)])

    # list_comprehension(2, 2, 2, 3)
    # list_comprehension(3, 4, 5, 5)
    # list_comprehension(-3, -2, 2, 0)
    # list_comprehension(0, -5, 2, 3)

    """
    Print the name(s) of any student(s) having the second lowest grade in Physics;
     if there are multiple students, order their names alphabetically and print each one on a new line."""

    my_list = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
    my_list2 = [['Harsh', 20], ['Beria', 20], ['Varun', 19], ['Kakunami', 19], ['Vikas', 21]]
    my_list3 = [['Rachel', -50], ['Mawer', -50], ['Sheen', -50], ['Shaheen', 51]]

    @staticmethod
    def Nested_Lists(points):
        second = sorted(Numbers.num_list(set([point for name, point in points])))[1]
        return '\n'.join([x for x, y in sorted(points) if y == second])

    @staticmethod
    def nested_list_input():
        n = int(input('Enter amount of students: '))
        points = [[input(f'Enter student name: '), float(input(f'Enter student grade: '))] for _ in range(n)]
        print(Numbers.Nested_Lists(points))

    # nested_list_input()
    # print(Nested_Lists(my_list))
    # print(Nested_Lists(my_list2))5
    # print(Nested_Lists(my_list3))

    """
    You have a record of n students. Each record contains the student's name, and their percent marks in Maths, 
    Physics and Chemistry. The marks can be floating values. The user enters some integer n followed by the names and 
    marks for n students. You are required to save the record in a dictionary data type. The user then enters a 
    student's name. Output the average percentage marks obtained by that student, correct to two decimal places."""

    @staticmethod
    def from_input_porcentage():
        n = int(input())
        student_marks = {}
        for _ in range(n):
            line = input().split()
            name, scores = line[0], line[1:]
            scores = map(float, scores)
            student_marks[name] = scores
        query_name = input()

        query_scores = student_marks[query_name]
        Numbers.porcentage_marks(query_scores)

    @staticmethod
    def turn_into_float(str_num_list):
        return [float(num) for num in str_num_list]

    @staticmethod
    def porcentage_marks(query_scores):
        query_scores = Numbers.turn_into_float(query_scores)
        porcentage = (sum(query_scores) / (len(query_scores)))
        # print('{0:.2f}'.format(porcentage))
        return '{0:.2f}'.format(porcentage)

    @staticmethod
    def porcentage_app(n, line, query_name):
        student_marks = {}
        for x in range(n):
            line_list = line[x].split()
            name, scores = f'{line_list[0]}', line_list[1:]
            student_marks[name] = scores

        query_scores = student_marks[query_name]
        return query_name, Numbers.porcentage_marks(query_scores)

    # print(porcentage_app(3, ['Krishna 67 68 69', 'Arjun 70 98 63', 'Malika 52 56 60'], 'Malika'))
    # print(porcentage_app(3, ['Krishna 67 68 69', 'Arjun 70 98 63', 'Malika 52 56 60'], 'Arjun'))
    # print(porcentage_app(3, ['Krishna 67 68 69', 'Arjun 70 98 63', 'Malika 52 56 60'], 'Krishna'))
    # print(porcentage_app(2, ['Harsh 25 26.5 28', 'Anurag 26 28 30'], 'Harsh'))
    # print(porcentage_app(2, ['Harsh 25 26.5 28', 'Anurag 26 28 30'], 'Anurag'))
    # print(porcentage_app(3, ['Riya 52 93 20', 'Rencho 69 65 62', 'Hbtg 52 60 68'], 'Hbtg'))
    # print(porcentage_app(3, ['Riya 52 93 20', 'Rencho 69 65 62', 'Hbtg 52 60 68'], 'Rencho'))
    # print(porcentage_app(3, ['Riya 52 93 20', 'Rencho 69 65 62', 'Hbtg 52 60 68'], 'Riya'))

    """
    1.- insert i e: Insert integer e at position i.
    2.- print: Print the list.
    3.- remove e: Delete the first occurrence of integer e.
    4.- append e: Insert integer e at the end of the list.
    5.- sort: Sort the list.
    6.- pop: Pop the last element from the list.
    7.- reverse: Reverse the list.
    Initialize your list and read in the value of N followed by N lines of commands where each command will be of the 7 
    types listed above. Iterate through each command in order and perform the corresponding operation on your list. """

    @staticmethod
    def eval_command(n):
        num_list = []
        for i in range(n):
            line = input().split()
            command = line[0]
            args = line[1:]
            if command != "print":
                command += "(" + ",".join(args) + ")"
                eval("l." + command)
            else:
                print(num_list)

    @staticmethod
    def from_str_eval_command(n, strs):
        l = []
        for i in range(n):

            s = strs[i].split()

            command = s[0]
            args = s[1:]
            if command != "print":
                command += "(" + ",".join(args) + ")"
                eval("l." + command)
            else:
                print(l)

    n = 12
    strs = [
        'insert 0 5',
        'insert 1 10',
        'insert 0 6',
        'print',
        'remove 6',
        'append 9',
        'append 1',
        'sort',
        'print',
        'pop',
        'reverse',
        'print',
    ]
    # from_str_eval_command(n, strs)

    """Task Given an integer, n, and n space-separated integers as input, create a tuple, t, of those n integers. Then 
    compute and print the result of hash(t). 
    Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.
    
    Input Format
    The first line contains an integer, n, denoting the number of elements in the tuple.
    The second line contains n space-separated integers describing the elements in tuple t.
    
    Output Format
    Print the result of hash(t).
    
    Sample Input 0
    2
    1 2
    
    Sample Output 0
    3713081631934410656"""

    @staticmethod
    def hash_tuple(tuple_):
        hash(tuple_)

    @staticmethod
    def make_tuple(str_):
        return tuple(i for i in str_)

    @staticmethod
    def read_command(n, str_):
        #  n = int(input())
        #  integer_list = map(int, input().split())
        integer_list = map(int, str_.split())
        integer_tuple = Numbers.make_tuple(integer_list)
        return Numbers.hash_tuple(integer_tuple)

    # read_command('12')

    """Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. 
    You are given  scores. Store them in a list and find the score of the runner-up. 
    
    Input Format
    The first line contains . The second line contains an array   of  integers each separated by a space.
    
    Output Format
    Print the runner-up score.
    
    Sample Input 0
    5
    2 3 6 6 5
    
    Sample Output 0
    5
    Explanation 0
    Given list is . The maximum score is , second maximum is . Hence, we print  as the runner-up score."""

    @staticmethod
    def runner_up(num_list):
        new_list = sorted(list(set([i for i in num_list])))
        return new_list[-2]

    @staticmethod
    def from_str_read(str_):
        if ' ' in str_:
            return str_.split(' ')
        return str_.split()

    # num_list = '2 3 6 6 5'
    # print(runner_up(from_str_read(num_list)))

    """Task
    Given an integer, n, perform the following conditional actions:

    If  is odd, print Weird
    If  is n even and in the inclusive range of 2 to 5, print Not Weird
    If  is n even and in the inclusive range of 6 to 20, print Weird
    If  is n even and greater than 20, print Not Weird
    """

    @staticmethod
    def weird_or_not(n):
        if n % 2 == 1:
            print("Weird")
        elif n % 2 == 0 and n in range(2, 6):
            print("Not Weird")
        elif n % 2 == 0 and n in range(6, 21):
            print("Weird")
        elif n % 2 == 0 and n > 20:
            print("Not Weird")


class Strings:
    """In Python, a string can be split on a delimiter.

    Example:
    # >>> a = "this is a string"
    # >>> a = a.split(" ") # a is converted to a list of strings.
    # >>> print a
    ['this', 'is', 'a', 'string']
    Joining a string is simple:

    # >>> a = "-".join(a)
    # >>> print a
    this-is-a-string
    Task
    You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

    Input Format
    The first line contains a string consisting of space separated words.

    Output Format
    Print the formatted string as explained above.

    Sample Input

    this is a string
    Sample Output

    this-is-a-string"""

    @staticmethod
    def split_and_join(line):
        str_list = line.split(' ')
        return '-'.join(str_list)

    """
    You are given the firstname and lastname of a person on two different lines. Your task is to read them and print the following:

    Hello firstname lastname! You just delved into python.
    
    Input Format
    
    The first line contains the first name, and the second line contains the last name.
    
    Constraints
    
    The length of the first and last name ≤ .
    
    Output Format
    
    Print the output as mentioned above.
    
    Sample Input 0
    
    Ross
    Taylor
    Sample Output 0
    
    Hello Ross Taylor! You just delved into python.
    Explanation 0
    
    The input read by the program is stored as a string data type. a string is a collection of characters."""

    @staticmethod
    def print_full_name(first_name, b):
        return f"Hello {first_name} {b}! You just delved into python."

    #  Ross Taylor! You just delved into python.

    """
    We have seen that lists are mutable (they can be changed), and tuples are immutable (they cannot be changed).
    
    Let's try to understand this with an example.
    
    You are given an immutable string, and you want to make changes to it.
    
    Example
    
    >>> string = "abracadabra"
    You can access an index by:
    
    >>> print string[5]
    a
    What if you would like to assign a value?
    
    >>> string[5] = 'k' 
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: 'str' object does not support item assignment
    How would you approach this?
    
    One solution is to convert the string to a list and then change the value.
    Example
    
    >>> string = "abracadabra"
    >>> l = list(string)
    >>> l[5] = 'k'
    >>> string = ''.join(l)
    >>> print string
    abrackdabra
    Another approach is to slice the string and join it back.
    Example
    
    >>> string = string[:5] + "k" + string[6:]
    >>> print string
    abrackdabra
    Task
    Read a given string, change the character at a given index and then print the modified string.
    
    Input Format
    The first line contains a string, s.
    The next line contains an integer i, denoting the index location and a character c separated by a space.
    
    Output Format
    Using any of the methods explained above, replace the character at index i with character c.
    
    Sample Input
    
    abracadabra
    5 k
    Sample Output
    
    abrackdabra"""

    @staticmethod
    def mutate_string(string, position, character):
        return string[:position] + character + string[position + 1:]
        # str in python are inmutables so you need to slice it and concatenate it

    """
    You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

    For Example:
    
    Www.HackerRank.com → wWW.hACKERrANK.COM
    Pythonist 2 → pYTHONIST 2
    
    Input Format
    a single line containing a string .
    
    Output Format    
    Print the modified string .
    
    Sample Input 0    
    HackerRank.com presents "Pythonist 2".
    Sample Output 0
    
    hACKERrANK.COM PRESENTS "pYTHONIST 2"."""

    @staticmethod
    def swap_case(line):
        return line.swapcase()

    """
    Task
    You are given a string . Your task is to find out if the string  contains: alphanumeric characters, alphabetical 
    characters, digits, lowercase and uppercase characters. 
    
    In the first line, print True if  has any alphanumeric characters. Otherwise, print False.
    In the second line, print True if  has any alphabetical characters. Otherwise, print False.
    In the third line, print True if  has any digits. Otherwise, print False.
    In the fourth line, print True if  has any lowercase characters. Otherwise, print False.
    In the fifth line, print True if  has any uppercase characters. Otherwise, print False."""

    @staticmethod
    def string_validator(s):
        print(any(c.isalnum() for c in s))
        print(any(c.isalpha() for c in s))
        print(any(c.isdigit() for c in s))
        print(any(c.islower() for c in s))
        print(any(c.isupper() for c in s))

    # Strings.string_validator('lowercase')

    """
    #Replace all ______ with rjust, ljust or center. 
    
    thickness = int(input()) #This must be an odd number
    c = 'H'
    
    #Top Cone
    for i in range(thickness):
        print((c*i).______(thickness-1)+c+(c*i).______(thickness-1))
    
    #Top Pillars
    for i in range(thickness+1):
        print((c*thickness).______(thickness*2)+(c*thickness).______(thickness*6))
    
    #Middle Belt
    for i in range((thickness+1)//2):
        print((c*thickness*5).______(thickness*6))    
    
    #Bottom Pillars
    for i in range(thickness+1):
        print((c*thickness).______(thickness*2)+(c*thickness).______(thickness*6))    
    
    #Bottom Cone
    for i in range(thickness):
        print(((c*(thickness-i-1)).______(thickness)+c+(c*(thickness-i-1)).______(thickness)).______(thickness*6))"""

    """In Python, a string of text can be aligned left, right and center.
    
    .ljust(width)
    
    This method returns a left aligned string of length width.
    
    >>> width = 20
    >>> print 'HackerRank'.ljust(width,'-')
    HackerRank----------  
    .center(width)
    
    This method returns a centered string of length width.
    
    >>> width = 20
    >>> print 'HackerRank'.center(width,'-')
    -----HackerRank-----
    .rjust(width)
    
    This method returns a right aligned string of length width.
    
    >>> width = 20
    >>> print 'HackerRank'.rjust(width,'-')
    ----------HackerRank"""

    @staticmethod
    def HR_logo(thickness=5):  # fucking dificult

        # thickness = int(input())  # This must be an odd number
        c = 'H'

        # Top Cone
        for i in range(thickness):
            print((c * i).ljust(thickness - 1) + c + (c * i).rjust(thickness - 1))

        # Top Pillars
        for i in range(thickness + 1):
            print((c * thickness).ljust(thickness * 2) + (c * thickness).rjust(thickness * 6))

        # Middle Belt
        for i in range((thickness + 1) // 2):
            print((c * thickness * 5).center(thickness * 6))

            # Bottom Pillars
        for i in range(thickness + 1):
            print((c * thickness).ljust(thickness * 2) + (c * thickness).rjust(thickness * 6))

            # Bottom Cone
        for i in range(thickness):
            print(
                ((c * (thickness - i - 1)).center(thickness) + c + (c * (thickness - i - 1)).rjust(thickness)).rjust(
                    thickness * 6))

    """In this challenge, the user enters a string and a substring. You have to print the number of times that the 
    substring occurs in the given string. String traversal will take place from left to right, not from right to left. 
    
    NOTE: String letters are case-sensitive.
    
    Input Format
    
    The first line of input contains the original string. The next line contains the substring."""

    @staticmethod
    def count_substring(string, sub_string):
        pos = 0
        segment = len(sub_string)
        counter = 0
        lenth = len(string)
        for a in range(lenth):
            if sub_string in string[pos:pos + segment]:
                counter += 1
            pos += 1

        return counter

    @staticmethod  # IMPORTANT
    def text_parragraph_maker(string, max_width):
        import textwrap
        wraped_text = '\n'.join(string[i * max_width:i * max_width + max_width] for i in range(len(string) - max_width))
        for line in wraped_text:
            print(line)
        return wraped_text

    """Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

    Mat size must be X x Y. (x is an odd natural number, and X is 3 times Y .)
    The design should have 'WELCOME' written in the center.
    The design pattern should only use |, . and - characters."""

    @staticmethod
    def door_pattern(x, y, center_text='WELCOME', mid_draw=".|.", fill_draw='-'):
        pattern = ""
        max_mid = y - 2

        if x / y == 3:

            # top cone
            for row in range(y // 2):
                top_mid = ""
                top_mid += mid_draw * ((row * 2) + 1)
                line = top_mid.center(x, fill_draw)
                pattern += line + "\n"

            # mid line
            pattern += center_text.center(x, fill_draw) + "\n"

            # bottom cone
            for row in range(y // 2):
                bottom_mid_mid = ""
                bottom_mid = mid_draw * (max_mid - (row * 2))

                line = bottom_mid.center(x, fill_draw)
                pattern += line + "\n"

            return pattern
        else:
            print('invalid values, X must be 3x Y')

    """Given an integer, n, print the following values for each integer n from 1 to n:

    Decimal
    Octal
    Hexadecimal (capitalized)
    Binary
    The four values must be printed on a single line in the order specified above for each n from 1 to n . 
    Each value should be space-padded to match the width of the binary value of ."""

    @staticmethod
    def print_formatted_mine(n):

        # print("The decimal value of", dec, "is:")
        # print(bin(n), "in binary.")
        # print(oct(n), "in octal.")
        # print(hex(n), "in hexadecimal.")
        # return[[x, str(hex(x)).strip('0x'), str(oct(x)).strip('0o'), str(bin(x)).strip('b')] for x in range(1, n + 1)]

        # print("Hello {0}, your balance is {blc}.".format("Adam", blc=230.2346))

        result = ""
        num_list = [[" {0}  {0:o}  {0:X}  {0:b}".format(x)] for x in range(1, n + 1)]
        for list in num_list:
            for item in list:
                result += " " + item
            result += "\n"
        return result

    @staticmethod
    def print_formatted(n):

        w = len("{0:b}".format(n))
        result = ""

        for x in range(1, n + 1):
            result += "{0:{w}d} {0:{w}o} {0:{w}X} {0:{w}b}\n".format(x, w=w)

        return result

    """You are given an integer, N. Your task is to print an alphabet rangoli of size N. (Rangoli is a form of Indian 
    folk art based on creation of patterns.) """

    @staticmethod
    def print_rangoli_solu1(n):
        import string
        alpha = string.ascii_lowercase

        # n = int(input())
        L = []
        for i in range(n):
            s = "-".join(alpha[i:n])
            L.append((s[::-1] + s[1:]).center(4 * n - 3, "-"))
        print('\n'.join(L[:0:-1] + L))

    @staticmethod
    def print_rangoli_solu2(num):
        import string

        alpha = string.ascii_lowercase

        # num = int(input())

        def srange(N):
            return list(range(N)) + list(range(N - 2, -1, -1))

        for i in srange(num):
            print('-'.join([alpha[num - j - 1] for j in srange(i + 1)]).center(4 * (num - 1) + 1, '-'))

    @staticmethod
    def print_rangoli_solu3(size):
        import string
        # if size % 2 == 0:
        #     print("""you have entered a wrong number!
        #     the required number must be odd""")
        #     size = int(input("enter an odd number: "))
        width = 4 * size - 3
        alpha = string.ascii_lowercase
        for i in list(range(size))[::-1] + list(range(1, size)):
            print('-'.join(alpha[size - 1:i:-1] + alpha[i:size]).center(width, '-'))

    """You are asked to ensure that the first and last names of people begin with a capital letter in their 
    passports. For example, alison heck should be capitalised correctly as Alison Heck. Given a full name, 
    your task is to capitalize the name appropriately. """

    # print(Strings.solve('victor grinan valdes 35g'))
    @staticmethod
    def capitalize(s):

        topindex = len(s)
        index = 0
        new_frase = ""
        while index < topindex:
            char = s[index]
            if s[index - 1] == " " or s.index(char) == 0:
                char = char.upper()
            new_frase += char
            index += 1

        print(new_frase)
        return new_frase

    # print(Strings.capitalize('hello   world  lol'))  # note the two spaces together
    # print(Strings.capitalize('132 456 Wq  m e'))

    @staticmethod
    def solve1(s):

        import string

        print(string.capwords(s, ' '))

        return string.capwords(s, ' ')

    @staticmethod
    def solve2(s):

        for x in s[:].split():
            s = s.replace(x, x.capitalize())
        print(s)
        return s

    @staticmethod
    def solve3(s):
        for x in s[:].split(" "):
            s = s.replace(x, x.capitalize())
            s = "".join(s)
            print(s)
        return s

    """Game Rules

    Both players are given the same string, s.
    Both players have to make substrings using the letters of the string s.
    Stuart has to make words starting with consonants.
    Kevin has to make words starting with vowels.
    The game ends when both players have made all possible substrings.
    
    Scoring
    a player gets +1 point for each occurrence of the substring in the string s.
    
    For Example:
    String  = BANANA
    Kevin's vowel beginning word = ANA
    Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points."""

    @staticmethod
    def the_minion_game(s):  # NOTE: if the string is too long it give a memory error

        vowels = 'AEIOU'

        kev = 0
        stu = 0

        substring_list = [s[i:(len(s) - j)] for i in range(0, len(s)) for j in range(0, len(s))]
        substring_list = [sub for sub in substring_list if sub != '']

        for i in substring_list:
            if i[0].upper() in vowels:
                kev += 1
            else:
                stu += 1
        if kev < stu:
            print('Stuart', stu)
            return 'Stuart', stu

        elif kev > stu:
            print('Kevin', kev)
            return 'Kevin', kev

        else:
            print('Draw')
            return 'Draw'

    @staticmethod
    def solv_comunity1(s):
        vowels = 'AEIOU'

        kevsc = 0
        stusc = 0

        for i in range(len(s)):
            if s[i] in vowels:
                kevsc += (len(s) - i)
            else:
                stusc += (len(s) - i)

        if kevsc > stusc:
            return "Kevin", kevsc
        elif kevsc < stusc:
            return "Stuart", stusc
        else:
            return "Draw", kevsc

    @staticmethod
    def solv_comunity2(s):
        vw = 'aeiou'.upper()
        strl = len(s)
        kevin = sum(strl - i for i in range(strl) if s[i] in vw)
        stuart = strl * (strl + 1) / 2 - kevin

        if kevin == stuart:
            print('Draw')
        elif kevin > stuart:
            print('Kevin %d' % kevin)
        else:
            print('Stuart %d' % stuart)

    @staticmethod
    def how_many_substrings(s):
        strl = len(s)
        return strl * (strl + 1) / 2

    @staticmethod
    def all_substrings(s):

        substring_list = [s[i:(len(s) - j)] for i in range(0, len(s)) for j in range(0, len(s))]
        substring_list = [sub for sub in substring_list if sub != '']

        return substring_list

    """Merge the Tools! split the string in the given number parts, and for each segment erase repeated characters"""

    @staticmethod
    def merge_tool(s, n):
        start = 0
        max = len(s)
        print(max)
        top = int(max/n)
        print(top)
        chunk = int(max/top)
        top_chunk = chunk

        for _ in range(top):

            print(s[start:top_chunk])
            start += n
            top_chunk += chunk


# Strings.merge_tool("AABCAAADA", 3) Strings.merge_tool(
# """KYQYTWXTDQXWDLKIXNWIITFBLIHRNGDZGVYCRXVWNUVSFFACUXMCSTFFBNWQVBQCWOEPNBOAVJUCOUGITSMNLSUOFRFAUXETNIKAJYCEJWIXSOHMGUBT
# OWKVPPXJOCEBKPDWNFCXDLWVZEJIALBOJLLYCIJQKOTXDWTSDVRIGOEIUPQUCRKLFVLHFXASNVPSUKKXHCGOSMYMDOIGHUTMPHWWEYORTFJNPVNXZVNTJ
# NFMBPSIJOXAVTXZRNSKTDAKANJAKYTTLBFMSAXCOUCJNBKGPESKHSWJHGJREFKSISGASDCIZHTOKFUBJNLSFIBPQNGWSROCLVCDAHNAQGOALJCUYPOFZP
# UPEDMYWAAHXDKAMXACFQCQBGMZWAHVRBNYEZWABXJBCVBOSDQZTSPVZDWXFDSZHFXNGTQISZLUVMKPPAPIVGFWKCTRHNQQVPEBJULDVYAQKKGBLXMIDREP
# VZHFMZVJPZNAVADRZDHJOPNBMZLSQRHOQQTEQQOFSDFNDKGCOQOEFBHUASMSJTIBMDFCUVHOYOBCYKGOAWSHXBDZTPUELEFXINZEIISJYVNWFTNHQHPPJS
# REKNJXRQUZDVDOFVZDRMBYHOGZYXRHRILBVWYMPUOURRIWPJBIVFGFVOGTLXADHOGCMHRBDFWVYGTPQVXNCGUXUBRGYTLGJRKWADZEIVZJEUAURAJTGER
# CFIKFDVLNPWJPZITKGUVKPVGGXPADVTGCBQIGOTTDREUTPQFVKCFBZNKXEMAAFICIBMOPGKUZOQUDGZYTDFUDUGAZUCBZNFJQSAFAKBBYRWEYXETBMPEG
# WGHQKISZOBPIDWINXJORHSRFWKGIZMRXSYOEHIEXLTHPQPCPASGIMXPJJVTJHMGBLWHUELTQHAHZRJOTEXDQWSBGNXPWJXXWUHQASJSBLZCCJRWPQZFMU
# HSHEJEPHDMDKCDFOWIZVLEGECVUDDIXKDFQMLFVQRYDWEKMCSNZFRGJTDFZGOWSTBIFOOBHHBKDHUPJMDJSWRDSUJRDZNVSRGZHUCODGYHNUYXJDIDCZG
# UVRNYSAWMTCMDYORBWSKKMJJVORYQSHMNAZOTCKFVORAMISNEKAQYLZUZSUSKDEYEEMXGYEDMYEYGYNMKNDIYEEAXBSHEYHICVHKTMQHKUFSUVGEKJMLQ
# TNNUFWYDEJIBQSVCIEOEMGAHNETYTEOMRDGYAEEGNMJGGEIRLZVXFYEUCXTVEJJXNPWPWAXLMGRUNCLYBHVIFBDJAYHGHQEWGANECMPQTJKILWIOFFWMI
# BVIZCPJVVHDVVHXJYPEHZMUVUKABJMJKISMMJVHGCKBZTAJSPPBOCYMYIMARZLEJFQXQNHWPRZRNBCFQRIHVGVURHWKIJOTPGRFTYCLRBEGDGLVZWEVEZ
# RVJPIRYWLNFETAEVLXYPEBXRZXNDSSDLPMAXFYWSMBYHBCCPACGGEEXDDLIXFNIUBISHGOBURABSCFJEIQKOWITZVBWCPEWQOQZUEBRXBSQFYBKGRWUNE
# NMBQKDFQCYESXZZYQWBKOHIQRQHNMXUBLXSWDZMFXRXVSYVKVZULGFBZXLOKKKNVIFTLFISEBPBTQZFNYBYEIADGNTSXEFSMLOZSWRYXIASYZXLXAMDJM
# IRBBJYHQSTDGUXENWBWYTWXSKWVWBGKJXLMILUADPEMKBQZZSVXNUWIESDCVJMEIZTSKNSPEYBOAUQBOLZBFVLLQONLZBQJALDMYWCCWFTYZJAPWZTEUE
# RKVFWWIOGJZJVZHZDEHWCGHCYGDRKYVBKSIIPRYVCZGZYOZCUGAYOKDMQGFCGDFTVQBKHAHLBOKAELEARGYISDWIKCMSFULCKPNRRUCSKOUOAYQTHRBZU
# AKGCWZJQMLCBATSVXNHOHYOGOHPFLOALYGPXHAPUNSVONQLNDSBKQPSHYHMLYOYWXNTEPLYDDWRQMCDRWGDNXWWWFIJDXICWXXANIZQNXJEJNJCJQFYN
# DULLFXOEFSACQAPYBHMYQSJDDLPVTNLWKWHPTYTAQVDGVUHZCVZUNJYQWPOPEZMOXVFTTATKVWSTTBUVWTPJCPCZGQQLPEZOAHHVJBHFZAASBUPYNHJSW
# NTFFJQWORLQYSLITTPVTRNWLFWAMISKVLPBXFXNXKDXDOHYHYTCPJBAOXBAFVKDJCEIHDVGOYGTONRYMLCDUDEKDHKICWLNYRVIXQONQWGHMZFAMHDGN
# SQQCYVBMIZFGJEYARPWZYIZDILMMUZVMPORQJSCTTJZDOYDHPZHPKGSURGINGGAXURNFLRYEDAJRAMYROFGYNAUHGDUOJUMFNBKYTIFWIOPKDPBRVHRIJ
# LPQQMGBISGWWQWPZDNJSEWXTXOQHHZQUQILEPONJVJFLHWMLLYFPUEJTSZCBATXTDIXSZMEUVJFFGUSTSZJODUHXVKYYFVRIGQDFDHBASIHACZUWYDMDZ
# UAUGYUNWLXEEALJJMLEUVEZUYVVDIYEEBZMBTZXHWDNZOYKALOXGTWDTTYZDYDHZETBAUAHTEWUSWEVHVSOQQRLJRKNPOWRSSSSMSBHYZBRVIODDGTVYM
# GHDRWUHTLZLFUZYXHYXKPUSFXXNSSLEZVJSREZMRAZXWZXUIVTSNNLSNIGFDRMEOVWGZXUTZUQYVNUDINXVCIOPTWXYNJCCGAKIZGBAARYVGUAOJYMMIC
# DDYCBNNFRUFDCGKFHKYHIECKSNIGBTIFYIJAWXHPTPTXVFCERAMBEQMYDWFFPPMQYXQWUZLNOGMKLOOFQCGUSSVYPAFGPTWPQOLNOZACFPOTDDYWFEQAZ
# NYQPFWFYVWOLIDBHGGOVUHYZHUHONHNCHDSOBZMYVCKFGNMMTBHOKHPSEWITFVXMAPABOOCMTORBBGNVHWLTFANLXVGCQERSTTWKIYWDMPENVTKCRVYWW
# LKVHQXZUQSQKQAUOYXCNDRJWCNNZNLXZVSIOSJIIDASTCOJANLQQFBMJQBIENGDIANWSWHBAJVVMMFOZSEQXHEIYGRCTZHDZUCSSLVUUSQGEVXEPBWNJA
# VJGOLZPSFPOJJIUGDOYTXFQUJFXFUIFSROIENYYUPMDYXXEAOEVNJLJUSGZPRHHIVPPKPNFECKCZKIZYPWNYJWTBEUQXDZIYRXLGKSLMCPLMAMMPIBPRX
# KVEFNDINLJGIUMTMZHQRVDTHRISTZJSKEWRUABHNKNWEBRSDAJWVOPDFZVYYGTKNRBHRDOHPDDUGWOJWZHSNWXTVSTWAMGNGKUXNKECPJYWHPHEOPYCLV
# XJPSFRHNFNZBMOMTTBERZMIJSXYQBLNYWESDVZRAOSCBHQUATYTTMCCEZCWCPJAMPUPLUINIBRLKJHKDIDYUFCZGEXIVJKHYFZLBJZJMSXWCEGFMMDHRH
# IALFIIOVSPARABCBMRULPWQYDCKILDPVDCDOKTLCILVJOAMCRGOGEGEHKQRYUGTZIWNVSYZALVLBXYGOGWWLCDUOTMMPUGPFEEAWFZZSWKUTKCJRYGECL
# YQGMFWHLNORRQQWRPROBLJMPTFPBJROHJUWOSFBFTTXJLVAAMQDZCPOVWFYFWOPIILWBQAILVFWGDWIPPLRRDFOZLOHJCWTMJSPBSYMNDIVGGDYXQPOTWE
# VJSCVWYOJHGYKYWWNCGIKONIMEXCZWJUFBWAAWPJFXJPWGLLKTUUIJFWPCAPAJJGNIINEXWMVFBTNPEXIAUSMZQBDRQEACMNKUAQSYCPGGKTVOTFRPYD
# OQERHXXKZJXLEABYAGNGMXCJNVOEKOJAFQTMNRWMCWXGYAEYITFWSHFIEWOQKYQPOJEBCAPFYOLYOSXZNEVINDQTZGJJGZBUKFXNHOSGCFGTZDSPJPZYU
# RRTXAFEBGAOLABSOVATCHMEMGTYVSWSJOLIQQMSWPGJPJCDGEWILKMAQHYOBUGMITVBMJTIYBUNKYTQCRAQCPQUWOKYIQKTMHUYRPIPSCFEAYUDRWTTL
# JQIZAIJTUEFEAFVPNMHQTNSRJVLGQERBWBAXLKQIQXMRCJGPVQHPDAINXTVOAMPWQSVDENLUKXLOGUGEMNVRPFENBBDBQUZGMVJQIXNVUYJDURHGHEYW
# JELKGOLWJNEXIPQSMDPJDBMYSVGZZGYILJVTYGRJVXGFOWYBBNMFOAFHVLIWSGGFSBASKRBFOJLCGLFJYTOPTTYQHGMBPTGHWIZGZCMPLZTTKBDKUTZQ
# PXGWGVZXQHEMPFTOHHFUGYOSBTCYMCOBBUZHRYEHFKUURPKYWRVESJWTEYRQCFSECTNVSUDXEZUWQGWOYRSQCQLGQFZTKTZOMMKEIPEPQANGGLUGDOYHE
# MQURPPDIOSUDEBNVFCLFPTNBNWGBUPHGFBXWTDGHVBMBEAYJEJQUCFXRBFSYUZGCCGYVJFFGIRJMTHXYSPUUWTNAYFAUGGWKOVGZCNFMGOAAXXAPOULK
# YKNDKHLTGWJDEJFRQTXFTZESZUGVFSKEFZJRJXMPTWSZFZSVSPCNRHFQDNOIFAOMCYELVQCQOWRTVJRPAVCRCJKHWAQDAEQEEWPBMRTDNKYKVPBYLDPP
# MBXKDPOGVEKAAADOTXRJJQTHHXFSAWIPYHZBWNJRTUTTUZKPWDYHTUODRVVTSFKSOKVKZFEVZXQVWAKUELEZHUCYQATKHECWQXGRCMMDMDYKDJFJWLLDH
# NDXPWJXCLTSLBKNOYRABRKHARSWCDBMRELIBVFDGYYRAKHOIAQMRATUSNSWRUIKYUSBPYFXWFRYPYOXAEJTFENZSGVJCGVCCNETLLSKQJKFJZEJDQDKU
# SJOAHXCPUHRILMVWEHOOSVZRZLWRQHMIQALZAPOWWHEHTAFYJVOBQNUSARJQYXBQAMQCBGYYODHHFPHQKXSBLMVNFGEFEFYETQIUWGUMLEUSTDJFBDIOR
# DBXKHEQMCWHSEEPKYBYEXSZDBFEENUWTVVDFZTTEPBWVFNHFRFKQYJTBQZIETGXRBCWCXPGOSFJXUQDLWPEWAXXRZFVUNUNOWLTTBBHTIQTDIYOGNUCNU
# CETJBNXVDNTOIORKXLSPGVYEMETGJGANNVYQLXOOLJCTYUFVHALPVJTJPMSYUULJQMCDJQRUZVQZRXVAXIPVRIEGWYHTTUELGGQQYJMAEEZWCUWZCOUVW
# BEVZNQUHUHOBXGBGSBNZBLBXJACXXZUYDRZQHUABDQEBWGHQHUPKFSIPVMOSLKSRBRJINJMRZSSXYBQIYHUFACWVQLPCVHVZYEHMOVDPOXPOAFYYOTGOX
# CLOPASLHNKIRTUHRZZHYQXYVWZLPFAMHNCZOUKXJWFDRZKKALRYBPXYLYKCDMQMZTLPPXNZVUENWQXWCRXFGWETUQVXCLLDGXVYWKZSEDHATGZXXWDFSH
# YOXVNBJYGPXBPULOOQTVSNDRKBNPIHWHXVCKYLJFDIGUCULQKENCTRWGULVCVULSRQFQDQVGYDDDXOTJUJOOCMWYXRASNONFESVHISQIXTLXJHIDQWTU
# KPSIHUCWIPBMJYWTSMCQHNPQUXTMWNGGCAQLVTIFKLUUKQNCERULFLBBJWOHLWPQXGDUBNZLZVHLLXPROMCTXFXIELPPJHHINLEQAGBZBLMPICGWOJSL
# QPUUCLKLSTWHGAXHGZIIKVZUXFQNOKAHZUBDINRAHNINNFWWGFGSAFMZKFMBPMIRJLURZLTGYDVOLSMRXUMZZAYLFMOXAYOLKKEJWYRWDOMOIAIHUUGV
# WGHCUXBXWPIIZNTXNMWQAIFLJNSDJBZFJIJEFKBDBJNDYGALSWEVHJGSYAXJBYQNGAROMUTQFHTEPVRISVFBGNTEPQPTPGGXIXNWTHMYQFEFBWPVTWYA
# JRGZHWSYEYWMXLIQSXQKCVQFTFAMCAMNRVOBRIBXIZJFLTXDQQOVLGAENDQRDFFXAVYTEZQMZBUKWTPPJFKULMAZPTQVYXSATSTZRLLSOHEKBUZMBLHN
# YJOPCGKAGECBWXAQILIYVPJYJKKKWRZWDNLFWYICCKDBIDRSQBRNQCLBMWMKPNISDUYZUGDWSIZANQVFSMTKQEMEAAPQNZKQTIRPQWOJENJREGXYSQII
# WUNXUEPIDBAZKUOCQCLXSXOWDNUYDEICZVBVBQFHTGIDCYGSDTRVQGRUTNSZRCBSYCQBUVKNDSTFRBAUURPNZIJVVDUOFXJFZZHVWRKAMFHDGJZDBOQC
# WZXTCRJHQUNRTWMSPZSBEZELLFQOTGQRHOMJHYSYSFPOBEGRDYUJZBUKGMYCSRVZFIKOIDOAKEOOKUFPUBYWCVIJHJLCAGBHQOVYRKBDQPRCMYRIAPGC
# KPLUYYWAFZHXNEYGQZKGQBIEABNARTEDKQXKQTKXTRVIYTPOUZXKCHPCJEEAZJFKBFURYHPTAMCYHTNBSKNUREZAKFCKOKWRPSLPBAJCONAVGNYAZLWT
# SVVCDAORKMLZHWQIYBKMOLHWAHYCUVVMSQRVQFPCUADBYUJWVUIMFRKHYJJUGEHAXAWPFNSZPVANRKJNGTBNMNUMWEGEKPFHPDXVQRWFMZUELFTRYWEK
# JAWGGCMRURAJUZGKQDRFELLPQEIQCOALQYTXDGQXXQGSSNEKSYRYLCPCIXUKNXWDVPCAXSXVLGPDVVPPTHNFJCJUBDEOACTYSWYPQYMBEDGZZWQSDDZO
# HKIIONYQRROLPNDGNPHRTQSUMIMRNOFUYQCOFCFWVVILKLTXACOVSIPEQEXFSDZSVDHAFOWBJEOURHRULGPEQHKHLIOFNOZITGIZUECGLSACBRWMZOQQ
# VBZGJNNWDMGXVOYRUCXFUXKXRGJQUAIRDJZOZMMEBSDWGBNAFLIBKSYBYIUVKCMNOODNAPRDHVBPYPPECXHMPIOQQKNCMBRAPUPSLHVSEXHCOYISYSGP
# AWFQGUUTWLVNHLFSUDM " , 3452) """