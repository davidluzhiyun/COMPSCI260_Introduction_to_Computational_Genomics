COMPSCI 260 - Problem Set 7, Problem 2
Due: Fri 9 Dec 2022, 5pm

Name: David Lu
NetID: zl303

Statement of collaboration and resources used (put None if you worked
entirely without collaboration or resources; otherwise cite carefully): 
None
My solutions and comments for this problem are below.
-----------------------------------------------------
Apply:
b)
-----------------------------------------------------
Done reading sequence of length  1664970
First 10 segments:
"W", 1-13558
"S", 13558-13666
"W", 13667-31085
"S", 31086-31119
"W", 31120-33376
"S", 33377-33408
"W", 33409-33652
"S", 33653-33681
"W", 33682-37429
"S", 37430-37465

Last 10 segments:
"S", 1622882-1622974
"W", 1622975-1626992
"S", 1626993-1627035
"W", 1627036-1627040
"S", 1627041-1627042
"W", 1627043-1636999
"S", 1637000-1637052
"W", 1637053-1659451
"S", 1659452-1659520
"W", 1659521-1664970

The number of segments that exist in each state:
key: W, number: 184
key: S, number: 183
-----------------------------------------------------
c) I detected 183  structural RNA. The relationship between the two is similar to that of viterbi.
Not all structural RNA regions I detect are among the known tRNA genes. Most of the known tRNA genes match some
regions I detect. For the matching regions, the known tRNA genes are slightly shorter on both ends. These matches
usually appear far away from the ends of the strand.

d) Viterbi seems more effective because it produces less false positives.
It is likely due to the fact that viterbi generates the most likely sequence of hidden states rather that a sequence
of most likely states, making it more suitable for capturing structures.

