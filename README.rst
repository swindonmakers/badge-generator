Automatic Badge Making Thing
============================

Script to automatically make name badges, the background is set by `logo.pdf`.

Usage
-----

..code_block:: bash

  # pipe the output from calling the script with some names to a file
  python3 create_latex.py Alice Bob Charlie > badges.tex

  # build the file with pdflatex
  pdflatex badges