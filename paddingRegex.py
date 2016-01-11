# -*- coding: utf-8 -*-
import re

def main(inFile, outFile, pattern, pLen, pChar):
	exp = re.compile(pattern)
	# x will be a _sre.SRE_Match instance
	repF = (lambda x: pChar*(pLen-len(x.string))+x.string)
	with open(inFile, "r") as f1, open(outFile, "w") as f2:
		for line in f1:
			# strip() to avoid useless blank lines
			line = line.strip()
			newLine = exp.sub(repF, line) if exp.match(line) else line
			f2.write(newLine+"\n")

# a simple test
if __name__ == "__main__":
	# input file
	inFile = "cap.csv"
	# output file
	outFile = "paddedCap.csv"
	# regex pattern
	pattern = r"^[0-9]{2,4}$"
	# string length after padding
	pLen = 5
	# char to add for padding
	pChar = "0"
	main(inFile, outFile, pattern, pLen, pChar)
