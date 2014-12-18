#!/usr/bin/python
"""Removes leading and trailing whitesapce from an InputFile into an OutputFile"""

import codecs 
import sys
import io

InputFile = sys.argv[1]
OutputFile = sys.argv[2]

def remove_whitespace(InputFile, OutputFile):
    io.open(OutputFile, 'w').writelines( [line.strip()+"\n" for line in io.open(InputFile).readlines()] )


if __name__ == "__main__":

	UserChoice = raw_input(u"Would you like to write a new OutputFile? Enter 'Yes/No':")
	if UserChoice == "Yes":
	    remove_whitespace(InputFile, OutputFile)
	elif UserChoice == "No":
	    remove_whitespace(InputFile, InputFile)
	else:
	    print "Enter 'Yes/No'"



