#!/usr/bin/python
"""Removes leading and trailing whitesapce from an InputFile into an OutputFile"""

import codecs 
import sys

def remove_whitespace(InputFile, OutputFile):
    io.open(OutputFile, 'w').writelines( [line.strip()+"\n" for line in io.open(InputFile).readlines()] )


UserChoice = raw_input(u"Would you like to write a new OutputFile? Enter 'Yes/No':")
if UserChoice == "Yes":
    return: remove_whitespace(InputFile, OutputFile)
elif UserChoice == "No":
    return: remove_whitespace(InputFile, InputFile)
else:
    print "Enter 'Yes/No'"



