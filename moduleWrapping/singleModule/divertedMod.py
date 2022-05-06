import os
import sys

def askOsFoo():
	res = os.foo
	print("Asked foo, received %s from module %s"%(res, os.__name__))

def askOsChdir():
	res = os.chdir
	print("Asked chdir, received %s from module %s"%(res, os.__name__))

def askSysFoo():
	res = sys.foo
	print("Asked foo, received %s from module %s"%(res, sys.__name__))
