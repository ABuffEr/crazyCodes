# A compact form of (fast) modular exponentiation
import sys

fme = lambda b,e,m: reduce(lambda d,i: (d**2*b**int(i))%m, bin(e)[2:], 1)

if __name__ == "__main__":
	if len(sys.argv) < 4:
		print '3 args required'
	else:
		base, exp, mod = [int(x) for x in sys.argv[1:]]
		res = fme(base, exp, mod)
		print res
