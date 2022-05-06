# Fast ok, but less verbose? #

## THE PROBLEM: ##

Well, in this case it's not a problem, only a challenge.

Given the usual, verbose form of fast modular exponentiation algorithm, with binary exponent in left-to-right order (see [Wikipedia][1] for details):

    def fme(base, exp, mod):
    	d = 1
    	for i in bin(exp)[2:]: # [2:] to exclude the trailing "0b"
    		d = (d*d)%mod
    		if i == '1':
    			d = (d*base)%mod
    	return d

we can reduce it in various ways, but our goal is to obtain a lambda (inline) function that accepts arguments, so to have:

    fme = our_fme_lambda
    res = fme(base, exp, mod)

## THE SOLUTION: ##

Well, briefly... [Python code.](compactModExp.py)


[1]: https://en.wikipedia.org/wiki/Modular_exponentiation