def setWrappedModule(modName, originalGlobals):
	# clean globals from previous setting
	globals().clear()
	# restore initial status
	globals().update(originalGlobals)
	# backup current __getattr__ in
	# case wrapped module has defined one
	originalGetattr = __getattr__
	global internalModule
	import importlib
	internalModule = importlib.import_module(modName)
	# get own globals from internalModule ones
	globals().update(vars(internalModule))
	# consider again __getattr__ defined here
	globals()["__getattr__"] = originalGetattr

def __getattr__(name):
	# demonstrate wrapping magic
	if name == "foo":
		return "bar!"
	else:
		# project case example: useful if deprecated_ method is defined in internalModule
		# or exists a map between deprecations and new guidelines, before they are finalized
		from warnings import warn
		warn(f"{name} is deprecated, use {newMethod} instead", DeprecationWarning)
		return getattr(internalModule, f"deprecated_{name}")

def __dir__():
	return internalModule.__dir__()
