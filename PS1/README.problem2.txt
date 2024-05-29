COMPSCI 260 - Problem Set 1, Problem 2
Due: Fri 16 Sep 2022, 5pm

Name: David Lu
NetID: zl303

Statement of collaboration and resources used (put None if you worked
entirely without collaboration or resources; otherwise cite carefully):
https://stackoverflow.com/questions/43149086/python-3-regex-find-all-overlapping-matches-start-and-end-index-in-a-string

My solutions and comments for this problem are below.
-----------------------------------------------------

Apply1 report:
-----------------------------------------------------
If the minimum ORF length is 10 amino acids, there are 16 ORF(s) with average length 600.25 in amino acids
If the minimum ORF length is 40 amino acids, there are 10 ORF(s) with average length 956.7 in amino acids
If the minimum ORF length is 60 amino acids, there are 10 ORF(s) with average length 956.7 in amino acids
-----------------------------------------------------

Apply1:
c) There are 12 ORFs
ORF10 is at 29558-29674 with length 117 nucleotides
S is at 21563-25384 and there are 1273 amino acids in the translated protein

Reflect1:
d) The larger the minimum ORF length, the less ORFs I identify and the higher the average length
e) The ORFs found in my function matches the genome map wel for the most part. The function captured
everthing except ORF1ab and ORF10. The former wasn't captured because it contains a stop codon within.
The latter wasn't captured because it was shorter than 60 amino acids.
In terms of false capture, since ORF1ab somehow contains ORF1a while being on the same frame (presumably
 some splicing happened), the part in ORF1ab that goes after ORF1a was miss identified as a ORF.