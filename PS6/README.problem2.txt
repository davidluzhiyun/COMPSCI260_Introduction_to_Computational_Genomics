COMPSCI 260 - Problem Set 6, Problem 2
Due: Wed 23 November 2022, 5pm

Name: David Lu
NetID: zl303

Statement of collaboration and resources used (put None if you worked
entirely without collaboration or resources; otherwise cite carefully): 
https://www.geeksforgeeks.org/how-to-get-weighted-random-choice-in-python/
https://www.geeksforgeeks.org/python-get-dictionary-keys-as-a-list/
My solutions and comments for this problem are below.
-----------------------------------------------------
Reflect:
f) The results for both groups of artificial texts improve significantly as the
order increases from 1 to 4. As the order increases, it is also easier to tell
which source text the artificial text is generated from since more complete words
start appearing.

g)
1) With a word-based model, the program will no longer generate nonsense words.
It will also be easier for the model to capture things like grammar patterns and
make the sentences more readable.
2) There are far more different words than characters. This could lead to a larger
space and time usage. Also, there are fewer number of words in a text than characters,
which means we need a longer source text to generate believable probabilities.

h)
The output would contain periods. The periods will always be followed by a space. For
lower orders, the period might randomly appear after letters or syllables commonly seen
at the end of words and cut words short. As the order grows, the period will appear after
words commonly seen at the end of a sentence.