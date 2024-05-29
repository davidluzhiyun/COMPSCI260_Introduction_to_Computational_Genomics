COMPSCI 260 - Problem Set 7, Problem 3
Due: Fri 9 Dec 2022, 5pm

Name: David Lu
NetID: zl303

Statement of collaboration and resources used (put None if you worked
entirely without collaboration or resources; otherwise cite carefully): 
https://www.genome.gov/genetics-glossary/histone
My solutions and comments for this problem are below.
-----------------------------------------------------
Plan:
a)
Assume each point has the same probability p to be read. Length of gaps then follow geometric distribution and have
expected value 1/p and variance (1-p)/(p^2). Setting a desirable percentile, one can use the central limit theorem to
estimate the upper and lower bound of the gap length.

Apply:
c)
Report:
-----------------------------------------------------
30 pair(s) have neither read found in contigs, therefore from another project:
seq2
seq7
seq37
seq49
seq62
seq90
seq103
seq133
seq134
seq182
seq183
seq195
seq199
seq206
seq208
seq215
seq220
seq235
seq255
seq271
seq272
seq277
seq303
seq306
seq310
seq324
seq397
seq407
seq413
seq421

25 pair(s) have at least one read in some contig, but we can't find both reads in one contig:
seq14
seq27
seq45
seq63
seq74
seq76
seq82
seq97
seq124
seq129
seq137
seq154
seq161
seq174
seq177
seq222
seq223
seq253
seq286
seq290
seq291
seq295
seq381
seq384
seq392

0 pair(s) have both reads in the same contig, but the outer distance (inclusive) isn't 2000+-10:

366 viable pair(s)
-----------------------------------------------------

d)
Report:
-----------------------------------------------------
2 supercontigs:
contig4, contig2
contig1, contig3
-----------------------------------------------------

e)
Report:
-----------------------------------------------------
Read name   Gap size range   Lower bound   Upper bound
------------------------------------------------------
seq14       86+-10           76            96
seq27       87+-10           77            97
seq63       86+-10           76            96
seq74       87+-10           77            97
seq129      84+-10           74            94
seq137      83+-10           73            93
seq177      85+-10           75            95
seq253      86+-10           76            96
seq286      85+-10           75            95
seq291      85+-10           75            95
-----------------------------------------------------

f)
All the gap ranges need to be satisfied at the same time, therefore:
Gap has lower bound 77 and upper bound 93
gap range = 85 +- 8

g)
Because I do not know if the sequence I am submitting begins with which state. If GENSCAN HMM can only start at N, it
won't give valid results if my sequence is already at the middle of some gene when it begins

Reflect:
i)
First line gives the time the scan is run. Then the report gives some overall info about the sequence being scanned
Then the report shows it uses the HumanIso.smat parameter matrix.
After that it reports the predicted genes/exons it found and the suboptimal ones with probability higher that I set.
Finally, it reports the peptide sequences that can be translated.

j)
k = 4. 11 exons were predicted.

k)
It is typical because GENSCAN didn't report any one as suboptimal

l)
The result for the one in contig1 and the first one in contig3 is believable because they are from Homo sapiens. The
other two are not because they are from mouse or rat.
The last two in contig3 are full proteins. The first in contig3 and the one in contig1 are fragments.
The two fragments are both on crick strand and near the beginning of the original sequence and might therefore be cut
off near the end.

m)
They match some type of histone. Histones provide structural support for chromosomes.