#!/usr/bin/env python
# coding: utf-8


"""Tests for my functions.
"""

from functions import*

def test_run():
    assert callable(run)
    """
    Test funtion for run function.
    """

def test_quotes():
    """
    Test funtion for quotes function.
    """
    assert callable(quotes)
    assert isinstance(quotes("y"), str)
    assert quotes("y") == "Quotes WILL be appended"
    assert quotes("") == "Quotes WON'T be appended"

def test_enter():
    """
    Test funtion for enter function.
    """
    assert callable(enter)
    assert isinstance(enter("y"), str)
    assert enter("y") == "A carriage return WILL be appended"
    assert enter("") == "A carriage return WON'T be appended"
    
def test_terminate():
    """
    Test funtion for terminate function.
    """
    assert callable(terminate)
    
def test_compare():
    """
    Test funtion for compare function.
    """
    assert callable(compare)
    assert isinstance(compare("A","B"), str)
    assert compare("A","B") == 'old: A new: B'
    assert compare("A\nB",""""AB"\n\n""") == 'old: A\nB new: "AB"\n\n'

def test_pdfcp():
    """
    Test funtion for pdfcp function.
    """
    assert callable(pdfcp)

def test_autopdfcp():
    """
    Test funtion for autopdfcp function.
    """
    assert callable(autopdfcp)
    # control test for normal behavior when function disabled
    a=clipboard.copy("A\r\nB") 
    b=clipboard.paste()
    assert b == "A\r\nB"
    # tests function with append quotes and carriage return options disabled
    a=clipboard.copy("A\r\nB")
    autopdfcp("", "") 
    b=clipboard.paste()
    assert b == "A B"
    # tests function with append quotes and carriage return options enabled
    a=clipboard.copy("A\r\nB")
    autopdfcp("y", "y") 
    b=clipboard.paste()
    assert b == '"A B"\r\n\r\n'
    # tests function with append quotes enabled and append carriage 
    # return disabled
    a=clipboard.copy("A\r\nB")
    autopdfcp("y", "") 
    b=clipboard.paste()
    assert b == '"A B"'
    # tests function with append quotes disabled and append carriage 
    # return enabled
    a=clipboard.copy("A\r\nB")
    autopdfcp("", "y") 
    b=clipboard.paste()
    assert b == 'A B\r\n\r\n'
    
def test_all():
    """
    Simultaneously test all functions.
    """
    test_run()
    test_quotes()
    test_enter()
    test_terminate()
    test_compare()
    test_pdfcp()
    test_autopdfcp()
