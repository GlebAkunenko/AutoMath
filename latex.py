import solves

def matrix(m: list[list] | list):
   pattern = r"""
\begin{pmatrix}
[BODY]
\end{pmatrix}
   """
   body = ""

   if isinstance(m[0], list):
      for line in m[:-1]:
         body += " & ".join(list(map(str, line))) + r"\\" + "\n"
      body += " & ".join(list(map(str, m[-1])))
   else:
      body += r" \\ ".join(list(map(str, m)))
   return pattern.replace("[BODY]", body)


def det(m: list[list] | solves.Determinant):
   if isinstance(m, solves.Determinant):
      m = m.matrix
   pattern = r"""
\begin{vmatrix}
[BODY]
\end{vmatrix}
   """
   body = ""
   for line in m[:-1]:
      body += " & ".join(list(map(str, line))) + r"\\" + "\n"
   body += " & ".join(list(map(str, m[-1])))
   return pattern.replace("[BODY]", body)




