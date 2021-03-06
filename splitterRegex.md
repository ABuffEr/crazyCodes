# One Regex to split them all #

## THE PROBLEM: ##

it was born in Java (the favourite language of my friend), and can be formulated as:

Is inputString.split(regex) too simple? Do you want a stream as output, perhaps enjoying an iterator, and is java.util.regex.Pattern.compile(regex).splitAsStream(inputString) too mainstream?

Voilà...

## THE SOLUTION! ##

Calling "regex" above as "subregex" (for explanation  purpose), the core of our solution is the following combination of three regex (Did I already say regex? Yeah, I love regex! XD):

`(?:subregex)|(.*?)(?=subregex)|(.+)(?!subregex)`

As explained (for example) in [Python documentation for re module][1], the meaning of three disjunctions is:

* for `(?:subregex)`: a non-capturing regex; there is a match of subregex, but the result will not be retrieved (substantially, it's useful to consume inputString of a subregex segment);
* for `(.*?)(?=subregex)`: a match of all text followed by subregex; the non-greedy expression `(.*?)` allows us to match some text correctly even if the text is followed by two occurrences of subregex; subregex is not consumed;
* for `(.+)(?!subregex)`: a match of all text NOT followed by subregex; again, subregex is not consumed.

NOTE: the disjunctions order is important! Specifically, the first expression, in its position, guarantees that no substring of subregex will be matched by the other regex disjunctions (test them separately to see for yourself).

Finally, subregex can be anything, a character, a word, a regex. And yes, it magically works. :D

And now... [Python code.](splitterRegex.py)


[1]: https://docs.python.org/2/library/re.html