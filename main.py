import latex
import solves

def get_Kramer(coef_matrix: list[list[float]], value_matrix: list[float]):
   kram = solves.Kramer(coef_matrix, value_matrix)
   pattern = r"""
   Определим матрицу коэффициентов системы, и матрицу значений системы. \\
   \begin{math}
   A = [MAT_A] \\
   B = [MAT_B] \\
   \end{math}
   Тогда необходимые определители: \\
   \begin{math}
   \Delta = [D] = [D_s] = [D_v] \\
   \Delta_{1} = [D1] = [D1_s] = [D1_v] \\
   \Delta_{2} = [D2] = [D2_s] = [D2_v] \\
   \Delta_{3} = [D3] = [D3_s] = [D3_v] \\
   \end{math}
   Тогда $x_1$, $x_2$ и $x_3$ равны \\
   \begin{math}
   x_1 = \displaystyle \frac{\Delta_1}}{\Delta} = \frac{[D1_v]}{[D_v]} = [x1] \\
   x_2 = \displaystyle \frac{\Delta_2}}{\Delta} = \frac{[D2_v]}{[D_v]} = [x2] \\
   x_3 = \displaystyle \frac{\Delta_3}{\Delta} = \frac{[D3_v]}{[D_v]} = [x3] \\
   \end{math}
   Ответ: ([x1], [x2], [x3])
   """

   d = str(solves.Determinant(kram.det_matrix()).get_value())
   d1 = str(solves.Determinant(kram.det_matrix(1)).get_value())
   d2 = str(solves.Determinant(kram.det_matrix(2)).get_value())
   d3 = str(solves.Determinant(kram.det_matrix(3)).get_value())
   x1 = str(float(d1) / float(d))
   x2 = str(float(d2) / float(d))
   x3 = str(float(d3) / float(d))

   result = pattern.\
      replace("[MAT_A]", latex.matrix(kram.a)).\
      replace("[MAT_B]", latex.matrix(kram.b)).\
      replace("[D]", latex.det(solves.Determinant(kram.det_matrix()))).\
      replace("[D1]", latex.det(solves.Determinant(kram.det_matrix(1)))).\
      replace("[D2]", latex.det(solves.Determinant(kram.det_matrix(2)))).\
      replace("[D3]", latex.det(solves.Determinant(kram.det_matrix(3)))).\
      replace("[D_s]", solves.Determinant(kram.det_matrix()).solve_3x3()).\
      replace("[D1_s]", solves.Determinant(kram.det_matrix(1)).solve_3x3()).\
      replace("[D2_s]", solves.Determinant(kram.det_matrix(2)).solve_3x3()).\
      replace("[D3_s]", solves.Determinant(kram.det_matrix(3)).solve_3x3()).\
      replace("[D_v]", d).\
      replace("[D1_v]", d1).\
      replace("[D2_v]", d2).\
      replace("[D3_v]", d3).\
      replace("[x1]", x1).\
      replace("[x2]", x2).\
      replace("[x3]", x3)

   result = result.replace(".0", "").replace("*", r" \cdot ")

   return result


M_a = [
   [0, 0, -2],
   [3, -1, -1],
   [7, -2, 3]
]
M_b = [-4, -2, 7]

# M_a = [
#    [3, -1, -3],
#    [7, -5, -6],
#    [2, -4, -1]
# ]
#
# M_b = [-5, -15, -8]


with open("result.txt", 'w', encoding='utf-8') as f:
   f.write(get_Kramer(M_a, M_b))


import numpy as np


