import sys
import importlib
from types import ModuleType

if __name__ == "__main__":
	# backup current modules status
	bakModules = {}
	bakModules.update(sys.modules)
	# import the module wrapper (where __getattr__ is defined)
	wrapperMod = importlib.import_module("wrapperMod")
	# save its initial status for later reset
	originalGlobals = {}
	originalGlobals.update(vars(wrapperMod))
	# having to change sys.modules, save its keys in a list
	modules = [m for m in sys.modules.keys()]
	for module in modules:
		# create a new instance of an empty module
		newMod = ModuleType(module)
		# set in wrapper the module to wrap
		# originalGlobals restores at initial status, forgetting the previous wrapping
		wrapperMod.setWrappedModule(module, originalGlobals)
		# turn newMod into the wrapped module
		newMod.__dict__.update(vars(wrapperMod))
		# divert module to newMod
		sys.modules[module] = newMod
	# now, import a module
	# that believes to import os, sys, etc...
	import divertedMod
	# demonstrate it uses wrapped os
	divertedMod.askOsFoo()
	divertedMod.askOsChdir()
	divertedMod.askSysFoo()
	# restore initial modules
	sys.modules.update(bakModules)
	# check the original os
	import os
	try:
		os.foo
	except AttributeError:
		print("os has no attribute foo, and this is correct!")
