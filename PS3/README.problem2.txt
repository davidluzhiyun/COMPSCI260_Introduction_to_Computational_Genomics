COMPSCI 260 - Problem Set 3, Problem 2
Due: Fri 14 Oct 2022, 5pm

Name: David Lu
NetID: zl303

Statement of collaboration and resources used (put None if you worked
entirely without collaboration or resources; otherwise cite carefully): 
https://stackoverflow.com/questions/26579392/sorting-string-values-according-to-a-custom-alphabet-in-python
https://stackoverflow.com/questions/5213033/sort-a-list-of-lists-with-a-custom-compare-function
https://stackoverflow.com/questions/22490366/how-to-use-cmp-in-python-3
My solutions and comments for this problem are below.
-----------------------------------------------------
Plan:

a)
Rotations :
TCCTGTAG$
CCTGTAG$T
CTGTAG$TC
TGTAG$TCC
GTAG$TCCT
TAG$TCCTG
AG$TCCTGT
G$TCCTGTA
$TCCTGTAG

Sorted:
$TCCTGTAG
AG$TCCTGT
CCTGTAG$T
CTGTAG$TC
G$TCCTGTA
GTAG$TCCT
TAG$TCCTG
TCCTGTAG$
TGTAG$TCC

Taking the last column:
GTTCATG$C

b)
sorted:
$AACCGTT

append1:
GTCA$ATC
$AACCGTT

sort1:
$AACCGTT
CCGAT$AT

append2:
GTCA$ATC
$AACCGTT
CCGAT$AT

sort2:
$AACCGTT
CCGAT$AT
TA$GTCCA

append3:
GTCA$ATC
$AACCGTT
CCGAT$AT
TA$GTCCA

sort3:
$AACCGTT
CCGAT$AT
TA$GTCCA
TGC$ATAC

append4:
GTCA$ATC
$AACCGTT
CCGAT$AT
TA$GTCCA
TGC$ATAC

sort4:
$AACCGTT
CCGAT$AT
TA$GTCCA
TGC$ATAC
A$TCCTGA

append5:
GTCA$ATC
$AACCGTT
CCGAT$AT
TA$GTCCA
TGC$ATAC
A$TCCTGA

sort5:
$AACCGTT
CCGAT$AT
TA$GTCCA
TGC$ATAC
A$TCCTGA
CCTTAA$G

append6:
GTCA$ATC
$AACCGTT
CCGAT$AT
TA$GTCCA
TGC$ATAC
A$TCCTGA
CCTTAA$G

sort6:
$AACCGTT
CCGAT$AT
TA$GTCCA
TGC$ATAC
A$TCCTGA
CCTTAA$G
ATATGCC$

append7:
GTCA$ATC
$AACCGTT
CCGAT$AT
TA$GTCCA
TGC$ATAC
A$TCCTGA
CCTTAA$G
ATATGCC$

sort7:
$AACCGTT
CCGAT$AT
TA$GTCCA
TGC$ATAC
A$TCCTGA
CCTTAS$G
ATATGCC$
GTCA$ATC

Take the first column:
$CTTACAG

Apply:

d) report:
-----------------------------------------------------
BWT: CGGACTAACGGACTAACGGACTAACGGACTAC$ -> CTTTTAAAGGGGA$AAAAAAAGGGGCCCCCCCC
-----------------------------------------------------

e) report:
-----------------------------------------------------
Four score and seven years ago our fathers brought forth, on
this continent, a new nation, conceived in liberty, and dedicated
to the proposition that all men are created equal. Now we are
engaged in a great civil war, testing whether that nation, or
any nation so conceived, and so dedicated, can long endure.
We are met on a great battle-field of that war. We have come
to dedicate a portion of that field, as a final resting-place
for those who here gave their lives, that that nation might
live. It is altogether fitting and proper that we should do
this. But, in a larger sense, we cannot dedicate, we cannot
consecrate—we cannot hallow—this ground. The brave men, living
and dead, who struggled here, have consecrated it far above
our poor power to add or detract. The world will little note,
nor long remember what we say here, but it can never forget
what they did here. It is for us the living, rather, to be dedicated
here to the unfinished work which they who fought here have
thus far so nobly advanced. It is rather for us to be here dedicated
to the great task remaining before us—that from these honored
dead we take increased devotion to that cause for which they
here gave the last full measure of devotion—that we here highly
resolve that these dead shall not have died in vain—that this
nation, under God, shall have a new birth of freedom, and that
government of the people, by the people, for the people, shall
not perish from the earth. --Abraham Lincoln
-----------------------------------------------------