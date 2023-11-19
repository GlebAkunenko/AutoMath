from unittest import TestCase
from solves import Determinant

class DeterminateTests(TestCase):

   def test_init_2x2(self):
      inp = [
         [1, 2],
         [3, 4]
      ]

      det = Determinant(inp)
      actual_a = det.a
      actual_b = det.b
      actual_c = det.c
      actual_d = det.d

      expected_a = [0, 1, 3]
      expected_b = [0, 2, 4]
      expected_c = None
      expected_d = None

      self.assertEqual(expected_a, actual_a)
      self.assertEqual(expected_b, actual_b)
      self.assertEqual(expected_c, actual_c)
      self.assertEqual(expected_d, actual_d)

   def test_init_4x4(self):
      inp = [
         [1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10, 11, 12],
         [13, 14, 15, 16],
      ]

      det = Determinant(inp)
      actual_a = det.a
      actual_b = det.b
      actual_c = det.c
      actual_d = det.d

      expected_a = [0, 1, 5, 9, 13]
      expected_b = [0, 2, 6, 10, 14]
      expected_c = [0, 3, 7, 11, 15]
      expected_d = [0, 4, 8, 12, 16]

      self.assertEqual(expected_a, actual_a)
      self.assertEqual(expected_b, actual_b)
      self.assertEqual(expected_c, actual_c)
      self.assertEqual(expected_d, actual_d)


   def test_solve_2x2(self):
      M = [
         [11, -3],
         [-15, -2]
      ]
      D = Determinant(M)
      actual = D.solve_2x2()
      expected = "11*(-2)-(-15)*(-3)"
      self.assertEqual(expected, actual)

   def test_solve_3x3(self):
      M = [
         [1, -2, 3],
         [4, 0, 6],
         [-7, 8, 9]
      ]
      D = Determinant(M)
      actual = D.solve_3x3()
      expected = "1*0*9+(-7)*(-2)*6+4*8*3-(-7)*0*3-1*8*6-4*(-2)*9"
      self.assertEqual(expected, actual)