# PEP 8 -- Style Guide for Python Code
# https://peps.python.org/pep-0008/
# Indentation
# Use 4 spaces per indentation level.
# Continuation lines should align wrapped elements vertically using Python's implicit line joining inside parentheses, brackets and braces, or using a hanging indent. When using a hanging indent the following should be considered; there should be no arguments on the first line and further indentation should be used to clearly distinguish itself as a continuation line.
# Maximum Line Length
# Limit all lines to a maximum of 79 characters.
# For flowing long blocks of text with fewer structural restrictions (docstrings or comments), the line length should be limited to 72 characters.
# Blank Lines
# Surround top-level function and class definitions with two blank lines.
# Method definitions inside a class are surrounded by a single blank line.
# Extra blank lines may be used (sparingly) to separate groups of related functions. Blank lines may be omitted between a bunch of related one-liners (e.g. a set of dummy implementations).
# Use blank lines in functions, sparingly, to indicate logical sections.
# Imports
# Imports should usually be on separate lines, e.g.:
# Yes: import os
#      import sys
# No:  import sys, os
# It's okay to say this though: from subprocess import Popen, PIPE
# Imports are always put at the top of the file, just after any module comments and docstrings, and before module globals and constants.
# Imports should be grouped in the following order:
# standard library imports
# related third party imports
# local application/library specific imports
# You should put a blank line between each group of imports.
# String Quotes
# In Python, single-quoted strings and double-quoted strings are the same. This PEP does not make a recommendation for this. Pick a rule and stick to it. When a string contains single or double quote characters, however, use the other one to avoid backslashes in the string. It improves readability.
# Whitespace in Expressions and Statements
# Avoid extraneous whitespace in the following situations:
# Immediately inside parentheses, brackets or braces.
# Yes: spam(ham[1], {eggs: 2})
# No:  spam( ham[ 1 ], { eggs: 2 } )