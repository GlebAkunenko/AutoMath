# from unittest import TestCase
# from records import *
#
# class RecordTests(TestCase):
#
#    def test_sum_1_2(self):
#       inp = Sum(1, 2)
#       actual = inp.get_record()
#       expected = "1+2"
#       self.assertEqual(expected, actual)
#
#    def test_sum_m1_2(self):
#       inp = Sum(-1, 2)
#       actual = inp.get_record()
#       expected = "-1+2"
#       self.assertEqual(expected, actual)
#
#    def test_sum_1_m2(self):
#       inp = Sum(1, -2)
#       actual = inp.get_record()
#       expected = "1-2"
#       self.assertEqual(expected, actual)
#
#    def test_sum_m1_m2(self):
#       inp = Sum(-1, -2)
#       actual = inp.get_record()
#       expected = "-1-2"
#       self.assertEqual(expected, actual)
#
#    def test_sum_1_2_3(self):
#       inp = Sum(1, 2, 3)
#       actual = inp.get_record()
#       expected = "1+2+3"
#       self.assertEqual(expected, actual)
#
#    def test_sum_m1_2_m3_4(self):
#       inp = Sum(-1, 2, -3, 4)
#       actual = inp.get_record()
#       expected = "-1+2-3+4"
#       self.assertEqual(expected, actual)
#
