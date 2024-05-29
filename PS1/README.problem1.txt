COMPSCI 260 - Problem Set 1, Problem 1
Due: Fri 16 Sep 2022, 5pm

Name: David Lu
NetID: zl303

Statement of collaboration and resources used (put None if you worked
entirely without collaboration or resources; otherwise cite carefully):

https://www.yeastgenome.org/

My solutions and comments for this problem are below.
-----------------------------------------------------
Plan1:
a) It is used to code a protein involved in mitochondrial function or
organization
b) 741
c) ((741) / 3) - 1 = 246
I would expect the resulting peptide to shorten because introns are cut
out of the gene.

Develop1 report:
-------------------------------------------------------------------
Aim2 gene
Start to end on Aim2 plus minus 1kb(in nucleotides and inclusive): 1001-1741
Length (in amino acids): 246
-------------------------------------------------------------------

Apply1 report:
-------------------------------------------------------------------
Restriction enzyme sites of Aim2 plus minus 1kb
Start and end in nucleotides and inclusive
BamHI:

BstYI:

    Start: 124
    End: 129
    Sequence: AGATCC
    Location: upstream

    Start: 217
    End: 222
    Sequence: AGATCT
    Location: upstream

    Start: 459
    End: 464
    Sequence: AGATCT
    Location: upstream

    Start: 2607
    End: 2612
    Sequence: AGATCT
    Location: downstream

    Start: 2664
    End: 2669
    Sequence: GGATCT
    Location: downstream

SpeI:

SphI:

    Start: 2357
    End: 2362
    Sequence: GCATGC
    Location: downstream

StyI:

    Start: 88
    End: 93
    Sequence: CCAAGG
    Location: upstream

    Start: 1059
    End: 1064
    Sequence: CCAAGG
    Location: within

    Start: 1119
    End: 1124
    Sequence: CCAAGG
    Location: within

SalI:

    Start: 688
    End: 693
    Sequence: GTCGAC
    Location: upstream
-------------------------------------------------------------------
Apply1 Answer:
Upstream: BstYI, StyI, SalI
Downstream: BstYI, SphI
Within: StyI

Reflect1:
g) I might use SalI and SphI because they together cut the upstream and downstream
of the gene without cutting within it. They also cut closer to the gene and produce
 less fragments comparing to BstYI. Last but not least, both of them only recognize
 fixed, palindromic sequences.
I might also use BstYI because it cuts both the upstream and downstream without cutting
within the gene. While it doesn't necessarily cut on palindromic sequences, it is
guaranteed to cut both strands and create sticky ends
I will avoid BamHI and SpeI because they don't cut within Aim2 plus minus 1kb. I will
also avoid StyI because it cut within the gene

Plan2:
h) MCS: Help with the insertion of foreign gene without disrupting the rest of the plasmid.
Ampicillin resistance gene: Help to select the yeasts that have successfully integrated the plasmids.If you
chose to use the cutting site on it, you may conduct further selection combined with the Auxotrophic marker.
Replication origin: Enable the replication of the plasmid and the genes it carries.
Auxotrophic marker: Help to select the yeasts that have successfully integrated the plasmids. If you
chose to use the cutting site on it, you may conduct further selection combined with the Ampicillin resistance gene
i) It might not be true for BstYI and StyI
j) BamHI and BstYI might display such behavior.

Develop2 report:
-------------------------------------------------------------------
PRS304 MCS sites report:
Start and end in nucleotides and inclusive

BamHI:
    Sites within MCS:

        Start: 1923
        End: 1928
        Sequence: GGATCC

        Total site(s) within: 1

    Other sites:
        Upstream: 0
        Downstream: 0
BstYI:
    Sites within MCS:

        Start: 1923
        End: 1928
        Sequence: GGATCC

        Total site(s) within: 1

    Other sites:
        Upstream: 0
        Downstream: 6
SpeI:
    Sites within MCS:

        Start: 1917
        End: 1922
        Sequence: ACTAGT

        Total site(s) within: 1

    Other sites:
        Upstream: 0
        Downstream: 0
SphI:
    Sites within MCS:

        Total site(s) within: 0

    Other sites:
        Upstream: 0
        Downstream: 0
StyI:
    Sites within MCS:

        Total site(s) within: 0

    Other sites:
        Upstream: 0
        Downstream: 0
SalI:
    Sites within MCS:

        Start: 1968
        End: 1973
        Sequence: GTCGAC

        Total site(s) within: 1

    Other sites:
        Upstream: 0
        Downstream: 0
-------------------------------------------------------------------

Plan3:
Use BstYI to cut Aim2 and BamHI to cut pRS304 .
The site on pRS304 is located at 1923-1928. The sites used for reattaching on Aim2 are
located at 459-464 and 2607-2612.

Develop3 report:
-------------------------------------------------------------------
In nucleotides
Start of excised fragment: 460
End of excised fragment: 2612
-------------------------------------------------------------------

Apply2:
o) 6420 nucleotides long

Reflect2:
p) The sites are recombined into GGATCT and AGATCC, they and their complement can still be cut
by BstYI but not BamHI, though BstYI will cut other parts of the plasmid as well.