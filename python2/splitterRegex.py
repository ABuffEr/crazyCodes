# -*- coding: utf-8 -*-
# A Python proof of concepts about splitting with a regex.
# See splitterRegex.md for more info.
import re

def splitterRegex(input, subExp):
	ourMagic = r'(?:{subExp})|(.*?)(?={subExp})|(.+)(?!{subExp})'
	exp = re.compile(ourMagic.format(subExp=subExp))
	validGroups = []
	for match in exp.finditer(input):
		for group in match.groups():
			# we want only non-None groups
			if group:
				validGroups.append(group)
	return validGroups

# some tests
if __name__ == "__main__":
	from collections import OrderedDict
	# a examples dict with (subExp,input) as (key,value) pairs
	d = OrderedDict()
	# at start, at end, char
	d["a"] = "abba"
	# middle, single, char
	d["b"] = "abcabcabcd"
	# middle, double, char
	d["c"] = "accbccd"
	# middle, single word
	d["singleword"] = "Oh, poor singleword, dead in our experiments..."
	# middle, repeated word (without spaces)
	d["doubleword"] = "I mean doubleworddoubleword, obviously."
	# 3-digits regex, with a postal tracking code
	d[r"\d{3}"] = "KZ717632487IT"
	for (subExp,input) in d.items():
		print "Input: %s"%input
		print "SubExp: %s"%subExp
		res = splitterRegex(input, subExp)
		print "List of results: %s"%res
