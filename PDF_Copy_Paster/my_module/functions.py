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

# global flag to enable termination of script
f = True

def run():
    """Gets user input for optional script features (appending quotes
    or carriage return) before running the script itself. 
    """
    q = input("Append quotes to selected text? (y=yes): ")
    e = input("Append carriage return to selected text? (y=yes): ")
    # Runs the infinite while loop component of the script using the
    # values of q and e specified by the user above
    pdfcp(q,e)
    
def quotes(q):
    """Allows user to specify if they want pdfcp() to automatically add quotes
       to both sides of copied pdf text in addition to removing line breaks 
       while pdfcp() is running.
       
       Parameters
       ----------
       q : str ("y" or "")
           Quote append option user input specifying which message to print.
            
       Returns
       -------
       "Quotes WILL be appended" : str
           Message returned if q set to "y" by user.
       "Quotes WON'T be appended" : str
           Message returned if q set to anything other than "y" by user.
    """
    # Notifies user if quotes will or won't be appended to copied text
    if q is "y":
        print("Quotes WILL be appended")
        return "Quotes WILL be appended"
    else:
        print("Quotes WON'T be appended")
        return "Quotes WON'T be appended"
        
def enter(e):
    """Allows user to specify if they want pdfcp() to automatically append a
       carriage return to the end of copied pdf text in addition to removing 
       line breaks while pdfcp() is running.
       
       Parameters
       ----------
       e : str ("y" or "")
           Carriage return append user input specifying which message to print.
            
       Returns
       -------
       "A carriage return WILL be appended" : str
           Message returned if e set to "y" by user.
       "A carriage return WON'T be appended" : str
           Message returned if e set to anything other than "y" by user.
    """
    # Resets global "f" variable value to True each time options is run
    # so pdfcp() function can restart and continue running post-termination
    global f
    f = True
    # Notifies user if carriage return will or won't be appended to copied text
    if e is "y":
        print("A carriage return WILL be appended")
        return "A carriage return WILL be appended"
    else:
        print("A carriage return WON'T be appended")
        return "A carriage return WON'T be appended"

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

def compare(pdftxt, pdfnew):
    """Returns copied pdf text before and after pdfcp() modifications.
    
       Parameters
       ----------
       pdftxt : str
           Initial unmodified text string copied from pdf.
       pdfnew : str
           New text string modified by pdfcp() and ready to be pasted.
       
       Returns
       -------
       "old: " + pdftxt + " "+ "new: " + pdfnew : str
           Output string comparing copied pdf text before and after modification
    """
    return("old: " + pdftxt + " "+ "new: " + pdfnew)
    
def pdfcp(q, e):
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
       
       Parameters
       ----------
       q : str ("y" or "")
           Quote append user input specifying whether or not
           to append quotes to newly copied pdf text.
       e : str ("y" or "")
           Carriage return append user input specifying whether or not
           to append a carriage return to newly copied pdf text.
    """
    # Allows user to specify optional copied text operations after 
    # main line break removal operation is run
    quotes(q)
    enter(e)
    # Starts termination function thread to run continuously while
    # pdfcp() monitors and updates clipboard contents
    threading.Thread(target=terminate).start()
    # Empty string value which is updated and copied to clipboard with 
    # newly modified text initially copied from a pdf
    pdfnew = ""
    # pdfcp() runs unless termination function sets "f" to False
    while f:
        # Gets current windows clipboard contents
        pdftxt = clipboard.paste()
        # Only modifies NEW clipboard contents to avoid
        # modifying copied text twice
        if pdftxt != pdfnew:
            # Removes line breaks via the replace string method
            pdfnew = pdftxt.replace("\r\n"," ")
            # Updates clipboard with modified text
            clipboard.copy(pdfnew)
        # Only runs if user selected to enclose text in quotes    
        if pdftxt != pdfnew and q is "y":
            # Adds quotation mark to both ends of copied pdf text
            pdfnew=f'"{pdfnew}"'
            clipboard.copy(pdfnew)
        # Only runs if user selected to append carriage return to text
        if pdftxt != pdfnew and e is "y":
            # Adds two carriage returns to end of copied text to
            # create a new line in word document ready to paste in
            # next modified segment of pdf text avoiding the need
            # for user to manually press return each time they paste text.
            pdfnew = (pdfnew + '\r\n\r\n')
            clipboard.copy(pdfnew)
        # Runs compare() after each while loop iteration to act as a 
        # proxy return comparing pre and post modified copied pdf text
        compare(pdftxt, pdfnew)
        # Allows pdfcp() function to rest for 1 sec before running again
        # to increase overall script stability and save cpu and memory resources
        time.sleep(1)

def autopdfcp(q, e):
    """A testable version of pdfcp that terminates automatically after 
       10 seconds used for testing purposes only. Unlike pdfcp(), this 
       function doesn't start a terminate() thread.
       
       Parameters
       ----------
       q : str ("y" or "")
           Quote append user input specifying whether or not
           to append quotes to newly copied pdf text.
       e : str ("y" or "")
           Carriage return append user input specifying whether or not
           to append a carriage return to newly copied pdf text.
    """
    global f
    f = True
    # Empty string value which is updated and copied to clipboard with 
    # newly modified text initially copied from a pdf
    pdfnew = ""
    # pdfcp() runs unless termination function sets "f" to False
    while f:
        # Gets current windows clipboard contents
        pdftxt = clipboard.paste()
        # Only modifies NEW clipboard contents to avoid
        # modifying copied text twice
        if pdftxt != pdfnew:
            # Removes line breaks via the replace string method
            pdfnew = pdftxt.replace("\r\n"," ")
            # Updates clipboard with modified text
            clipboard.copy(pdfnew)
        # Only runs if user selected to enclose text in quotes    
        if pdftxt != pdfnew and q is "y":
            # Adds quotation mark to both ends of copied pdf text
            pdfnew=f'"{pdfnew}"'
            clipboard.copy(pdfnew)
        # Only runs if user selected to append carriage return to text
        if pdftxt != pdfnew and e is "y":
            # Adds two carriage returns to end of copied text to
            # create a new line in word document ready to paste in
            # next modified segment of pdf text avoiding the need
            # for user to manually press return each time they paste text.
            pdfnew = (pdfnew + '\r\n\r\n')
            clipboard.copy(pdfnew)
        print("running...")
        # Allows pdfcp() function to rest for 1 sec before running again
        # to increase overall script stability and save cpu and memory resources
        time.sleep(1)
        f = False