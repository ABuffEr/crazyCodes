def setWrappedModule(modName):
	global internalModule
	import importlib
	internalModule = importlib.import_module(modName)
	# backup current __getattr__ in
	# case wrapped module has defined one
	originalGetattr = __getattr__
	# get own globals from internalModule ones
	globals().update(vars(internalModule))
	# consider again this __getattr__
	globals()["__getattr__"] = originalGetattr

def __getattr__(name):
	# demonstrate wrapping magic
	if name == "foo":
		return "bar!"
	else:
		# for deprecations not finalized yet
		return getattr(internalModule, f"deprecated_{name}")

def __dir__():
	return internalModule.__dir__()
