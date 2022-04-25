# -*- coding: UTF-8 -*-
import ast
#import builtins

"""
A module like a customs,
to statically intercept all imported things
(classes, functions, attributes...)
from an external module.
WARNING: experimental, and far from being complete.
"""

DEBUG = False

def dbgPrint(message):
	if DEBUG:
		print(message)

class AddonParser(object):

	# parser and visitor instances
	parser = visitor = None
	# imports dict, in the form import:alias)
	_importDict = dict()
	# calls and attributes set (to avoid duplicates)
	_callTupleSet = set()
	# assignments tuples list, in the form (value, target)
	_assignList = []

	def __init__(self, filepath):
		with open(filepath, "rt") as f:
			self.parser = ast.parse(f.read())
		self.visitor = AddonVisitor()
		self.collectImports()
		self.collectAssignments()
		self.collectCalls()

	def getNodes(self, types=[]):
		nodes = []
		for node in ast.walk(self.parser):
			if not types or type(node) in types:
				nodes.append(node)
		return nodes

	def collectImports(self):
		importObjs = self.getNodes((ast.Import, ast.ImportFrom,))
		for obj in importObjs:
			infos = self.visitor.visit(obj)
			if infos:
				for k, v in infos:
					# populate _importDict with (import chain, alias)
					self._importDict[k] = v

	def collectAssignments(self):
		assignNodes = self.getNodes((ast.Assign,))
		for node in assignNodes:
			infos = self.visitor.visit(node)
			if infos:
				value, target = infos[0]
				originValue = value.split(".")[0]
				module = list(filter(lambda i: i[1] == originValue, self._importDict.items()))
				if not module:
					dbgPrint("Assign value not in imports, skip %s"%value)
					continue
				originModule = module[0][0]
				newValue = '.'.join([originModule, *value.split(".")[1:]])
				infos = (newValue, target)
				self._assignList.append(infos)

	def collectCalls(self):
		callObjs = self.getNodes((ast.Call, ast.Attribute,))
		for obj in callObjs:
			call = self.visitor.visit(obj)
			if call:
				# like self for self.func, or speech for speech.speak
				originCall = call.split(".")[0]
				module = list(filter(lambda i: i[1] == originCall, self._importDict.items()))
				assign = list(filter(lambda i: i[1] == originCall, self._assignList))
				if not module and not assign:
					dbgPrint("Call/attribute not from imports, skip %s"%call)
					continue
				# rebuild non-aliased chain
				if module:
					originModule = module[0][0]
				else:
					originModule = assign[0][0]
				newCall = '.'.join([originModule, *call.split(".")[1:]])
				self._callTupleSet.add(newCall)


class AddonVisitor(ast.NodeVisitor):

	def visit_alias(self, node):
		return (node.name, node.asname if node.asname else node.name)

	def visit_Name(self, node):
		return node.id

	def visit_Import(self, node):
		# names -> list of alias nodes
		infos = []
		for name in node.names:
			infos.append(self.visit(name))
		return infos

	def visit_ImportFrom(self, node):
		# module -> bare string module name
		# names -> list of alias nodes
		# level -> module level (0 means absolute import)
		if node.level > 0:
			# we want only Python/project modules
			return
		infos = []
		module = node.module+"." if node.module else ""
		for name in node.names:
			name, asname = self.visit(name)
			info = (module+name, asname)
			infos.append(info)
		return infos

	def visit_Attribute(self, node):
		# value -> Name node
		# attr -> bare string attribute
		value = self.visit(node.value)
		if not value:
			info = node.attr
		else:
			info = '.'.join([value, node.attr])
		return info

	def visit_Index(self, node):
		# value -> Str, Num... node
		# we suppose only a field, and return as repr (guarantee it's a string)
		index = getattr(node.value, node.value._fields[0])
		info = "["+repr(index)+"]"
		return info

	def visit_Subscript(self, node):
		# value -> Attribute node
		# slice -> Index node
		value = self.visit(node.value)
		index = self.visit(node.slice)
		if index and value:
			info = ''.join([value, index])
		elif index:
			info = index
		elif value:
			info = value
		return info

	def visit_Call(self, node):
		# func -> Name or Attribute node
		info = self.visit(node.func)
		return info

	def visit_Assign(self, node):
		# targets -> list of nodes
		# value -> single node
		if type(node.value) == ast.Call:
			# exclude stuff like
			# res = func()
			return
		value = self.visit(node.value)
		if not value:
			return
		infos = []
		for target in node.targets:
			# fixme: return local stuff to follow chain
			targetInfo = self.visit(target)
			infos.append((value, targetInfo))
		return infos

def main(*args):
	p = AddonParser(*args)
	print("[IMPORTS]")
	for k,v in p._importDict.items():
		print("%s: %s"%(k, v))
	print("[ASSIGNMENTS]")
	for i in p._assignList:
		print(i)
	print("[CALLS/ATTRIBUTES]")
	for i in p._callTupleSet:
		print(i)

if __name__ == "__main__":
	import sys
	args = sys.argv[1:]
	if args:
		main(*args)
	else:
		print("Please specify a .py filepath")
