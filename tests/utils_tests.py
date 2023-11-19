from unittest import TestCase
import utils

class UtilsTests(TestCase):

   def test_replace_column_1(self):
      inp1 = [
         [1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]
      ]
      inp1_bak = inp1.copy()
      inp2 = [-1, -2, -3]

      actual = utils.replace_column(inp1, 1, inp2)
      expected = [
         [-1, 2, 3],
         [-2, 5, 6],
         [-3, 8, 9]
      ]

      self.assertEqual(expected, actual)
      self.assertEqual(inp1, inp1_bak)

   def test_replace_column_2(self):
      inp1 = [
         [1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]
      ]
      inp1_bak = inp1.copy()
      inp2 = [-1, -2, -3]

      actual = utils.replace_column(inp1, 2, inp2)
      expected = [
         [1, -1, 3],
         [4, -2, 6],
         [7, -3, 9]
      ]

      self.assertEqual(expected, actual)
      self.assertEqual(inp1, inp1_bak)

   def test_replace_column_3(self):
      inp1 = [
         [1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]
      ]
      inp1_bak = inp1.copy()
      inp2 = [-1, -2, -3]

      actual = utils.replace_column(inp1, 3, inp2)
      expected = [
         [1, 2, -1],
         [4, 5, -2],
         [7, 8, -3]
      ]

      self.assertEqual(expected, actual)
      self.assertEqual(inp1, inp1_bak)