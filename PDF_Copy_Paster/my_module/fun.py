#!/usr/bin/env python
# coding: utf-8

# In[ ]:

# All modules imported that the below functions depend on 
import time
import sys
import os
# Allows direct monitoring and updating of windows cipboard contents
import clipboard
# Allows termination function to be initialized as a thread to run 
# continuously while pdfcp() function runs
import threading

# Global variables defined to be used by each of the functions below
f = ""
quotes = input("Append quotes to selected text? (y=yes): ")
enter = input("Append carriage return to selected text? (y=yes): ")

def after(quotes, enter):
    return str(input_string)

def options():
    """Allows user to specify if they want pdfcp() to automatically add quotes
       to both sides of copied pdf text and/or append a carriage return at the 
       end of copied pdf text in addition to removing line breaks while pdfcp() 
       is running.
    """
    # Variables are set as global to use between functions
    global quotes
    global enter
    global f
    # Allows user to select if they want quotes added to copied text
    if quotes is "y":
        print("Quotes WILL be appended")
    else:
        print("Quotes WON'T be appended")
    # Allows user to select if carriage return is added to copied text
    if enter is "y":
        print("A carriage return WILL be appended")
    else:
        print("A carriage return WON'T be appended")
    # Resets global "f" variable value to True each time options is run
    # so pdfcp() function can restart and continue running post-termination
    f = True

def terminate():
    """Allows user to terminate pdfcp at any time simply by pressing <enter>.
        
       MODIFIED CODE DISCLAIMER AND ATTRIBUTION:
       The terminate() function is modified from the code specified in
       reference 4 of the "References" section in the "Final project PDF 
       copy paster.ipynb" notebook. However, the organization and functionality
       of terminate() was significantly updated (refactoring the code, and/or 
       updating functionality more than just updating naming, style and 
       documentation) and SHOULD BE CONSIDERED PART OF MY GRADED PROJECT CODE.
    """
    global f
    print("running...")
    input('Press <enter> to terminate: ')
    # Function continues to run until user presses <enter>.
    # After <enter> is pressed, global variable "f" value
    # is set to False, terminating pdfcp()
    f = False
    print('pdfcp has terminated')

def pdfcp():
    """Continously monitors for clipboard contents copied from pdf and updates 
       clipboard with the same text without line breaks and, if desired by user
       with quotes and/or a carriage return automatically appended.
       
       MODIFIED CODE DISCLAIMER AND ATTRIBUTION:
       The pdfcp() function is modified from the code specified in
       reference 2 of the "References" section in the "Final project PDF 
       copy paster.ipynb" notebook. However, the organization and functionality
       of pdfcp() was significantly updated (refactoring the code, and/or 
       updating functionality more than just updating naming, style and 
       documentation) and SHOULD BE CONSIDERED PART OF MY GRADED PROJECT CODE.
    """
    # Allows user to specify optional copied text operations after 
    # main line break removal operation is run
    options()
    global quotes
    global enter
    # Starts termination function thread to run continuously while
    # pdfcp() monitors and updates clipboard contents
    threading.Thread(target=terminate).start()
    # Empty string that is updated then copied to clipboard with 
    # edited text initially copied from a pdf
    pdfnew = ""
    # pdfcp() runs unless termination function sets "f" to False
    while f:
        # Gets current windows clipboard contents
        pdftxt = clipboard.paste()
        # Only modifies new clipboard contents to avoid
        # modifying the same copied text twice
        if pdftxt != pdfnew:
            # Removes line breaks via the replace string method
            pdfnew = pdftxt.replace("\r\n"," ")
            # Updates clipboard with modified text
            clipboard.copy(pdfnew)
        # Only runs if user selected to enclose text in quotes    
        if pdftxt != pdfnew and quotes is "y":
            # Adds quotation mark to both ends of copied pdf text
            pdfnew=f'"{pdfnew}"'
            clipboard.copy(pdfnew)
        # Only runs if user selected to append carriage return to text
        if pdftxt != pdfnew and enter is "y":
            # Adds two carriage returns to end of copied text to
            # create a new line in word document ready to paste in
            # next modified segment of pdf text avoiding the need
            # for user to manually press return each time they paste text.
            pdfnew = (pdfnew + '\r\n\r\n')
            clipboard.copy(pdfnew)
        # Allows pdfcp() function to rest for 500ms before running again
        # to increase overall script stability and save cpu and memory resources
        time.sleep(0.5)

