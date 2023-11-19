def replace_column(matrix: list[list], column_number: int, values: list):
   if len(matrix[0]) != len(values):
      raise Exception("Gotten matrix len must equals value matrix len")

   matrix = matrix.copy()
   n = len(matrix[0])
   for i in range(n):
      matrix[i][column_number - 1] = values[i]

   return matrix