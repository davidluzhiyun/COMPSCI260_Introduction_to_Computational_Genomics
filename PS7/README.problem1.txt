COMPSCI 260 - Problem Set 7, Problem 1
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
Report:
-----------------------------------------------------
Decoding the Viterbi path for bacterial.genome.fasta using HMM.methanococcus.txt
Read a sequence of length 1664970
First 10 segments:
"W", 1-13561
"S", 13562-13666
"W", 13667-31085
"S", 31086-31119
"W", 31120-33652
"S", 33653-33681
"W", 33682-97325
"S", 97326-97541
"W", 97542-97626
"S", 97627-97715

Last 10 segments:
"S", 1410404-1410467
"W", 1410468-1525011
"S", 1525012-1525080
"W", 1525081-1553924
"S", 1553925-1553981
"W", 1553982-1622880
"S", 1622881-1622973
"W", 1622974-1659452
"S", 1659453-1659520
"W", 1659521-1664970

The number of segments that exist in each state:
key: W, number: 68
key: S, number: 67
-----------------------------------------------------

Reflect:
d)
67. Not all structural RNA regions I detect are among the known tRNA genes. Most of the known tRNA genes match some
regions I detect. For the matching regions, the known tRNA genes are slightly shorter on both ends. These matches
usually appear far away from the ends of the strand.