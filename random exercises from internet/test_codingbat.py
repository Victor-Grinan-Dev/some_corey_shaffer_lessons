import unittest
from SDA_studies.Autoestudio import solved_internet_exercises


class TestCodingBat(unittest.TestCase):

    def test_not_string(self):
        self.assertEqual(solved_internet_exercises.CodingBat_warmups.not_string('candy'), 'not candy')
        self.assertEqual(solved_internet_exercises.CodingBat_warmups.not_string('x'), 'not x')
        self.assertEqual(solved_internet_exercises.CodingBat_warmups.not_string('not bad'), 'not bad')

    def test_missing_char(self):
        self.assertEqual(solved_internet_exercises.CodingBat_warmups.missing_char('kitten', 1), 'ktten')
        self.assertEqual(solved_internet_exercises.CodingBat_warmups.missing_char('kitten', 0), 'itten')
        self.assertEqual(solved_internet_exercises.CodingBat_warmups.missing_char('kitten', 4), 'kittn')

    def test_front_back(self):
        self.assertEqual(solved_internet_exercises.CodingBat_warmups.front_back('code'), 'eodc')
        self.assertEqual(solved_internet_exercises.CodingBat_warmups.front_back('a'), 'a')
        self.assertEqual(solved_internet_exercises.CodingBat_warmups.front_back('ab'), 'ba')

    def test_front3(self):
        self.assertEqual(solved_internet_exercises.CodingBat_warmups.front3('Java'), 'JavJavJav')
        self.assertEqual(solved_internet_exercises.CodingBat_warmups.front3('Chocolate'), 'ChoChoCho')
        self.assertEqual(solved_internet_exercises.CodingBat_warmups.front3('abc'), 'abcabcabc')

    def test_sum_double(self):
        self.assertEqual(solved_internet_exercises.CodingBat_warmups.sum_double(1, 2), 3)
        self.assertEqual(solved_internet_exercises.CodingBat_warmups.sum_double(3, 2), 5)
        self.assertEqual(solved_internet_exercises.CodingBat_warmups.sum_double(2, 2), 8)

    def test_monkey_trouble(self):
        self.assertTrue(solved_internet_exercises.CodingBat_warmups.monkey_trouble(True, True), True)
        self.assertTrue(solved_internet_exercises.CodingBat_warmups.monkey_trouble(True, True), True)
        self.assertTrue(solved_internet_exercises.CodingBat_warmups.monkey_trouble(True, True), True)

    def test_parrot_trouble(self):
        self.assertTrue(solved_internet_exercises.CodingBat_warmups.parrot_trouble(True, 6), True)
        self.assertTrue(solved_internet_exercises.CodingBat_warmups.parrot_trouble(True, 6), True)
        self.assertTrue(solved_internet_exercises.CodingBat_warmups.parrot_trouble(True, 6), True)

    def test_makes10(self):
        self.assertTrue(solved_internet_exercises.CodingBat_warmups.makes10(9, 10), True)
        self.assertFalse(solved_internet_exercises.CodingBat_warmups.makes10(9, 9), False)
        self.assertTrue(solved_internet_exercises.CodingBat_warmups.makes10(1, 9), True)

    def test_string_times(self):
        self.assertEqual(solved_internet_exercises.CodingBat_warmups.string_times('Hi', 2), 'HiHi')
        self.assertEqual(solved_internet_exercises.CodingBat_warmups.string_times('Hi', 3), 'HiHiHi')
        self.assertEqual(solved_internet_exercises.CodingBat_warmups.string_times('Hi', 1), 'Hi')

    def test_front_time(self):
        self.assertEqual(solved_internet_exercises.CodingBat_warmups.front_times('Chocolate', 2), 'ChoCho')
        self.assertEqual(solved_internet_exercises.CodingBat_warmups.front_times('Chocolate', 3), 'ChoChoCho')
        self.assertEqual(solved_internet_exercises.CodingBat_warmups.front_times('Abc', 3), 'AbcAbcAbc')

    def test_string_bits(self):
        self.assertEqual(solved_internet_exercises.CodingBat_warmups.string_bits('Hello'), 'Hlo')
        self.assertEqual(solved_internet_exercises.CodingBat_warmups.string_bits('Hi'), 'H')
        self.assertEqual(solved_internet_exercises.CodingBat_warmups.string_bits('Heeololeo'), 'Hello')

    def test_string_splosion(self):
        self.assertEqual(solved_internet_exercises.CodingBat_warmups.string_splosion('Code'), 'CCoCodCode')
        self.assertEqual(solved_internet_exercises.CodingBat_warmups.string_splosion('abc'), 'aababc')
        self.assertEqual(solved_internet_exercises.CodingBat_warmups.string_splosion('ab'), 'aab')

    def test_last2(self):
        self.assertEqual(solved_internet_exercises.CodingBat_warmups.last2('hixxhi'), 1)
        self.assertEqual(solved_internet_exercises.CodingBat_warmups.last2('xaxxaxaxx'), 1)
        self.assertEqual(solved_internet_exercises.CodingBat_warmups.last2('axxxaaxx'), 2)

    def test_array_count9(self):
        self.assertEqual(solved_internet_exercises.CodingBat_warmups.array_count9([1, 2, 9]), 1)
        self.assertEqual(solved_internet_exercises.CodingBat_warmups.array_count9([1, 9, 9]), 2)
        self.assertEqual(solved_internet_exercises.CodingBat_warmups.array_count9([1, 9, 9, 3, 9]), 3)

    def test_array_front9(self):
        self.assertTrue(solved_internet_exercises.CodingBat_warmups.array_front9([1, 2, 9, 3, 4]), True)
        self.assertFalse(solved_internet_exercises.CodingBat_warmups.array_front9([1, 2, 3, 4, 9]), False)
        self.assertFalse(solved_internet_exercises.CodingBat_warmups.array_front9([1, 2, 3, 4, 5]), False)

    def test_array123(self):
        self.assertTrue(solved_internet_exercises.CodingBat_warmups.array123([1, 1, 2, 3, 1]), True)
        self.assertFalse(solved_internet_exercises.CodingBat_warmups.array123([1, 1, 2, 4, 1]), False)
        self.assertTrue(solved_internet_exercises.CodingBat_warmups.array123([1, 1, 2, 1, 2, 3]), True)

    def test_string_match(self):
        self.assertEqual(solved_internet_exercises.CodingBat_warmups.string_match('xxcaazz', 'xxbaaz'), 3)
        self.assertEqual(solved_internet_exercises.CodingBat_warmups.string_match('abc', 'abc'), 2)
        self.assertEqual(solved_internet_exercises.CodingBat_warmups.string_match('abc', 'axc'), 0)
        self.assertEqual(solved_internet_exercises.CodingBat_warmups.string_match('aabbccdd', 'abbbxxd'), 2)
        self.assertEqual(solved_internet_exercises.CodingBat_warmups.string_match('aaxxaaxx', 'iaxxai'), 3)

    def test_hello_name(self):
        self.assertEqual(solved_internet_exercises.CodingBat_warmups.hello_name('Bob'), 'Hello Bob!')
        self.assertEqual(solved_internet_exercises.CodingBat_warmups.hello_name('Alice'), 'Hello Alice!')
        self.assertEqual(solved_internet_exercises.CodingBat_warmups.hello_name('X'), 'Hello X!')

    def test_makeabba(self):
        self.assertEqual(solved_internet_exercises.CodingBat_warmups.make_abba('Hi', 'Bye'), 'HiByeByeHi')
        self.assertEqual(solved_internet_exercises.CodingBat_warmups.make_abba('Yo', 'Alice'), 'YoAliceAliceYo')
        self.assertEqual(solved_internet_exercises.CodingBat_warmups.make_abba('What', 'Up'), 'WhatUpUpWhat')

    def test_make_tags(self):
        self.assertEqual(solved_internet_exercises.CodingBat_warmups.make_tags('i', 'Yay'), '<i>Yay</i>')
        self.assertEqual(solved_internet_exercises.CodingBat_warmups.make_tags('i', 'Hello'), '<i>Hello</i>')
        self.assertEqual(solved_internet_exercises.CodingBat_warmups.make_tags('cite', 'Yay'), '<cite>Yay</cite>')

    def test_make_out_word(self):
        self.assertEqual(solved_internet_exercises.CodingBat_warmups.make_out_word('<<>>', 'Yay'), '<<Yay>>')
        self.assertEqual(solved_internet_exercises.CodingBat_warmups.make_out_word('<<>>', 'WooHoo'), '<<WooHoo>>')
        self.assertEqual(solved_internet_exercises.CodingBat_warmups.make_out_word('[[]]', 'word'), '[[word]]')

    def test_left2(self):
        self.assertEqual(solved_internet_exercises.CodingBat_warmups.left2('Hello'), 'lloHe')
        self.assertEqual(solved_internet_exercises.CodingBat_warmups.left2('java'), 'vaja')
        self.assertEqual(solved_internet_exercises.CodingBat_warmups.left2('Hi'), 'Hi')
        self.assertEqual(solved_internet_exercises.CodingBat_warmups.left2('cat'), 'tca')
        self.assertEqual(solved_internet_exercises.CodingBat_warmups.left2('Chocolate'), 'ocolateCh')
        self.assertEqual(solved_internet_exercises.CodingBat_warmups.left2('bricks'), 'icksbr')

class TestCodingBatList(unittest.TestCase):

    def test_first_last6(self):
        self.assertTrue(solved_internet_exercises.CodingBat_List1.first_last6([1, 2, 6]), True)
        self.assertTrue(solved_internet_exercises.CodingBat_List1.first_last6([6, 1, 2, 3]), True)
        self.assertFalse(solved_internet_exercises.CodingBat_List1.first_last6([13, 6, 1, 2, 3]), False)

    def test_same_first_last(self):
        self.assertFalse(solved_internet_exercises.CodingBat_List1.same_first_last([1, 2, 3]), False)
        self.assertTrue(solved_internet_exercises.CodingBat_List1.same_first_last([1, 2, 3, 1]), True)
        self.assertTrue(solved_internet_exercises.CodingBat_List1.same_first_last([1, 2, 1]), True)

    def test_rotate_left3(self):
        self.assertEqual(solved_internet_exercises.CodingBat_List1.rotate_left3([1, 2, 3]), [2, 3, 1])
        self.assertEqual(solved_internet_exercises.CodingBat_List1.rotate_left3([5, 11, 9]), [11, 9, 5])
        self.assertEqual(solved_internet_exercises.CodingBat_List1.rotate_left3([7, 0, 0]), [0, 0, 7])

    def test_date_fashion(self):
        self.assertEqual(solved_internet_exercises.CodingBat_Logic1.date_fashion(5, 10), 2)
        self.assertEqual(solved_internet_exercises.CodingBat_Logic1.date_fashion(5, 2), 0)
        self.assertEqual(solved_internet_exercises.CodingBat_Logic1.date_fashion(5, 5), 1)

    def test_squirrel_play(self):
        self.assertTrue(solved_internet_exercises.CodingBat_Logic1.squirrel_play(70, False), True)
        self.assertFalse(solved_internet_exercises.CodingBat_Logic1.squirrel_play(95, False), False)
        self.assertTrue(solved_internet_exercises.CodingBat_Logic1.squirrel_play(95, True), True)

    def test_caught_speeding(self):
        self.assertEqual(solved_internet_exercises.CodingBat_Logic1.caught_speeding(60, False), 0)
        self.assertEqual(solved_internet_exercises.CodingBat_Logic1.caught_speeding(65, False), 1)
        self.assertEqual(solved_internet_exercises.CodingBat_Logic1.caught_speeding(65, True), 0)


# self.assertTrue(solved_internet_exercises.CodingBat.)
# self.assertEqual(solved_internet_exercises.CodingBat.)

if __name__ == '__main__':
    unittest.main
