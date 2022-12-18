# Given a string, return a new string where "not " has been added to the front. However, if the string already begins
# with "not", return the string unchanged.

# not_string('candy') → 'not candy'
# not_string('x') → 'not x'
# not_string('not bad') → 'not bad'


def not_string(str):
    if "not" in str[:3]:
        return str
    else:
        return "not " + str


# print(not_string('candy'))
# print(not_string('x'))
# print(not_string('not bad'))
# print(not_string('bad'))
# print(not_string('not'))
# print(not_string('is not'))
# print(not_string('no'))


# Given a non-empty string and an int n, return a new string where the char at index n has been removed. The value of
# n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).
#
#
# missing_char('kitten', 1) → 'ktten'
# missing_char('kitten', 0) → 'itten'
# missing_char('kitten', 4) → 'kittn

def missing_char(str, n):
    obj = str[n]
    return str.remove(obj)


# Given a string, return a new string where the first and last chars have been exchanged.
#
#
# front_back('code') → 'eodc'
# front_back('a') → 'a'
# front_back('ab') → 'ba'

def front_back(str):
    new_word = ""
    if len(str) == 1:
        return str
    else:
        word = list(str)
        first = str[0]
        last = str[-1]
        word[0] = last
        word[-1] = first
        for x in word:
            new_word += x
    return new_word


# print(front_back('code'))
# print(front_back('a'))
# print(front_back('ab'))


# Given a string, we'll say that the front is the first 3 chars of the string. If the string length is less than 3,
# the front is whatever is there. Return a new string which is 3 copies of the front.

def front3(str):
    return str[:3] * 3


# print(front3('Java'))# → 'JavJavJav'
# print(front3('Chocolate'))# → 'ChoChoCho'
# print(front3('abc'))# → 'abcabcabc'


# Given two int values, return their sum. Unless the two values are the same, then return double their sum.
def sum_double(a, b):
    if a != b:
        return a + b
    else:
        return (a + b) * 2


# print(sum_double(1, 2))# → 3
# print(sum_double(3, 2))# → 5
# print(sum_double(2, 2))# → 8

# We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling. We are in trouble if
# they are both smiling or if neither of them is smiling. Return True if we are in trouble.

def monkey_trouble(a_smile, b_smile):
    return (a_smile is b_smile)


# print(monkey_trouble(True, True))# → True
# print(monkey_trouble(False, False))# → True
# print(monkey_trouble(True, False))# → False


# We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23.
# We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble.
def parrot_trouble(talking, hour):
    if talking:
        if hour > 20 or hour < 7:
            return True
        else:
            return False
    else:
        return False


# print(parrot_trouble(True, 6))# → True
# print(parrot_trouble(True, 7))# → False
# print(parrot_trouble(False, 6))# → False
# print(parrot_trouble(False, 21))# → False


# Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.
def makes10(a, b):
    return ((a == 10) or (b == 10) or (a + b == 10))


# print(makes10(9, 10))# → True
# print(makes10(9, 9))# → False
# print(makes10(1, 9))# → True


# Given a string and a non-negative int n, return a larger string that is n copies of the original string.
def string_times(str, n):
    return str * abs(n)


# string_times('Hi', 2)# → 'HiHi'
# string_times('Hi', 3)# → 'HiHiHi'
# string_times('Hi', 1)# → 'Hi'


# Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars,
#  or whatever is there if the string is less than length 3. Return n copies of the front;
def front_times(str, n):
    return str[:3] * n


# print(front_times('Chocolate', 2))# → 'ChoCho'
# print(front_times('Chocolate', 3))# → 'ChoChoCho'
# print(front_times('Abc', 3))# → 'AbcAbcAbc'


# Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".

def string_bits(str):
    i = 1
    word = ""
    for char in str:
        if i % 2 != 0:
            word += char
        i += 1
    return word


# print(string_bits('Hello'))# → 'Hlo'
# print(string_bits('Hi'))# → 'H'
# print(string_bits('Heeololeo'))# → 'Hello'

# Given a non-empty string like "Code" return a string like "CCoCodCode".
def string_splosion(str):
    i = 1
    word = ""
    for char in str:
        word += str[:i]
        i += 1
    return word


# print(string_splosion('Code'))# → 'CCoCodCode'
# print(string_splosion('abc'))# → 'aababc'
# print(string_splosion('ab'))# → 'aab'


# Given a string, return the count of the number of times that a substring length 2 appears in the string and also as
# the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).

def last2(str):
    # last 2 chars, can be written as str[-2:]
    last2 = str[len(str) - 2:]
    count = 0

    # Check each substring length 2 starting at i
    for i in range(len(str) - 2):
        sub = str[i:i + 2]
        if sub == last2:
            count = count + 1

    return count


# last2('hixxhi')# → 1
# last2('xaxxaxaxx')# → 1
# last2('axxxaaxx')# → 2

# Given an array of ints, return the number of 9's in the array.
def array_count9(nums):
    nines = 0
    for item in nums:
        if item == 9:
            nines += 1
    return nines


# print(array_count9([1, 2, 9]))# → 1
# print(array_count9([1, 9, 9]))# → 2
# print(array_count9([1, 9, 9, 3, 9]))# → 3


# Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be
# less than 4.
def array_front9(nums):
    return 9 in nums[:4]


# print(array_front9([1, 2, 9, 3, 4]))# → True
# print(array_front9([1, 2, 3, 4, 9]))# → False
# print(array_front9([1, 2, 3, 4, 5]))# → False


# Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.
def array123(nums):
    i = 0
    j = i + 1
    k = j + 1
    for num1 in nums:
        if num1 == 1:
            for num2 in nums[j:]:
                if num2 == 2:
                    for num3 in nums[k:]:
                        if num3 == 3:
                            return True
        i += 1
    return False


# print(array123([1, 1, 2, 3, 1]))# → True
# # print(array123([1, 1, 2, 4, 1]))# → False
# # print(array123([1, 1, 2, 1, 2, 3]))# → True


# Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. So
# "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.

def string_match(a, b):
    i = 1
    counter = 0
    for char_a in a:
        j = 1
        if i < len(a):
            sector_a = char_a + a[i]
            # print(sector_a)
            i += 1
            if sector_a in b:
                counter += 1
    return counter


# print(string_match('xxcaazz', 'xxbaaz'))# → 3
# print(string_match('abc', 'abc'))# → 2
# print(string_match('abc', 'axc'))# → 0


# Given a non-negative number "num", return True if num is within 2 of a multiple of 10.
# Note: (a % b) is the remainder of dividing a by b, so (7 % 5) is 2. See also: Introduction to Mod


def near_ten(num):
    print(num % 10)
    if abs(num % 10 - 10) <= 2 or num % 10 <= 2:
        return True
    return False


# near_ten(12)# → True
# near_ten(17)# → False
# near_ten(19)# → True

# We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch each) and big
# bricks (5 inches each). Return True if it is possible to make the goal by choosing from the given bricks.
# This is a little harder than it looks and can be done without any loops. See also: Introduction to MakeBricks

def make_bricks(small, big, goal):
    b_bricks = []
    s_bricks = []
    for _ in range(small):
        s_bricks.append(1)
    for _ in range(big):
        b_bricks.append(5)
    print(s_bricks, b_bricks)

    while goal > 0:
        if goal >= 5 and b_bricks:
            goal -= 5
            b_bricks.pop()
            if goal == 0:
                return True
        elif s_bricks:
            for _ in s_bricks:
                goal -= 1
                s_bricks.pop()
                if goal == 0:
                    return True
        else:
            return False


# print(make_bricks(3, 1, 8), 'True')  # → True
# print(make_bricks(3, 1, 9), 'False')  # → False
# print(make_bricks(3, 2, 10), 'True')  # → True
# print(make_bricks(3, 1, 8), 'True' ) # → True
# print(make_bricks(3, 1, 9), 'False')  # → False
# print(make_bricks(3, 2, 10), 'True')  # → True
# print(make_bricks(3, 2, 8), 'True')  # → True
# print(make_bricks(0, 2, 10), 'True')  # → True
# print(make_bricks(1000000, 1000, 1000100), 'True')  # → True
# print(make_bricks(2, 1000000, 100003), 'False')  # → False
# print(make_bricks(20, 0, 19), 'True')  # → True
# print(make_bricks(20, 0, 21), 'False')  # → False
# print(make_bricks(20, 4, 51), 'False')  # → False
# print(make_bricks(20, 4, 39), 'True')  # → True
# print(make_bricks(1, 4, 11), 'True')  # → True
# print(make_bricks(3, 2, 9), 'False')  # → False
# print(make_bricks(6, 1, 11), 'True')  # → True
# print(make_bricks(6, 0, 11), 'False')  # → False

# Given 3 int values, a b c, return their sum. However, if one of the values is the same as another of the values,
# it does not count towards the sum
def lone_sum(a, b, c):
    num_list = [a, b, c]
    for x in num_list:
        if num_list.count(x) > 1:
            for num in range(num_list.count(x)):
                num_list[num_list.index(x)] = 0

    total = 0
    for num in num_list:
        total += num
    return total


# print(lone_sum(1, 2, 3), '6')  # → 6
# print(lone_sum(3, 2, 3), '2')  # → 2
# print(lone_sum(3, 3, 3), '0')  # → 0

# Given 3 int values, a b c, return their sum. However, if one of the values is 13 then it does not count towards the
# sum and values to its right do not count. So for example, if b is 13, then both b and c do not count.
def lucky_sum(a, b, c):
    from functools import reduce
    num_list = [a, b, c]
    for element in num_list:

        if element == 13:
            index_13 = num_list.index(element)
            next_zero = index_13 + 1
            next_next_zero = next_zero + 1
            num_list[index_13] = 0

            if num_list[index_13] is not num_list[-1]:
                num_list[next_zero] = 0
                if num_list[next_zero] is not num_list[-1]:
                    num_list[next_next_zero] = 0

    return reduce(lambda x, y: x + y, num_list)


# print(lucky_sum(1, 2, 3))  # → 6
# print(lucky_sum(1, 2, 13))  # → 3
# print(lucky_sum(1, 13, 3))  # → 1
# print(lucky_sum(13, 13, 2))  # → 0
# print(lucky_sum(13, 2, 3))  # → 0

# Given 3 int values, a b c, return their sum. However, if any of the values is a teen -- in the range 13..19 inclusive
# -- then that value counts as 0, except 15 and 16 do not count as a teens. Write a separate helper "def fix_teen(n):
# "that takes in an int value and returns that value fixed for the teen rule. In this way, you avoid repeating the
# teen code 3 times (i.e. "decomposition"). Define the helper below and at the same indent level as the
# main no_teen_sum().

def no_teen_sum(a, b, c):
    from functools import reduce
    ages = [a, b, c]
    for age in ages:
        if age in range(13, 20):
            index = ages.index(age)
            ages[index] = fix_teen(age)
    return reduce(lambda x, y: x + y, ages)


def fix_teen(n):
    if n == 15 or n == 16:
        return n
    return 0


# print(no_teen_sum(1, 2, 3))  # → 6
# print(no_teen_sum(2, 13, 1))  # → 3
# print(no_teen_sum(2, 1, 14))  # → 3

# For this problem, we'll round an int value up to the next multiple of 10 if its rightmost digit is 5 or more,
# so 15 rounds up to 20. Alternately, round down to the previous multiple of 10 if its rightmost digit is less than
# 5, so 12 rounds down to 10. Given 3 ints, a b c, return the sum of their rounded values. To avoid code repetition,
# write a separate helper "def round10(num):" and call it 3 times. Write the helper entirely below and at the same
# indent level as round_sum().


def round_sum(a, b, c):
    """works perfect here but not in the page"""
    num_list = [a, b, c]
    fives = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]
    for num in num_list:

        if num in fives:
            fix = num + 1
            print(num_list[num_list.index(num)], '→', round10(fix), end=' ')
            num_list[num_list.index(num)] = round10(fix)

        else:
            print(num_list[num_list.index(num)], '→', round10(num), end=' ')
            num_list[num_list.index(num)] = round10(num)

    total = 0
    for num in num_list:
        total += num
    return total


def round10(num):
    return int(round(num / 10)) * 10


# print('=', round_sum(16, 17, 18), 60)  # → 60
# print('=', round_sum(12, 13, 14), 30)  # → 30
# print('=', round_sum(6, 4, 4), 10)  # → 10
# print('=', round_sum(16, 17, 18), 60)  # → 60
# print('=', round_sum(12, 13, 14), 30)  # → 30
# print('=', round_sum(6, 4, 4), 10)  # → 10
# print('=', round_sum(4, 6, 5), 20)  # → 20
# print('=', round_sum(4, 4, 6), 10)  # → 10
# print('=', round_sum(9, 4, 4), 10)  # → 10
# print('=', round_sum(0, 0, 1), 0)  # → 0
# print('=', round_sum(0, 9, 0), 10)  # → 10
# print('=', round_sum(10, 10, 19), 40)  # → 40
# print('=', round_sum(20, 30, 40), 90)  # → 90
# print('=', round_sum(45, 21, 30), 100)  # → 100
# print('=', round_sum(23, 11, 26), 60)  # → 60
# print('=', round_sum(23, 24, 25), 70)  # → 70
# print('=', round_sum(25, 24, 25), 80)  # → 80
# print('=', round_sum(23, 24, 29), 70)  # → 70
# print('=', round_sum(11, 24, 36), 70)  # → 70
# print('=', round_sum(24, 36, 32), 90)  # → 90
# print('=', round_sum(14, 12, 26), 50)  # → 50
# print('=', round_sum(12, 10, 24), 40)  # → 40


# Given three ints, a b c, return True if one of b or c is "close" (differing from a by at most 1), while the other
# is "far", differing from both other values by 2 or more. Note: abs(num) computes the absolute value of a number.

def close_far(a, b, c):
    if abs(a - b) <= 1:
        return abs(b - c) >= 2 and abs(a - c) >= 2
    elif abs(a - c) <= 1:
        return abs(c - b) >= 2 and abs(a - b) >= 2
    return False


# print(close_far(1, 2, 10))  # → True
# print(close_far(1, 2, 3))  # → False
# print(close_far(4, 1, 3))  # → True
# print(close_far(4, 5, 3)  )#→ False
# print(close_far(4, 3, 5)  )#→ False
# print(close_far(-1, 10, 0))# → True
# print(close_far(8, 6, 9)  )#→ True
# print(close_far(10, 10, 8))# → True
# print(close_far(-1, 10, 0))# → True
# print(close_far(4, 1, 3)  )#→ True

# We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars (5 kilos each).
# Return the number of small bars to use, assuming we always use big bars before small bars. Return -1 if it can't be
# done.


def make_chocolate(small, big, goal):
    """works fine, not in the page"""
    leftover = goal
    big_value = 5
    for bar in range(big):
        if leftover - big_value >= 0:
            leftover -= big_value

    if leftover <= small and leftover >= 0:
        return leftover

    return -1


"""normal cases"""


# print(make_chocolate(4, 1, 9), 4)  # → 4
# print(make_chocolate(4, 1, 7), 2)  # → 2
# print(make_chocolate(6, 2, 7), 2)  # → 2	Timed out	X
# print(make_chocolate(5, 4, 9), 4)  # → 4	Timed out	X
# print(make_chocolate(1, 2, 6), 1)  # → 1	Timed out	X
# print(make_chocolate(1, 2, 5), 0)  # → 0	Timed out	X
# print(make_chocolate(6, 1, 10), 5)  # → 5	Timed out	X
# print(make_chocolate(6, 1, 11), 6)  # → 6	Timed out	X
# print(make_chocolate(6, 2, 10), 0)  # → 0
# print(make_chocolate(6, 2, 11), 1)  # → 1
# print(make_chocolate(4, 1, 5), 0)  # → 0	Timed out	X
# print(make_chocolate(9, 3, 18), 3)  # → 3	Timed out	X
# print(make_chocolate(6, 2, 12), 2)  # → 2
# print(make_chocolate(7, 1, 12), 7)  # → 7
# print(make_chocolate(7, 2, 13), 3)  # → 3
#
# """-1 cases"""
# print(make_chocolate(4, 1, 10), -1)  # → -1
# print(make_chocolate(7, 1, 13), -1)  # → -1
# print(make_chocolate(4, 1, 4), 4)  # → 4	Timed out	X
# print(make_chocolate(3, 1, 9), -1)  # → -1	Timed out	X
# print(make_chocolate(1, 2, 7), -1)  # → -1	Timed out	X
# print(make_chocolate(6, 1, 12), -1)  # → -1	Timed out	X
# print(make_chocolate(6, 1, 13), -1)  # → -1	Timed out	X
#
# """big cases"""
# print(make_chocolate(60, 100, 550), 50)  # → 50
# print(make_chocolate(1000, 1000000, 5000006), 6)  # → 6


# Given a string, return a string where for every char in the original, there are two chars.

def double_char(str):
    new_str = ''
    for i in range(len(str)):
        new_str += str[i] * 2
    return new_str


# print(double_char('The'))  # → 'TThhee'
# print(double_char('AAbb'))  # → 'AAAAbbbb'
# print(double_char('Hi-There'))  # → 'HHii--TThheerree'

# Return the number of times that the string "hi" appears anywhere in the given string.
def count_hi(str):
    return str.count('hi')


# print(count_hi('abc hi ho'))  # → 1
# print(count_hi('ABChi hi'))  # → 2
# print(count_hi('hihi'))  # → 2

# Return True if the string "cat" and "dog" appear the same number of times in the given string.
def cat_dog(str):
    return str.count('cat') == str.count('dog')


# print(cat_dog('catdog'))  # → True
# print(cat_dog('catcat'))  # → False
# print(cat_dog('1cat1cadodog'))  # → True

# Return the number of times that the string "code" appears anywhere in the given string, except we'll accept any
# letter for the 'd', so "cope" and "cooe" count.

def count_code(str):
    code = 0
    for i in range(len(str) - 3):
        if str[i:i + 2] == 'co' and str[i + 3] == 'e':
            code += 1
    return code


# print(count_code('aaacodebbb'))  # → 1
# print(count_code('codexxcode'))  # → 2
# print(count_code('cozexxcope'))  # → 2


# Given two strings, return True if either of the strings appears at the very end of the other string,
# ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). Note:
# s.lower() returns the lowercase version of a string.

def end_other(a, b):
    # print(a.lower()[len(b.lower())*-1:], b.lower()[len(a.lower())  * -1:])
    return a.lower() in b.lower()[len(a.lower()) * -1:] or b.lower() in a.lower()[len(b.lower()) * -1:]


# print(end_other('Hiabc', 'abc'))  # → True
# print(end_other('AbC', 'HiaBc'))  # → True
# print(end_other('abc', 'abXabc'))  # → True

# Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period
# (.). So "xxyz" counts but "x.xyz" does not.

def xyz_there(str):
    what = False
    i = 0

    print(str)

    if "xyz" in str and len(str) > 1:

        for element in range(str.count("xyz")):

            i = str.find("xyz", i)

            for char in range(len(str)):

                if str.count('xyz'):

                    if str[str.find('xyz', i) - 1] == '.':
                        what = False
                    else:
                        what = True

            i += 2

    return what


# print(xyz_there('abcxyz'), True,"\n")  # → True
# print(xyz_there('abc.xyz'), False,"\n")  # → False
# print(xyz_there('xyz.abc'), True,"\n")  # → True
# print(xyz_there('abcxy'), False,"\n")  # → False
# print(xyz_there('xyz'), True,"\n")  # → True
# print(xyz_there('xy'), False,"\n")  # → False
# print(xyz_there('x'), False,"\n")  # → False
# print(xyz_there(''), False,"\n")  # → False
# print(xyz_there('abc.xyzxyz'), True,"\n")  # → True
# print(xyz_there('abc.xxyz'), True,"\n")  # → True
# print(xyz_there('.xyz'), False,"\n")  # → False
# print(xyz_there('12.xyz'), False,"\n")  # → False
# print(xyz_there('12xyz'), True,"\n")  # → True
# print(xyz_there('1.xyz.xyz2.xyz'), False,"\n")  # → False


# We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch each) and big
# bricks (5 inches each). Return True if it is possible to make the goal by choosing from the given bricks. This is a
# little harder than it looks and can be done without any loops. See also: Introduction to MakeBricks


def make_bricks(small, big, goal):
    """works fine, not in the page"""
    leftover = goal
    big_value = 5
    for brick in range(big):
        if leftover - big_value >= 0:
            leftover -= big_value

    if small >= leftover >= 0:
        return True

    return False


# print(make_bricks(3, 1, 8))  # → True
# print(make_bricks(3, 1, 9))  # → False
# print(make_bricks(3, 2, 10) ) # → True

