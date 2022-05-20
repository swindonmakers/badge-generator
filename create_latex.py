import sys

names = sys.argv[1:]

test_names = [
    "Alice",
    "Bob",
    "Charlie",
    "Dave",
    "Ellen",
    "Frank"]

header = r"""
\documentclass[12pt]{article}
\usepackage{graphicx}
\usepackage{multicol}

\begin{document}
%\begin{multicols}{2}
\begin{center}
"""

footer = r"""
\end{center}
%\end{multicols}
\end{document}
"""

def badge_entry(name: str, size: int):
    pic = r"\includegraphics[width=%imm, height=%imm]{logo.pdf}"%(size, size)
    label = r"\vspace{%gmm}\textbf{\textsf{\Huge %s}}"%(-size/2-3.5, name)
    space = r"\vspace{%imm}"%size
    return "\n".join(["", pic, "", label, "", space, ""])

print(header)
for name in names:
    print(badge_entry(name, 38))
print(footer)

