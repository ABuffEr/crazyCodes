# Crazy Codes

A collection of brief codes, quite useless or unlikely applicable, to solve in a shorter or involved manner some relatively simple problems.

Problems that, for majority of cases, come from my friend and colleague [Emmanuel Schoysman][1], and which he uses to torture me for days and days. 😄

Ok, there could be serious things too... but it's not guaranteed. 😛

## Python module redirection

Is there a way to make a module-in-the-middle attack? To run a filter between a module importer and  a module imported from it? To intercept and alert about deprecations?

A first experiment (lacking of the class patching part) around [PEP 562.][3] [Wrapper](moduleWrapping/multipleModules/wrapperMod.py?raw=true), [diverted](moduleWrapping/multipleModules/divertedMod.py?raw=true) and [main](moduleWrapping/multipleModules/mainMod.py?raw=true) modules.

(for a single module redirection, see the repo tree under moduleWrapping/singleModule)

## Python module customs

What's imported? What's used from this import?

A experiment to discover it statically, using [ast][2]: [code](customsStaticAnalyzer.py?raw=true)

(manually run by command-line with your .py as argument, i.e.: "py -3.7 customsStaticAnalyzer.py your.py")

## Old (Python 2)

### Splitter Regex

A exercise/challenge to build a (monstrous) regex to split a string, in all possible cases.

[Explanation](python2/splitterRegex.md) and [Python code.](python2/splitterRegex.py?raw=true)

### Function Chooser

A code density exercise, to apply different functions on list items according to satisfied predicates.

[Explanation](python2/functionChooser.md) and [Python code.](python2/functionChooser.py?raw=true)

### Padding Regex

An attempt to use regex for padding; in practice, a replacing example using a function rather than a pre-determined string.

[Explanation](python2/paddingRegex.md) and [Python code.](python2/paddingRegex.py?raw=true)

### Compact Fast Modular Exponentiation

A challenge to minimize the well-known function for modular exponentiation.

[Explanation](python2/compactModExp.md) and [Python code.](python2/compactModExp.py?raw=true)


[1]: https://github.com/eschoysman
[2]: https://docs.python.org/3/library/ast.html
[3]: https://peps.python.org/pep-0562/
