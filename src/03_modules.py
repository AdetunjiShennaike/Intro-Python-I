"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE
for arg in sys.argv:
  print(arg)

# Print out the OS platform you're using:
# YOUR CODE HERE
version = sys.platform
print(version)

# Print out the version of Python you're using:
# YOUR CODE HERE
pv = sys.winver
print(pv)


import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE
uid = os.getpid()
print(uid)

# Print the current working directory (cwd):
# YOUR CODE HERE
cwd = os.getcwd()
print(cwd)

# Print out your machine's login name
# YOUR CODE HERE
lin = os.getlogin()
print(lin)
