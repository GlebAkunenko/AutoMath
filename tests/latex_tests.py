from unittest import TestCase
import latex
import solves


class LatexTests(TestCase):

   def test_matrix(self):
      matrix = [
         [1, 2, 3],
         ['a', 'b', 'c']
      ]

      actual = latex.matrix(matrix).strip()
      expected = r"""
\begin{pmatrix}
1 & 2 & 3\\
a & b & c
\end{pmatrix}
""".strip()

      self.assertEqual(expected, actual)

   def test_matrix_vec(self):
      matrix = [1, 2, 3]
      actual = latex.matrix(matrix).strip()
      expected = r"""
\begin{pmatrix}
1 \\ 2 \\ 3
\end{pmatrix}
""".strip()

      self.assertEqual(expected, actual)

   def test_det1(self):
      matrix = [
         [1, 2, 3],
         ['a', 'b', 'c']
      ]

      actual = latex.det(matrix).strip()
      expected = r"""
\begin{vmatrix}
1 & 2 & 3\\
a & b & c
\end{vmatrix}
""".strip()

      self.assertEqual(expected, actual)

   def test_det2(self):
      matrix = [
         [1, 2, 3],
         ['a', 'b', 'c'],
         [5, 6, 7]
      ]
      det = solves.Determinant(matrix)

      actual = latex.det(det).strip()
      expected = r"""
\begin{vmatrix}
1 & 2 & 3\\
a & b & c\\
5 & 6 & 7
\end{vmatrix}
""".strip()

      self.assertEqual(expected, actual)