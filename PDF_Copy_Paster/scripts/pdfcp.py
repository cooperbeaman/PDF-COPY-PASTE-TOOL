#!/usr/bin/env python
# coding: utf-8

# In[3]:

"""Script runs pdf copy paste tool through command prompt.
   Automatically monitors and updates clipboard contents.
"""

# Allows importing functions from functions.py in my_module folder
import sys
sys.path.append('../')
# Imports functions from my_module folder 
from my_module.functions import *

# Runs windows clipboard monitoring and updating function "pdfcp"
# to remove line breaks from copied pdf text and optionally enclose
# copied pdf text in quotes or append a carriage return to the end of it
pdfcp()


