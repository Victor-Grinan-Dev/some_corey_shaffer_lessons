import random
import logging


class SomeExercises:
    num_list = [i for i in range(10)]
    char_list = "me cago impunemente en la puta madre"

    # 3. Using any(), check whether any of the expressions are true: False, None, "a" in "abc"
    def any_all(num_list, char_list):
        print(any(i < 5 for i in num_list))  # true
        print(all(i < 5 for i in num_list))  # false
        print(any("a" for char in char_list))
        print(all(True for char in char_list))
        print(all(True for char in char_list))
        print(any(None for char in char_list))
        print(all(None for char in char_list))

    # 4. Convert "Ünicöde" to ASCII using ascii()
    def meh(self):
        print(ascii("Ünicöde"))

    # 5. Find out the binary representation of 19 using bin()
    def bin_num(x):
        return bin(x)

    # 6. bool() covered in the next chapter
    def true_or_false(self):
        bool(45)
        bool(-45)
        bool("abc")
        bool("")
        bool([0])
        bool([])

    # 7. breakpoint() starts a debugger session at the call site.
    def breakpoint(self):
        breakpoint()  # ??????????

    # 8. Using bytearray(), convert a string to byte array.
    def byte_array(self):
        byte = bytearray()
        print(byte)  # ??????????

    # 9. Using bytes(), convert a string to bytes literal.
    def bytes(self):
        SomeExercises.char_list.bytes()  # ??????????
        pass

    # 10. Using callable(), check whether bin() built-in function is callable.
    # print(callable(bin(8)))

    # 11. Using chr(), convert Unicode code 97 to a character.
    def chr_code(self):
        code = 97
        while code < 123:
            print(chr(code), end=" ")
            code += 1

    # 12. @classmethod is an advanced way of providing class constructors.

    # 13. compile is an advanced function used when parsing Python code.

    # 14. Use complex() to create a complex number 1+2j
    """nope, nonononon, NOPE"""

    # 15. delattr() is used to remove object's attribute.
    # 16. Pass keyword arguments to dict() to create a new dictionary.

    # 17. dir() will be covered in chapter 18

    # otros ejercisios
    # 1. Use count() to count occurrences of one or more characters in the string.
    def count_char(char, text):
        print(text.count(char))

    def count_char_arguments(self):
        text = input("write a text: ")
        char = input("what character u wanna count: ")

    # 2. Use find() to find the index of first occurrence of letter "a" in "anagram". Then try it again, with
    def find(a, b):
        return a.find(b)

    # 3. rfind() works just like find, but searches from the end of the string back to its
    """find reverse"""

    def rfind(a, b):
        return a.rfind(b)

    # 4. index() is like find(), but raises ValueError if the substring is not found. rindex() also exists.

    # 5. format() has been covered in chapter 6. Printing
    # 6. format_map() uses dictionary to apply the same formatting as format(). Format string "I like {something}"
    # using format_map()

    # 7. Use startswith() to check whether "pre" is a prefix of "preamble"
    # 8. Use endswith() to check, whether "tle" is the suffix of "my castle"
    # 9. Use strip(<iterable>) to remove all occurences of any of the symbols in iterable from string's beginning and
    # end.
    # 10. Likewise, you can use either lstrip() or rstrip() to remove symbols from string's beginning and end
    # respectively.
    # 11. Use split(<separator>) to split "first, second, third" into a list.
    # 12. Use splitlines() to split "first\nsecond" into a list.
    # 13. Use partition() to split string "Address: Rosewood St. 2113", assuming ":" is the separator. What is the
    # result?
    # 14. Use ", ".join(<list of strings>) with range(5) to get a string with comma-separated numbers. Use
    # comprehension to convert numbers to strings first.
    # 15. Use replace() to replace all occurrences of "X" to your name in "Welcome, X. Is it OK if I call you X?"
    # 16. Use center() with arbitrary length to center any string.
    # 17. Using ljust() and rjust() achieve the same result as "x".center(11)
    # 18. Check whether all characters in string "19²" are digits using isdigit().
    # 19. Check whether all characters in string "imminent" are alphabetic using isalpha().
    # 20. Use isalnum() to check, whether string "Rose Hightower, Sailsbury Rd 92" contains alphanumerics only. Fix
    # it if it contains anything else.
    # 21. Use isspace()to check if string " \t\n" contains whitespace only.
    # 22. Use lower() to convert "mIxED caSe sTRING" to lowercase.
    # 23. Use islower() to check if all letters in your string of choice are lowercase.
    # 24. Use title() to capitalize every word in "this could be a title"
    # 25. Use capitalize() to capitalize the following string "morocco is a beautiful country."
    # 26. Use istitle() to check whether the string "illiad" is titlecased. Use capitalize() to fix it and then check
    # again.
    # 27. Use upper() to convert a string of your choice to upper-case.
    # 28. Check whether a string of your choice is uppercased using isupper().
    # 29. Use swapcase() on "a vErY mIxEd Case string". What does it do?
    # 30. Use casefold() on "Straße" (German for street) and then compare it to "strasse"
    # 31. Use encode() to encode UTF-8 string "garçon"


class SomeOtherExcersices:

    @staticmethod
    def Create_Random_List(length, range_ini, range_end):
        return [random.randint(range_ini, range_end) for element in range(0, length)]

    # Exercise 2 "Odd Or Even" Ask the user for a number. Depending on whether the number is even or odd,
    # print out an appropriate message to the user. Hint: how does an even / odd number react differently when
    # divided by 2? Extras: If the number is a multiple of 4, print out a different message. Ask the user for two
    # numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into
    # num, tell that to the user. If not, print a different appropriate message.
    @staticmethod
    def odd_or_even(self):
        x = int(input("input a number: "))
        if x % 2 == 0:
            print(f"{x} is an even number", end="")
            if x % 4 == 0:
                print("... and actually is also a multiplo of 4")
            else:
                print("\n")
            return True
        else:
            print(f"{x} is an even number")
            return False

    @staticmethod
    def evenly_division(dividendo, divisor):

        if divisor != 0:
            return dividendo % divisor == 0
        else:
            return logging.warning('Dividion by 0 not defined')

    # Exercise 3 "List Less Than X" write a program that prints out all the elements of the list that are less than
    # 5 Extras: Instead of printing the elements one by one, make a new list that has all the elements less than 5
    # from this list in it and print out this new list. Write this in one line of Python. Ask the user for a number
    # and return a list that contains only elements from the original list a that are smaller than that number given
    # by the user.

    @staticmethod
    def List_Less_Than(num_list, compare_num):

        return [num for num in num_list if num < compare_num]

    # Exercise 4 "Divisors"
    # Create a program that asks the user for a number and then prints out a list of all the divisors of that number.

    @staticmethod
    def divisors(num):
        divisors = []
        for pos_div in range(1, num + 1):
            if num % pos_div == 0:
                divisors.append(pos_div)
        return divisors

    # Exercise 5 "List Overlap"
    # Take two lists, say for example these two:

    # and write a program that returns a list that contains only the elements that are
    # common between the lists (without duplicates). Make sure your program works on two lists of different sizes.
    @staticmethod
    def List_Overlap(listA, listB):
        over_lap = []
        for element in listA:
            for comparable in listB:
                if element == comparable:
                    over_lap.append(element)

        for element in over_lap:
            a = element
            index = 0
            if a == over_lap[index + 1]:
                over_lap.remove(element)
        for unique_item in over_lap:
            print(unique_item, end=" ")
        pass

    # Extras:
    # Randomly generate two lists to test this
    @staticmethod
    def Create_2_Random_list(list_len, num_bottom_len, num_top_range):

        a = [random.randint(num_bottom_len, num_top_range) for element in range(0, list_len)]
        b = [random.randint(num_bottom_len, num_top_range) for element in range(0, list_len)]

        return a, b

    # listA,listB = Create_2_Random_list()
    # List_Overlap(listA,listB)
    # Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)
    @staticmethod
    def list_overlap_one_line(listA, listB):
        listC = []
        listC = [element for element in listA if element in listB if element not in listC if element < 5]
        print(listC)

    # Exercise 6 "Palindrome"
    # Ask the user for a string and print out whether this string is a palindrome or not.
    @staticmethod
    def Palindrome_1st_I_did():  # meh
        # palindrome = input("input a palindrome phrase: ")
        # palindrome = "madam"
        palindrome = "mada adem"
        index = 0
        minus_index = -1
        is_palindrome = []  # bool list
        # revers = palindrome.__reversed__() #need to find function to reverse text
        for char in range(0, len(palindrome) // 2):
            if palindrome[index] == palindrome[minus_index]:
                is_palindrome.append(True)
            else:
                is_palindrome.append(False)
            minus_index -= 1
            index += 1
        print(is_palindrome)
        for stat in is_palindrome:
            print(stat)
            pass
        pass

    @staticmethod
    def Palindrome(palindrome):
        palindrome = str(palindrome)
        reverse = SomeOtherExcersices.reverse_word(palindrome)

        if palindrome == reverse:
            # print(f"{palindrome} is indeed a palindrome")
            return True
        else:
            # print("not really, but good try!!!")
            return False

    @staticmethod
    def is_palindrome_juhani(word):
        if len(word) == 0:
            return False
        return word == word[::-1] # god this was easy... not from me

    @staticmethod
    def reverse_word(word):
        revers_list = []
        index = 0
        for char in word:
            revers_list.insert(index, char)
            index += -1
            reverse = ""
        for item in revers_list:
            reverse += item
        return reverse

    # Exercise 7 "List Comprehensions"
    # Let’s say I give you a list saved in a variable:
    # # Write one line of Python that takes this list a and makes a new list that has only the even elements of this
    # list in it.
    @staticmethod
    def List_Comprehensions(listA):
        return [number for number in listA if number % 2 == 0]

    # Exercise 8 "Rock Paper Scissors" Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using
    # input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a
    # new game)
    """from Autoestudio import little_games_no_graph as lgng
    lgng.NoGraphGames.Rock_Paper_Scissors(self)"""

    @staticmethod
    def internet_solution():
        print('''Please pick one:
                    rock
                    scissors
                    paper''')

        while True:
            game_dict = {'rock': 1, 'scissors': 2, 'paper': 3}
            player_a = str(input("Player a: "))
            player_b = str(input("Player b: "))
            a = game_dict.get(player_a)
            b = game_dict.get(player_b)
            dif = a - b

            if dif in [-1, 2]:
                print('player a wins.')
                if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
                    continue
                else:
                    print('game over.')
                    break
            elif dif in [-2, 1]:
                print('player b wins.')
                if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
                    continue
                else:
                    print('game over.')
                    break
            else:
                print('Draw.Please continue.')
                print('')

    # Exercise 9 "Guessing Game One"
    # Generate a random number between 1 and 9, Ask the user to guess the number,
    # then tell them whether they guessed too low, too high, or exactly right.
    # Extras:
    # Keep the game going until the user types “exit”
    # Keep track of how many guesses the user has taken, and when the game ends, print this out.

    """lgng.NoGraphGames.guess_my_number()"""

    # Exercise 10 "List Overlap Comprehensions" and write a program that returns a list that contains only the
    # elements that are common between the lists (without duplicates). Make sure your program works on two lists of
    # different sizes. Write this in one line of Python using at least one list comprehension. Extra: Randomly
    # generate two lists to test this

    def list_overlap_comprehensions(listA, listB):
        listC = []
        listC = [element for element in listA if element in listB if element < 10 if element not in listC]
        print(f"{listA}")
        print(f"{listB}")
        print(f"{listC}")
        pass

    # Exercise 11 "Check Primality Functions"
    # Ask the user for a number and determine whether the number is prime or not.
    def Check_Primality_Functions(self):
        while True:
            num = int(input("\ninput 0 = exit\ninput a number > 1 to check primality: "))
            if num == 0:
                break
            elif num == 1:
                print(f"{num} is not a prime number")
            else:
                # divisors_list = []
                # for pos_div in range(1, num):
                #     if num % pos_div == 0:
                #         divisors_list.append(pos_div)
                divisors_list = SomeOtherExcersices.divisors(num)
                length = len(divisors_list)
                index = 1
                if length > 2:
                    print(f"the divisors for {num} are")
                    for element in divisors_list:
                        # print(element,end=" ")
                        if index < length:
                            print(element, end=", ")
                        else:
                            print("and", element, end=" ")
                        index += 1

                else:
                    print(f"the divisors for {num} are only {divisors_list[0]} and {num}")

                result = 1
                for element in divisors_list:
                    result *= element

                if result == num:
                    print(f"\n{num} is a prime number")
                else:
                    print(f"\n{num} is not a prime number")

    # Exercise 12 "List Ends"
    # Write a program that takes a list of numbers
    listA = [5, 10, 15, 20, 25]

    # and makes a new list of only the
    # first and last elements of the given list. For practice, write this code inside a function
    def List_Ends(listA):
        stop_index = len(listA)
        # print(stop_index)
        # listB =[element for element in listA if listA[element] == 0 if listA[element] == stop_index]
        listB = []
        for element in listA:
            if listA.index(element) == 0 or listA.index(element) == stop_index - 1:
                print(listA.index(element))
                listB.append(element)
        print(listB)
        pass

    # Exercise 13 "Fibonacci" Write a program that asks the user how many Fibonnaci numbers to generate and then
    # generates them. Take this opportunity to think about how you can use functions. Make sure to ask the user to enter
    # the number of numbers in the sequence to generate.(Hint: The Fibonnaci seqence is a sequence of numbers where the
    # next number in the sequence is the sum of the previous two numbers in the sequence. The sequence looks like this:
    # 1, 1, 2, 3, 5, 8, 13, …)
    @staticmethod
    def Fibonacci():
        limit = int(input("input how many number should we create: "))
        first_num = 0
        second_num = 1
        counter = 0
        fibonacci = []
        while counter < limit:
            fib_num = first_num + second_num
            fibonacci.append(fib_num)
            first_num = second_num
            second_num = fib_num
            counter += 1
        print(1, end=" ")
        for elememt in fibonacci:
            print(elememt, end=" ")
        pass

    # Exercise 14 "List Remove Duplicates"
    # Write a program (function!) that takes a list and returns a new list that contains all the elements of the first
    # list minus all the duplicates.
    # Extras:
    # Write two different functions to do this - one using a loop and constructing a list, and another using sets.
    # Go back and do Exercise 5 using sets, and write the solution for that in a different function.
    @staticmethod
    def List_Remove_Duplicates(listA):
        listB = []
        for element in listA:
            if element not in listB:
                listB.append(element)
        listB.sort()
        return listB

    def deldupli_v2(x):
        "internet solution"
        # sets cant have duplicated values
        # then turns it back to list type and sort it
        return list(set(x))

    # Exercise 15 "Reverse Word Order"
    # Write a program (using functions!) that asks the user for a long string containing multiple words.
    # Print back to the user the same string, except with the words in backwards order. For example,
    # say I type the string:

    #   My name is Michele
    # Then I would see the string:
    #   Michele is name My
    @staticmethod
    def Reverse_Word_Order(phrase):
        phrase_list = []
        reversed_phrase = []
        word = ""
        for char in phrase:
            if char == " ":
                phrase_list.append(word)
                word = ""
            else:
                word += char

        phrase_list.append(word)

        reversed_phrase.append(phrase_list[3])
        reversed_phrase.append(phrase_list[2])
        reversed_phrase.append(phrase_list[0])
        reversed_phrase.append(phrase_list[1])
        for word in reversed_phrase:
            print(word, end=" ")

        return reversed_phrase

    # phrase = input("input a 4-word phrase: ")
    # phrase = Reverse_Word_Order(input("input a 4-word phrase: "))
    "given solution in web"

    @staticmethod
    def reverse_v1(x):
        # this prints "victor is name my" (non sense)
        y = x.split()
        result = []
        for word in y:
            result.insert(0, word)
        return " ".join(result)

    # method 2
    @staticmethod
    def reverse_v2(x):
        # this prints "victor is name my" (non sense)
        y = x.split()
        return " ".join(y[::-1])

    # method 3
    @staticmethod
    def reverse_v3(x):
        # this prints "victor is name my" (non sense)
        y = x.split()
        return " ".join(reversed(y))

    # method 4
    @staticmethod
    def reverse_v4(x):
        # this prints "victor is name my" (non sense)
        y = x.split()
        y.reverse()
        return " ".join(y)

    # x = reverse_v4("my name is victor")
    # print(x)

    # Exercise 16 "Password Generator"
    # Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of
    # lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new
    # password every time the user asks for a new password. Include your run-time code in a main method.
    # Extra:
    # Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list
    """I dont think symbols are very common in paswords generators nowdays, but including all wanted symbols in the sample
    should fix the extra strenght of the password, i wont do it in this excercise"""

    @staticmethod
    def Password_Generator(password):
        print(f"Current pasword is: {password}")
        answer = {"a": 4, "b": 8, "c": 12}
        sample = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

        while True:
            strength = input(
                "input \"exit\" to quit\nchoose the strength of your password:\na)weak [4]\nb)medium [8]\na) strong [12]\n")
            if strength == "exit":
                break
            elif strength in answer:
                password = ""
                mid_password = random.sample(sample, answer[strength])
                for element in mid_password:
                    password += element
            else:
                print("invalid input, try again or", end=" ")

    "Password_Generator(None)"

    import string

    @staticmethod
    def Password_Generator_netSolution(size, chars=string.ascii_letters + string.digits + string.punctuation):
        print(size)
        return ''.join(random.choice(chars) for _ in range(size))

    # print(Password_Generator_netSolution(int(input('How many characters in your password?'))))

    # chars = string.ascii_letters
    # print(string.ascii_letters)
    # print(string.digits)
    # print(string.POINTS)
    # chars = string.ascii_letters + string.digits + string.POINTS
    # print(chars)

    @staticmethod
    def Password_Generator_ver2(password):
        import string
        print(f"Current pasword is: {password}")
        answer = {"a": 4, "b": 8, "c": 12}
        sample = string.ascii_letters + string.digits

        while True:
            strength = input(
                "input \"exit\" to quit\nchoose the strength of your password:\na) weak [4]\nb) medium [8]\nc) strong ["
                "12]\nd) own size")
            if strength == "exit":
                break
            elif strength in answer:
                password = ''.join(random.choice(sample) for _ in range(answer[strength]))
                print(password)
            elif strength == "d":
                password = ''.join(
                    random.choice(sample) for _ in range(int(input("How many characters in your password? "))))
                print(password)
            else:
                print("invalid input, try again or", end=" ")

    # Password_Generator_ver2(None)

    #
    # Exercise 18 "Cows And Bulls"
    # Create a program that will play the “cows and bulls” game with the user. The game works like this:
    # Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the user
    # guessed correctly in the correct place, they have a “cow”. For every digit the user guessed correctly in the
    # wrong place is a “bull.” Every time the user makes a guess, tell them how many “cows” and “bulls” they have.
    # Once the user guesses the correct number, the game is over. Keep track of the number of guesses the user makes
    # throughout teh game and tell the user at the end.

    @staticmethod
    def Cows_And_Bulls(self):
        pool = SomeOtherExcersices.string.digits
        secret_num = ''.join(random.choice(pool) for _ in range(4))
        # print(secret_num)
        while True:
            # print(secret_num)
            guess = input("guess the random number")
            if guess == "exit":
                break
            elif guess == secret_num:
                print("you win, number was guessed")
            else:
                counter_i = 0
                counter_j = 0
                cow = 0
                bull = 0
                for i in guess:
                    for j in secret_num:
                        if i == j and counter_i == counter_j:
                            cow += 1
                        elif i == j and counter_i != counter_j:
                            bull += 1
                        else:
                            pass
                        counter_j += 1
                    counter_i += 1

            print(f"cows: {cow}, bulls: {bull}")

        pass

    # Decode a Web Page Two
    # Exercise 19 (and Solution)
    # Using the requests and BeautifulSoup Python libraries, print to the screen the full text of the article on
    # this website: http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture.
    # The article is long, so it is split up between 4 pages. Your task is to print out the text to the screen
    # so that you can read the full article without having to click any buttons.
    # (Hint: The post here describes in detail how to use the BeautifulSoup and requests libraries through the
    # solution of the exercise posted here.)
    # This will just print the full text of the article to the screen. It will not make it easy to read, so next
    # exercise we will learn how to write this text to a .txt file.
    # net solution, doesnt run
    @staticmethod
    def Decode_A_Web_Page_Two(my_url='http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture'):
        from pprint import pprint
        from urllib.request import urlopen as uReq
        from bs4 import BeautifulSoup as soup

        uClient = uReq(my_url)
        page_html = uClient.read()
        uClient.close()

        page_soup = soup(page_html, "html.parser")

        main_header = page_soup.body.div.article.div.header.div.div.h1.text

        # text_container = page_soup.findAll("div",{"class": "grid--item body body__container article__body grid-layout__content"})
        text_container = page_soup.findAll("p")
        print(main_header)

        for element in text_container:
            for text in element:
                pprint(text.text)

    # Exercise 20 "Element Search "
    # Write a function that takes an ordered list of numbers (a list where the elements are in order
    # from smallest to largest) and another number. The function decides whether or not the given number is inside
    # the list and returns (then prints) an appropriate boolean.
    #
    # Extras:
    #
    # Use binary search.

    def Element_Search(listA):
        num = random.randint(1, 10)
        print(num)
        listA.sort()
        print(listA)
        return num in listA


# are numbers that can’t be divided by any other number. And yes, happy numbers are a real thing in mathematics - you
# can look it up on Wikipedia. The explanation is easier with an example, which I will describe below.)

# print(Element_Search(Create_Random_List(10,1,10)))


# File Overlap Exercise 23 (and Solution) Given two .txt files that have lists of numbers in them, find the numbers
# that are overlapping. One .txt file has a list of all prime numbers under 1000, and the other .txt file has a list
# of happy numbers up to 1000.

import csv

with open('one.txt', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)


# (If you forgot, prime numbers are numbers that can’t be divided by any other number. And yes, happy numbers are a
# real thing in mathematics - you can look it up on Wikipedia. The explanation is easier with an example,
# which I will describe below.)


class CodingBat_warmups:
    # Given a string, return a new string where "not " has been added to the front. However, if the string already
    # begins with "not", return the string unchanged.

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

    # Given a non-empty string and an int n, return a new string where the char at index n has been removed. The
    # value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1
    # inclusive).
    #
    #
    # missing_char('kitten', 1) → 'ktten'
    # missing_char('kitten', 0) → 'itten'
    # missing_char('kitten', 4) → 'kittn

    def missing_char(str, n):
        obj = str[n]
        return str.remove(obj)

    def missing_char(str, n):
        obj = str[n]
        Nstr = ""
        for elemento in str:
            if elemento == obj:
                pass
            else:
                Nstr += elemento
        return Nstr

    # Given a string, return a new string where the first and last chars have been exchanged.
    #
    #
    # front_back('code') → 'eodc'
    # front_back('a') → 'a'
    # front_back('ab') → 'ba'

    def front_back(str):
        new = ""
        if len(str) == 1:
            return str
        else:
            word = list(str)
            primera = str[0]
            ultima = str[-1]
            word[0] = ultima
            word[-1] = primera
            for _ in word:
                new += _
        return new

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

    # We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling. We are in
    # trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.

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

    # Given a string, return the count of the number of times that a substring length 2 appears in the string and
    # also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).

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
    # "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both
    # strings.

    def string_match(a, b):
        shorter = min(a, b)
        i = 1
        counter = 0
        match = []
        for char_a in a:

            if i < len(a):
                sector_a = char_a + a[i]
                if sector_a not in match:
                    if sector_a in b:
                        match.append(sector_a)
                        counter += 1
            i += 1
        return counter

    # solution in internet:
    # def string_match(a, b):
    #
    #   shorter = min(len(a), len(b))
    #   count = 0
    #
    #
    #   for i in range(shorter-1):
    #     a_sub = a[i:i+2]
    #     b_sub = b[i:i+2]
    #     if a_sub == b_sub:
    #       count = count + 1
    #
    #   return count

    # print(CodingBat.string_match('xxcaazz', 'xxbaaz'))  # → 3
    # print(CodingBat.string_match('abc', 'abc'))  # → 2
    # print(CodingBat.string_match('abc', 'axc'))  # → 0
    # print(CodingBat.string_match('aabbccdd', 'abbbxxd'))  # → 2
    # print(CodingBat.string_match('aaxxaaxx', 'iaxxai'))  # → 3

    # Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".

    def hello_name(name):
        return f'Hello {name}!'

    # hello_name('Bob') → 'Hello Bob!'
    # hello_name('Alice') → 'Hello Alice!'
    # hello_name('X') → 'Hello X!'

    # Given two strings, a and b, return the result of putting them together in the order abba, e.g. "Hi" and "Bye"
    # returns "HiByeByeHi".

    def make_abba(a, b):
        return a + b + b + a

    # make_abba('Hi', 'Bye') → 'HiByeByeHi'
    # make_abba('Yo', 'Alice') → 'YoAliceAliceYo'
    # make_abba('What', 'Up') → 'WhatUpUpWhat'

    # The web is built with HTML strings like "<i>Yay</i>" which draws Yay as italic text. In this example,
    # the "i" tag makes <i> and </i> which surround the word "Yay". Given tag and word strings, create the HTML
    # string with tags around the word, e.g. "<i>Yay</i>".

    def make_tags(tag, word):
        return f'<{tag}>{word}</{tag}>'

    # make_tags('i', 'Yay') → '<i>Yay</i>'
    # make_tags('i', 'Hello') → '<i>Hello</i>'
    # make_tags('cite', 'Yay') → '<cite>Yay</cite>'

    # Given an "out" string length 4, such as "<<>>", and a word, return a new string where the word is in the middle
    # of the out string, e.g. "<<word>>

    def make_out_word(out, word):
        return out[:len(out) // 2] + word + out[len(out) // 2:]

    # CodingBat.make_out_word('<<>>', 'Yay')# → '<<Yay>>'
    # make_out_word('<<>>', 'WooHoo') → '<<WooHoo>>'
    # make_out_word('[[]]', 'word') → '[[word]]'

    # Given a string, return a new string made of 3 copies of the last 2 chars of the original string. The string
    # length will be at least 2

    def extra_end(str):
        return str[-2:] * 3

    # extra_end('Hello') → 'lololo'
    # extra_end('ab') → 'ababab'
    # extra_end('Hi') → 'HiHiHi'

    # Given a string, return the string made of its first two chars, so the String "Hello" yields "He". If the string
    # is shorter than length 2, return whatever there is, so "X" yields "X", and the empty string "" yields the empty
    # string "".

    def first_two(str):
        return str[:2]

    # first_two('Hello') → 'He'
    # first_two('abcdefg') → 'ab'
    # first_two('ab') → 'ab

    # Given a string of even length, return the first half. So the string "WooHoo" yields "Woo"

    def first_half(str):
        return str[:len(str) // 2]

    # first_half('WooHoo') → 'Woo'
    # first_half('HelloThere') → 'Hello'
    # first_half('abcdef') → 'abc'

    # Given a string, return a version without the first and last char, so "Hello" yields "ell". The string length
    # will be at least 2.

    def without_end(str):
        return str[1:-1]

    # without_end('Hello') → 'ell'
    # without_end('java') → 'av'
    # without_end('coding') → 'odin'

    # Given 2 strings, a and b, return a string of the form short+long+short, with the shorter string on the outside
    # and the longer string on the inside. The strings will not be the same length, but they may be empty (length 0).

    def combo_string(a, b):
        return min(a, b, key=len) + max(a, b, key=len) + min(a, b, key=len)

    # combo_string('Hello', 'hi') → 'hiHellohi'
    # combo_string('hi', 'Hello') → 'hiHellohi'
    # combo_string('aaa', 'b') → 'baaab'

    # Given 2 strings, return their concatenation, except omit the first char of each. The strings will be at least
    # length 1.

    def non_start(a, b):
        return a[1:] + b[1:]

    # non_start('Hello', 'There') → 'ellohere'
    # non_start('java', 'code') → 'avaode'
    # non_start('shotl', 'java') → 'hotlava

    # Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end. The string
    # length will be at least 2

    def left2(str):
        if len(str) > 2:
            return str[2:] + str[:2]
        else:
            return str

    # CodingBat.left2('Hello')  # → 'lloHe'
    # CodingBat.left2('java')  # → 'vaja'
    # CodingBat.left2('Hi')  # → 'Hi'
    # CodingBat.left2('cat')  # → 'tca'
    # CodingBat.left2('Chocolate')  # → 'ocolateCh'
    # CodingBat.left2('bricks')  # → 'icksbr'


class CodingBat_List1:
    # Given an array of ints, return True if 6 appears as either the first or last element in the array. The array
    # will be length 1 or more.

    def first_last6(nums):
        return nums[0] == 6 or nums[-1] == 6

    # first_last6([1, 2, 6]) → True
    # first_last6([6, 1, 2, 3]) → True
    # first_last6([13, 6, 1, 2, 3]) → False

    # Given an array of ints, return True if the array is length 1 or more, and the first element and the last
    # element are equal.
    def same_first_last(nums):
        if len(nums) > 1:
            return nums[0] == nums[-1]
        elif len(nums) == 1:
            return True
        else:
            return False

    # print(CodingBat_List1.same_first_last([1, 2, 3]))# → False
    # print(CodingBat_List1.same_first_last([1, 2, 3, 1]))# → True
    # print(CodingBat_List1.same_first_last([1, 2, 1]))# → True

    # Return an int array length 3 containing the first 3 digits of pi, {3, 1, 4}.
    def make_pi(self):
        return [3, 1, 4]

    # make_pi()# → [3, 1, 4]

    # Given 2 arrays of ints, a and b, return True if they have the same first element or they have the same last
    # element. Both arrays will be length 1 or more

    def common_end(a, b):
        return a[0] == b[0] or a[-1] == b[-1]

    # common_end([1, 2, 3], [7, 3]) → True
    # common_end([1, 2, 3], [7, 3, 2]) → False
    # common_end([1, 2, 3], [1, 3]) → True

    # Given an array of ints length 3, return the sum of all the elements.
    def sum3(nums):
        result = 0
        for _ in nums:
            result += _
        return result

    # sum3([1, 2, 3]) → 6
    # sum3([5, 11, 2]) → 18
    # sum3([7, 0, 0]) → 7

    # Given an array of ints length 3, return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.

    def rotate_left3(nums):
        hold = nums.pop(0)
        nums.append(hold)
        return nums

    # print(CodingBat_List1.rotate_left3([1, 2, 3]))# → [2, 3, 1]
    # print(CodingBat_List1.rotate_left3([5, 11, 9]))# → [11, 9, 5]
    # print(CodingBat_List1.rotate_left3([7, 0, 0]))# → [0, 0, 7]

    # Given an array of ints length 3, return a new array with the elements in reverse order, so {1, 2, 3} becomes {
    # 3, 2, 1}.

    def reverse3(nums):
        holdfirst = nums.pop(0)
        holdlast = nums.pop(-1)
        nums.append(holdfirst)
        nums.insert(0, holdlast)
        return nums

    # print(CodingBat_List1.reverse3([1, 2, 3]))  # → [3, 2, 1]
    # print(CodingBat_List1.reverse3([5, 11, 9]))# → [9, 11, 5]
    # reverse3([7, 0, 0]) → [0, 0, 7]

    # Given an array of ints length 3, figure out which is larger, the first or last element in the array,
    # and set all the other elements to be that value. Return the changed array.

    def max_end3(nums):
        index = 0
        while index < len(nums):
            nums[index] = max(nums[0], nums[-1])
            index += 1
        return nums

    # print(CodingBat_List1.max_end3([1, 2, 3]))  # → [3, 3, 3]
    # print(CodingBat_List1.max_end3([11, 5, 9]))  # → [11, 11, 11]
    # print(CodingBat_List1.max_end3([2, 11, 3]))  # → [3, 3, 3]

    # Given an array of ints, return the sum of the first 2 elements in the array. If the array length is less than 2,
    # just sum up the elements that exist, returning 0 if the array is length 0.

    def sum2(nums):
        if len(nums) > 1:
            return nums[0] + nums[1]
        elif len(nums) == 1:
            return nums[0]
        else:
            return 0

    # print(CodingBat_List1.sum2([1, 2, 3]))# → 3
    # print(CodingBat_List1.sum2([1, 1]))# → 2
    # print(CodingBat_List1.sum2([1, 1, 1, 1]))# → 2

    # Given 2 int arrays, a and b, each length 3, return a new array length 2 containing their middle elements.

    def middle_way(a, b):
        mid_list = [a[1], b[1]]
        return mid_list

    # middle_way([1, 2, 3], [4, 5, 6]) → [2, 5]
    # middle_way([7, 7, 7], [3, 8, 0]) → [7, 8]
    # middle_way([5, 2, 9], [1, 4, 5]) → [2, 4]

    # Given an array of ints, return a new array length 2 containing the first and last elements from the original
    # array. The original array will be length 1 or more.

    def make_ends(nums):
        end_list = [nums[0], nums[-1]]
        return end_list

    # make_ends([1, 2, 3]) → [1, 3]
    # make_ends([1, 2, 3, 4]) → [1, 4]
    # make_ends([7, 4, 6, 2]) → [7, 2]

    # Given an int array length 2, return True if it contains a 2 or a 3.

    def has23(nums):
        return 2 in nums or 3 in nums

    # print(CodingBat_List1.has23([2, 5]))# → True
    # print(CodingBat_List1.has23([4, 3]))# → True
    # print(CodingBat_List1.has23([4, 5]))# → False


class CodingBat_Logic1:

    # When squirrels get together for a party, they like to have cigars. a squirrel party is successful when the number
    # of cigars is between 40 and 60, inclusive. Unless it is the weekend, in which case there is no upper bound on the
    # number of cigars. Return True if the party with the given values is successful, or False otherwise.

    def cigar_party(cigars, is_weekend):
        if not is_weekend:
            if 60 >= cigars >= 40:
                return True
        elif is_weekend and cigars >= 40:
            return True
        return False

    # cigar_party(30, False) → False
    # cigar_party(50, False) → True
    # cigar_party(70, True) → True

    # You and your date are trying to get a table at a restaurant. The parameter "you" is the stylishness of your
    # clothes, in the range 0..10, and "date" is the stylishness of your date's clothes. The result getting the table is
    # encoded as an int value with 0=no, 1=maybe, 2=yes. If either of you is very stylish, 8 or more, then the result is
    # 2 (yes). With the exception that if either of you has style of 2 or less, then the result is 0 (no). Otherwise the
    # result is 1 (maybe).

    def date_fashion(you, date):
        if you <= 2 or date <= 2:
            return 0
        elif you >= 8 or date >= 8:
            return 2
        return 1

    # date_fashion(5, 10) → 2
    # date_fashion(5, 2) → 0
    # date_fashion(5, 5) → 1

    # The squirrels in Palo Alto spend most of the day playing. In particular, they play if the temperature is
    # between 60 and 90 (inclusive). Unless it is summer, then the upper limit is 100 instead of 90. Given an int
    # temperature and a boolean is_summer, return True if the squirrels play and False otherwise.

    def squirrel_play(temp, is_summer):
        if is_summer:
            if 60 <= temp <= 100:
                return True
        elif not is_summer:
            if 60 <= temp <= 90:
                return True
        return False

    # squirrel_play(70, False) → True
    # squirrel_play(95, False) → False
    # squirrel_play(95, True) → True

    # You are driving a little too fast, and a police officer stops you. Write code to compute the result, encoded as an
    # int value: 0=no ticket, 1=small ticket, 2=big ticket. If speed is 60 or less, the result is 0. If speed is
    # between 61 and 80 inclusive, the result is 1. If speed is 81 or more, the result is 2. Unless it is your
    # birthday -- on that day, your speed can be 5 higher in all cases.

    def caught_speeding(speed, is_birthday):
        if is_birthday:
            if speed > 86:
                return 2
            elif 65 < speed <= 86:
                return 1
            return 0
        else:
            if speed >= 81:
                return 2
            elif 80 >= speed >= 61:
                return 1
        return 0

    # caught_speeding(60, False) → 0
    # caught_speeding(65, False) → 1
    # caught_speeding(65, True) → 0

    # Given 2 ints, a and b, return their sum. However, sums in the range 10..19 inclusive, are forbidden,
    # so in that case just return 20.

    def sorta_sum(a, b):
        if 19 >= a + b >= 10:
            return 20
        return a + b

    # sorta_sum(3, 4) → 7
    # sorta_sum(9, 4) → 20
    # sorta_sum(10, 11) → 21

    # Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and a boolean indicating if we are on
    # vacation, return a string of the form "7:00" indicating when the alarm clock should ring. Weekdays,
    # the alarm should be "7:00" and on the weekend it should be "10:00". Unless we are on vacation -- then on
    # weekdays it should be "10:00" and weekends it should be "off".

    def alarm_clock(day, vacation):
        if vacation:
            if day == 0 or day == 6:
                return "off"
            return "10:00"
        else:
            if day == 0 or day == 6:
                return "10:00"
            return "7:00"

    # alarm_clock(1, False) → '7:00'
    # alarm_clock(5, False) → '7:00'
    # alarm_clock(0, False) → '10:00

    # The number 6 is a truly great number. Given two int values, a and b, return True if either one is 6. Or if
    # their sum or difference is 6. Note: the function abs(num) computes the absolute value of a number.

    def love6(a, b):
        if a == 6 == b:
            return True
        elif abs(a + b) == abs(a - b) == 6:
            return True
        return False

    # love6(6, 4) → True
    # love6(4, 5) → False
    # love6(1, 5) → True

    # Given a number n, return True if n is in the range 1..10, inclusive. Unless outside_mode is True, in which case
    # return True if the number is less or equal to 1, or greater or equal to 10.

    def in1to10(n, outside_mode):
        if outside_mode:
            if n <= 1 or n >= 10:
                return True
            return False
        else:
            if 1 <= n <= 10:
                return True
            return False

    # in1to10(5, False) → True
    # in1to10(11, False) → False
    # in1to10(11, True) → True
