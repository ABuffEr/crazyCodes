# Testing a predicate, applying a function #

## THE PROBLEM: ##

We have a series of items (a list, a stream,... according to language), a collection (dictionary, map...) with (predicate, function) pairs, and a default function.

We want to apply a specific function to each series element, depending on what predicate it satisfies; if it satisfies no predicate, then we apply default function.

We want to do it (for pure masochism) in the more compact way, using Python and only map, filter and lambda functions.

## THE SOLUTION: ##

First, some considerations. If we have predicates mutually exclusive, that is, each element satisfies only a predicate, then the dictionary can be a normal dictionary (that not keeps the insertion order). However, if the order is important, a OrderedDict is needed.

In our example, predicates are implemented as lambda functions, such as relative (and default) functions to apply.

That said, if d is the dictionary, df the default function, and l the list to process, the core of our solution is...

`map(lambda i: (lambda f: d.get(f[0])(i) if f else df(i))(filter(lambda p: p(i), d.keys())), l)`

where, in each step:
* `i` becomes a list element;
* `f` becomes a list of predicates (eventually empty);
* `p` becomes a predicate (from dictionary keys);
* `lambda i` executes `lambda f` and returns its result, that `map` will store in output list;
* `lambda f` chooses what function should be applied on `i`, according to `f` (if empty, chooses default function `df`, if not empty then retrieves function associated with first (and unique if mutually exclusive) predicate in list `f`), runs chosen function and returns the result;
* `lambda p` checks predicate `p` on `i`, and, if it holds, `filter` function adds `p` to the returned list (which will be the argument of `lambda f`).


### ALTERNATIVE SOLUTION: ###

In case of OrderedDict, we can even apply a trick, inserting as last the default function in dictionary with a always-true predicate and getting a slightly simpler code.

`map(lambda i: d.get(filter(lambda p: p(i), d.keys())[0])(i), l)`

I hope it will be useful (maybe, perhaps, in a time far, far away...) XD
