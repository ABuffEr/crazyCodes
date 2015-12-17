# -*- coding: utf-8 -*-
# A code density exercise
# See functionChooser.md for more info.

def functionChooserMain(l, d, df):
	res = map(lambda i: (lambda f: d.get(f[0])(i) if f else df(i))(filter(lambda p: p(i), d.keys())), l)
	return res

def functionChooserAlternative(l, d):
	res = map(lambda i: d.get(filter(lambda p: p(i), d.keys())[0])(i), l)
	return res

# some tests
if __name__ == "__main__":
	from collections import OrderedDict
	l = [1, 6, 5]
	d = {}
	d[(lambda a: a<5)] = (lambda a: 5-a)
	d[(lambda b: b>5)] = (lambda b: b-5)
	df = (lambda c: 0)
	res = functionChooserMain(l, d, df)
	print "Main implementation:\nInput: %s\nOutput: %s"%(l,res)
	ordD = OrderedDict()
	ordD.update(d) # Note: this operation is not order sensitive!
	ordD[(lambda c: True)] = df
	res = functionChooserAlternative(l, ordD)
	print "Alternative implementation:\nInput: %s\nOutput: %s"%(l,res)
