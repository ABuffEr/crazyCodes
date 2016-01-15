# Padding with regex #

## THE PROBLEM: ##

It was born from a working case of my friend and colleague [Dennis Boanini,][1] and can be formulated as:

is possible to pad a string using regex? And, more specifically, can we do it avoiding a different pattern for each sub-length of a fixed length?

## THE SOLUTION: ##

It seems that a way using a single pattern and a standard replacing operation doesn't exist; so, the only way seems to work to replacing side, using a quite generic pattern to filter cases and a function that pads and returns the fixed-length string.

In our example, we use:

* an input file containing various, non-fixed-length Italian mail postcode, usually of 5 digits, but reported here also with 2, 3 or 4 digits (that is, without leading zeros);
* an output file, identical to the input file, but with fixed-length postcodes;
* a pattern to totally match (with "^...$") string containing from 2 to 4 digits;
* a function replacing passed string with a number of zeros according to string length, plus the same string.

You can arrange these elements in various ways, of course, doing a grouping in pattern, taking a specific group or joining all groups in replacing function, not only for padding, and so on... but this is the basic scheme.

And now... [Python code.](paddingRegex.py)


[1]: https://bitbucket.org/DennisB/