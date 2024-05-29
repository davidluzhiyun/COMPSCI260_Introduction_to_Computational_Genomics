COMPSCI 260 - Problem Set 4, Problem 4
Due: Fri 28 Oct 2022, 5pm

Name: David Lu
NetID: zl303

Statement of collaboration and resources used (put None if you worked
entirely without collaboration or resources; otherwise cite carefully): 
https://www.uniprot.org/
My solutions and comments for this problem are below.
-----------------------------------------------------

Apply:
b)
Report:
-----------------------------------------------------
Sequence 1:  P63015
Sequence 2:  O18381
Optimal Alignment Score:  644
Number of Locations:  4
Locations
136 in Seq1 and 188 in Seq2
137 in Seq1 and 189 in Seq2
138 in Seq1 and 190 in Seq2
139 in Seq1 and 191 in Seq2
One optimal case:
In Seq1:
5 - 136
In Seq2:
57 - 188
P63015: HSGVNQLGGVFVNGRPLPDSTRQKIVELAHSGARPCDISRILQVSNGCVSKILGRYYETG (5-64)
O18381: HSGVNQLGGVFVGGRPLPDSTRQKIVELAHSGARPCDISRILQVSNGCVSKILGRYYETG (57-116)

P63015: SIRPRAIGGSKPRVATPEVVSKIAQYKRECPSIFAWEIRDRLLSEGVCTNDNIPSVSSIN (65-124)
O18381: SIRPRAIGGSKPRVATAEVVSKISQYKRECPSIFAWEIRDRLLQENVCTNDNIPSVSSIN (117-176)

P63015: RVLRNLASEKQQ                                                 (125-136)
O18381: RVLRNLAAQKEQ                                                 (177-188)
-----------------------------------------------------
Reflect:
c)
P63015 is paired box protein Pax-6 from mice. O18381 is paired box protein Pax-6
from fruit flies. The two share some common regions. Both are involved in the
development eyes. In this case, the local alignment contains the DNA-binding
region essential to their shared function. It also contains the PAI subdomain
and RED subdomain common to the proteins
d)
Score of optimal alignment of any suffix of i-prefix of x with any suffix of j-prefix
of Y. It's max value is the score of an optimal local alignment.