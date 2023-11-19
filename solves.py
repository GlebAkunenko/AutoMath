import utils


class Determinant:
   def __init__(self, matrix: list[list[float]]):
      if len(matrix) != len(matrix[0]):
         raise Exception("Determinant class supports only square matrix")
      self.n = len(matrix)
      # WARING: Indexing from 1!!!!
      self.a = [0.] + [m[0] for m in matrix]
      self.b = [0.] + [m[1] for m in matrix]
      self.c = [0.] + [m[2] for m in matrix] if self.n > 2 else None
      self.d = [0.] + [m[3] for m in matrix] if self.n > 3 else None
      self.matrix = matrix

   def solve_2x2(self) -> str:
      a = self.a[1]
      b = self.b[1]
      c = self.a[2]
      d = self.b[2]
      return f"{a} * {b} + {c} * {d}".replace(" ", "")

   def solve_3x3(self) -> str:
      a = [f"({x})" if x < 0 else str(x) for x in self.a]
      b = [f"({x})" if x < 0 else str(x) for x in self.b]
      c = [f"({x})" if x < 0 else str(x) for x in self.c]
      return f"{a[1]}*{b[2]}*{c[3]} + {a[3]}*{b[1]}*{c[2]} + {a[2]}*{b[3]}*{c[1]}" \
             f" - {a[3]}*{b[2]}*{c[1]} - {a[1]}*{b[3]}*{c[2]} - {a[2]}*{b[1]}*{c[3]}".replace(" ", "")



class Kramer:
   def __init__(self, coef_matrix: list[list[float]], value_matrix: list[list[float]]):
      self.a = coef_matrix
      self.b = value_matrix

   def det_matrix(self, number: int) -> list[list[float]]:
      if number == 0:
         return self.a
      return utils.replace_column(self.a, number, self.b)


