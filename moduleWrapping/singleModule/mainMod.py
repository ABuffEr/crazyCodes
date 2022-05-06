import sys
import importlib

if __name__ == "__main__":
	# backup current modules status
	bakModules = {}
	bakModules.update(sys.modules)
	# import module wrapper
	wrapperMod = importlib.import_module("wrapperMod")
	# wrap os (for example)
	wrapperMod.setWrappedModule("os")
	# divert os to wrapper
	sys.modules["os"] = wrapperMod
	# now, import a module
	# that believes to import os
	import divertedMod
	# demonstrate it uses wrapped os
	divertedMod.askOsFoo()
	divertedMod.askOsChdir()
	# restore initial modules
	sys.modules.update(bakModules)
	# check the original os
	import os
	try:
		os.foo
	except AttributeError:
		print("os has no attribute foo, and this is correct!")
