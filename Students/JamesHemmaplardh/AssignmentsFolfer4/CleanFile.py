"""Remove leading and trailing whitesapce from an InputFile into an OutputFile"""
#!/usr/bin/python

import codecs 
import sys
import io
import string 

InputFile = sys.argv[1]
OutputFile = sys.argv[2]

def remove_whitespace(InputFile, OutputFile):
    io.open(OutputFile, 'w').writelines( [line.strip()+"\n" for line in io.open(InputFile).readlines()] )

def remove_whitespace_using_map(InputFile, OutputFile):
    input = io.open(InputFile)
    output = map(string.strip, input)
    out = io.open(OutputFile, 'w')
    for line in output:
        out.write(line+"\n")


if __name__ == "__main__":

	UserChoice = raw_input(u"Would you like to write a new OutputFile? Enter 'Yes/No':")
	if UserChoice == "Yes":
	    remove_whitespace(InputFile, OutputFile)
	elif UserChoice == "No":
	    remove_whitespace(InputFile, InputFile)
	else:
	    print "Enter 'Yes/No'"



