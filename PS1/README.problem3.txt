COMPSCI 260 - Problem Set 1, Problem 3
Due: Fri 16 Sep 2022, 5pm

Name: David Lu
NetID: zl303

Statement of collaboration and resources used (put None if you worked
entirely without collaboration or resources; otherwise cite carefully):
https://stackoverflow.com/questions/43149086/python-3-regex-find-all-overlapping-matches-start-and-end-index-in-a-string

My solutions and comments for this problem are below.
-----------------------------------------------------

Plan1:
My approch is to compare the ends of the contigs. It could be made impossible
if there are gaps in readings. If there are contigs that completely contain another
contig. Repeating sequence can also cause problems. I could use a greedy approach
and discard ambiguous contigs if I have enough reads. The approach works relative
good if enough reads are evenly distributed on a not too long segment and can' handle
errors in reads. If I assume the genome have repeated sequences, I might need to think
more about how to first cut the genome into manageable peices. The method also don't deal
with peices from two strands.

Develop1 report:
-----------------------------------------------------
Length of assembled plasmid: 8541
agaaagaacagcagagtaccggaagtggctccagtagtacgtctgctggtaactcaatctcagcaaaagttagtgtatcgattgggggtaatgtgtcaaa
cgtagcttcagggtcgcgtggcacgctgtctagttctactgacctaatgcaaactgctacgcccctaaacagctctgaatctggaggcgcctccaactcg
ggagagggcagtgaacaagaggctatatacgaaaagcttagattgctcaacactcagcacgcagcggggcctgggcccctcgaaccagcacgtgccgccc
ccttagtaggacagtcgccaaatcaccttgggacacggtcatcgcacccccaattggtccatggcaatcatcaggcattgcaacagcatcagcaacagtc
atggcctcctcgtcattactcaggctcgtggtaccctacgtccctttctgagatcccaatatcttcggcccctaatattgcaagcgttactgcttacgcc
tccgggccgtctcttgctcactcactgagccctcctaatgatatagagagccttgcttcgataggtcaccaaaggaattgtcctgtagctacagaggaca
tccacttgaagaaggagctcgacgggcaccaatcagatgaaaccgggtccggggagggcgaaaactcaaacggtggcgcctctaacattggtaatacgga
agacgaccaagcccgactgattctcaaacgaaagctccaaaggaataggaccagtttcacaaacgaccaaatagactctctagagaaagagtttgaacga
actcactacccggacgtatttgctcgcgagcgattggccggcaagattgggttgccagaggcccgaattcaggtctggttttctaaccgacgggcgaaat
ggaggcgtgaagaaaaattgcgcaaccagcggaggactccgaactcaacaggcgcgtctgcaacatcctcgagtacctcggctacggcatcacttacaga
ttcgccgaacagtttatccgcctgctcctcacttttaagcggttcagcgggtggtccctcagtgtctacgatcaatgggctgtcgtccccatctacgctt
tcgacaaatgtgaacgctcctaccctcggtgctggaatcgattcgagtgagagcccaacaccgataccgcacatacggccgtcatgcacaagtgataatg
ataatgggcgccaatccgaggattgtcgaagggtatgtagtccttgtcccctaggggttggaggccatcaaaatacacaccacatccaaagtaacggcca
cgcgcaggggcacgcgttggttccggcgatttcgcctcgcctgaactttaattcaggctccttcggcgcgatgtattcaaatatgcatcataccgcttta
tctatgtctgattcttacggcgccgtcaccccaatcccttcgtttaaccattcggccgtcggaccccttgcgccccctagcccgatcccgcagcagggag
acttaacgccgtcatctctttacccatgccacatgactctccgaccgcctccgatggcccccgctcaccaccatatcgtgccgggcgacggaggccggcc
agccggtgtagggctgggctcggggcagtcggccaatcttggcgctagttgctcagggtcagggtacgaggtgctgtcagcatacgcgttgcctcccccc
ccgatggcttcttcgtctgcggccgattctagtttctccgcagcaagttcagcttcggccaatgtaaccccacatcatacaattgctcaggagtcttgtc
cgtccccatgctctagcgcttcccactttggagttgcgcatagttctgggttttcctcagacccgatctcgcccgcggtgtcctcgtacgcccatatgag
ctataattacgcctcatcggccaacacaatgactccctcctctgcatcaggcacttccgctcacgtagctccagggaagcagcaattcttcgctagctgc
ttctattcaccctgggtctagggtggcctaactacggctacactagaaggacagtatttggtatctgcgctctgctgaagccagttaccttcggaaaaag
agttggtagctcttgatccggcaaacaaaccaccgctggtagcggtggtttttttgtttgcaagcagcagattacgcgcagaaaaaaaggatctcaagaa
gatcctttgatcttttctacggggtctgacgctcagtggaacgaaaactcacgttaagggattttggtcatgagattatcaaaaaggatcttcacctaga
tccttttaaattaaaaatgaagttttaaatcaatctaaagtatatatgagtaaacttggtctgacagttaccaatgcttaatcagtgaggcacctatctc
agcgatctgtctatttcgttcatccatagttgcctgactccccgtcgtgtagataactacgatacgggagggcttaccatctggccccagtgctgcaatg
ataccgcgagacccacgctcaccggctccagatttatcagcaataaaccagccagccggaagggccgagcgcagaagtggtcctgcaactttatccgcct
ccatccagtctattaattgttgccgggaagctagagtaagtagttcgccagttaatagtttgcgcaacgttgttgccattgctacaggcatcgtggtgtc
acgctcgtcgtttggtatggcttcattcagctccggttcccaacgatcaaggcgagttacatgatcccccatgttgtgcaaaaaagcggttagctccttc
ggtcctccgatcgttgtcagaagtaagttggccgcagtgttatcactcatggttatggcagcactgcataattctcttactgtcatgccatccgtaagat
gcttttctgtgactggtgagtactcaaccaagtcattctgagaatagtgtatgcggcgaccgagttgctcttgcccggcgtcaatacgggataataccgc
gccacatagcagaactttaaaagtgctcatcattggaaaacgttcttcggggcgaaaactctcaaggatcttaccgctgttgagatccagttcgatgtaa
cccactcgtgcacccaactgatcttcagcatcttttactttcaccagcgtttctgggtgagcaaaaacaggaaggcaaaatgccgcaaaaaagggaataa
gggcgacacggaaatgttgaatactcatactcttcctttttcaatattattgaagcatttatcagggttattgtctcatgagcggatacatatttgaatg
tatttagaaaaataaacaaataggggttccgcgcacatttccccgaaaagtgccacctgggtccttttcatcacgtgctataaaaataattataatttaa
attttttaatataaatatataaattaaaaatagaaagtaaaaaaagaaattaaagaaaaaatagtttttgttttccgaagatgtaaaagactctaggggg
atcgccaacaaatactaccttttatcttgctcttcctgctctcaggtattaatgccgaattgtttcatcttgtctgtgtagaagaccacacacgaaaatc
ctgtgattttacattttacttatcgttaatcgaatgtatatctatttaatctgcttttcttgtctaataaatatatatgtaaagtacgctttttgttgaa
attttttaaacctttgtttatttttttttcttcattccgtaactcttctaccttctttatttactttctaaaatccaaatacaaaacataaaaataaata
aacacagagtaaattcccaaattattccatcattaaaagatacgaggcgcgtgtaagttacaggcaagcgatccgtcctaagaaaccattattatcatga
cattaacctataaaaataggcgtatcacgaggccctttcgtctccgcgcccgtttcggtgatgacggtgaaaacctctgacacatgcagctcccggagac
ggtcacagcttgtctgtaagcggatgccgggagcagacaagcccgtcagggcgcgtcagcgggtgttggcgggtgtcggggctggcttaactatgcggca
tcagagcagattgtactgagagtgcaccatatcgactacgtcgtaaggccgtttctgacagagtaaaattcttgagggaactttcaccattatgggaaat
ggttcaagaaggtattgacttaaactccatcaaatggtcaggtcattgagtgttttttatttgttgtatttttttttttttagagaaaatcctccaatat
caaattaggaatcgtagtttcatgattttctgttacacctaactttttgtgtggtgccctcctccttgtcaatattaatgttaaagtgcaattctttttc
cttatcacgttgagccattagtatcaatttgcttacctgtattcctttactatcctcctttttctccttcttgataaatgtatgtagattgcgtatatag
tttcgtctaccctatgaacatattccattttgtaatttcgtgtcgtttctattatgaatttcatttataaagtttatgtacaaatatcataaaaaaagag
aatctttttaagcaaggattttcttaacttcttcggcgacagcatcaccgacttcggtggtactgttggaaccacctaaatcaccagttctgatacctgc
atccaaaacctttttaactgcatcttcaatggccttaccttcttcaggcaagttcaatgacaatttcaacatcattgcagcagacaagatagtggcgata
gggtcaaccttattctttggcaaatctggagcagaaccgtggcatggttcgtacaaaccaaatgcggtgttcttgtctggcaaagaggccaaggacgcag
atggcaacaaacccaaggaacctgggataacggaggcttcatcggagatgatatcaccaaacatgttgctggtgattataataccatttaggtgggttgg
gttcttaactaggatcatggcggcagaatcaatcaattgatgttgaaccttcaatgtagggaattcgttcttgatggtttcctccacagtttttctccat
aatcttgaagaggccaaaacattagctttatccaaggaccaaataggcaatggtggctcatgttgtagggccatgaaagcggccattcttgtgattcttt
gcacttctggaacggtgtattgttcactatcccaagcgacaccatcaccatcgtcttcctttctcttaccaaagtaaatacctcccactaattctctgac
aacaacgaagtcagtacctttagcaaattgtggcttgattggagataagtctaaaagagagtcggatgcaaagttacatggtcttaagttggcgtacaat
tgaagttctttacggatttttagtaaaccttgttcaggtctaacactaccggtaccccatttaggaccacccacagcacctaacaaaacggcatcaacct
tcttggaggcttccagcgcctcatctggaagtgggacacctgtagcatcgatagcagcaccaccaattaaatgattttcgaaatcgaacttgacattgga
acgaacatcagaaatagctttaagaaccttaatggcttcggctgtgatttcttgaccaacgtggtcacctggcaaaacgacgatcttcttaggggcagac
ataggggcagacattagaatggtatatccttgaaatatatatatatattgctgaaatgtaaaaggtaagaaaagttagaaagtaagacgattgctaacca
cctattggaaaaaacaataggtccttaaataatattgtcaacttcaagtattgtgatgcaagcatttagtcatgaacgcttctctattctatatgaaaag
ccggttccggcctctcacctttcctttttctcccaatttttcagttgaaaaaggtatatgcgtcaggcgacctctgaaattaacaaaaaatttccagtca
tcgaatttgattctgtgcgatagcgcccctgtgtgttctcgttatgttgaggaaaaaaataatggttgctaagagattcgaactcttgcatcttacgata
cctgagtattcccacagttaactgcggtcaagatatttcttgaatcaggcgccttagaccgctcggccaaacaaccaattacttgttgagaaatagagta
taattatcctataaatataacgtttttgaacacacatgaacaaggaagtacaggacaattgattttgaagagaatgtggattttgatgtaattgttggga
ttccatttttaataaggcaataatattaggtatgtggatatactagaagttctcctcgaccgtcgatatgcggtgtgaaataccgcacagatgcgtaagg
agaaaataccgcatcaggaaattgtaaacgttaatattttgttaaaattcgcgttaaatttttgttaaatcagctcattttttaaccaataggccgaaat
cggcaaaatcccttataaatcaaaagaatagaccgagatagggttgagtgttgttccagtttggaacaagagtccactattaaagaacgtggactccaac
gtcaaagggcgaaaaaccgtctatcagggcgatggcccactacgtgaaccatcaccctaatcaagttttttggggtcgaggtgccgtaaagcactaaatc
ggaaccctaaagggagcccccgatttagagcttgacggggaaagccggcgaacgtggcgagaaaggaagggaagaaagcgaaaggagcgggcgctagggc
gctggcaagtgtagcggtcacgctgcgcgtaaccaccacacccgccgcgcttaatgcgccgctacagggcgcgtcgcgccattcgccattcaggctgcgc
aactgttgggaagggcgatcggtgcgggcctcttcgctattacgccagctggcgaaagggggatgtgctgcaaggcgattaagttgggtaacgccagggt
tttcccagtcacgacgttgtaaaacgacggccagtgagcgcgcgtaatacgactcactatagggcgaattgggtaccgggccccccctcgaggtcgacgg
tatcgataagcttgatatcgaattcctgcagcccgggggatccactagttctagagcggccgccaccgcggtggagctccagcttttgttccctttagtg
agggttaattgcgcgcttggcgtaatcatggtcatagctgtttcctgtgtgaaattgttatccgctcacaattccacacaacataggagccggaagcata
aagtgtaaagcctggggtgcctaatgagtgaggtaactcacattaattgcgttgcgctcactgcccgctttccagtcgggaaacctgtcgtgccagctgc
attaatgaatcggccaacgcgcggggagaggcggtttgcgtattgggcgctcttccgcttcctcgctcactgactcgctgcgctcggtcgttcggctgcg
gcgagcggtatcagctcactcaaaggcggtaatacggttatccacagaatcaggggataacgcaggaaagaacatgtgagcaaaaggccagcaaaaggcc
aggaaccgtaaaaaggccgcgttgctggcgtttttccataggctccgcccccctgacgagcatcacaaaaatcgacgctcaagtcagaggtggcgaaacc
cgacaggactataaagataccaggcgtttccccctggaagctccctcgtgcgctctcctgttccgaccctgccgcttaccggatacctgtccgcctttct
cccttcgggaagcgtggcgctttctcatagctcacgctgtaggtatctcagttcggtgtaggtcgttcgctccaagctgggctgtgtgcacgaacccccc
gttcagcccgaccgctgcgccttatccggtaactatcgtcttgagtccaacccggtaagacacgacttatcgccactggcagcagccactggtaacagga
ttagcagagcgaggtatgtaggcggtgctacagagttcttgaagtatgttcacgctacagccgacgcctactgcgatcggaacagttgtacctccgtgga
gtgctggcacactgatagaacgcctacccagtcttgaagacatggctcataagggtcatagcggtgtcaatcagctgggaggcgtttttgtcgggggcag
gccattgccagactcaacacgtcaaaagatcgtggaactcgcccattcgggggctcggccttgtgatatttctcggattcttcaagttagcaacggatgt
gtatctaagattttggggcgctactacgaaactggctccatacgcccccgcgccataggcggcagcaaaccacgcgttgcaactgctgaagtcgtatcca
aaatatcacagtataagagagaatgtccttcgatatttgcgtgggagatacgggatcggctcctccaggagaatgtttgcactaatgataatatcccctc
ggtctcatcgattaacagagttcttcggaacttggcagctc
-----------------------------------------------------

Apply1:
c) 8541

Reflect1:
d) Yes. 8541 is a multiple of three. Also, the average length of each read
is 8541/14 + 15 = 625.07, which is close to the value provided.

Apply2 report:
-----------------------------------------------------
ORFs in the plasmid (Start and stop in nucleotides and inclusive):

    Frame: 2
    Stop: 2021
    Length in amino acids 838
    Start: 8046
    Stop Codon: TAG
    Length in nucleotides: 2517
    Strand: W

    Frame: 0
    Stop: 528
    Length in amino acids 55
    Start: 361
    Stop Codon: TGA
    Length in nucleotides: 168
    Strand: W

    Frame: 1
    Stop: 2764
    Length in amino acids 88
    Start: 2498
    Stop Codon: TGA
    Length in nucleotides: 267
    Strand: W

    Frame: 1
    Stop: 2941
    Length in amino acids 56
    Start: 2771
    Stop Codon: TGA
    Length in nucleotides: 171
    Strand: W

    Frame: 0
    Stop: 4119
    Length in amino acids 52
    Start: 3961
    Stop Codon: TGA
    Length in nucleotides: 159
    Strand: W

    Frame: 0
    Stop: 5040
    Length in amino acids 103
    Start: 4729
    Stop Codon: TGA
    Length in nucleotides: 312
    Strand: W

    Frame: 0
    Stop: 5277
    Length in amino acids 67
    Start: 5074
    Stop Codon: TAA
    Length in nucleotides: 204
    Strand: W

    Frame: 0
    Stop: 6072
    Length in amino acids 66
    Start: 5872
    Stop Codon: TAA
    Length in nucleotides: 201
    Strand: W

    Frame: 0
    Stop: 105
    Length in amino acids 57
    Start: 8473
    Stop Codon: TAG
    Length in nucleotides: 174
    Strand: W

    Frame: 2
    Stop: 575
    Length in amino acids 58
    Start: 399
    Stop Codon: TAA
    Length in nucleotides: 177
    Strand: C

    Frame: 1
    Stop: 1885
    Length in amino acids 192
    Start: 1307
    Stop Codon: TAG
    Length in nucleotides: 579
    Strand: C

    Frame: 0
    Stop: 2388
    Length in amino acids 50
    Start: 2236
    Stop Codon: TAA
    Length in nucleotides: 153
    Strand: C

    Frame: 1
    Stop: 3934
    Length in amino acids 368
    Start: 2828
    Stop Codon: TAA
    Length in nucleotides: 1107
    Strand: C

    Frame: 2
    Stop: 3491
    Length in amino acids 66
    Start: 3291
    Stop Codon: TGA
    Length in nucleotides: 201
    Strand: C

    Frame: 2
    Stop: 3770
    Length in amino acids 56
    Start: 3600
    Stop Codon: TGA
    Length in nucleotides: 171
    Strand: C

    Frame: 0
    Stop: 6174
    Length in amino acids 286
    Start: 5314
    Stop Codon: TAA
    Length in nucleotides: 861
    Strand: C

    Frame: 2
    Stop: 7673
    Length in amino acids 101
    Start: 7368
    Stop Codon: TGA
    Length in nucleotides: 306
    Strand: C

    Frame: 0
    Stop: 8295
    Length in amino acids 51
    Start: 8140
    Stop Codon: TGA
    Length in nucleotides: 156
    Strand: C

    18 ORF(s) in Total
-----------------------------------------------------

Apply2:
g) 18 in total, there are overlaps
h) All the coding sequence counted with coordinates on W strand and length in nucleotides:
8046-2018 2514
361-525 165
2498-2761 264
2771-2938 168
3961-4116 156
4729-5037 309
5074-5274 201
5872-6069 198
8473-102 171
7970-8143 174
6660-7235 576
6157-6306 150
4611-5714 1104
5054-5251 198
4775-4942 168
2371-3228 858
872-1174 303
250-402 153
Upon merging overlapping sequences:
2371-3228 858
3961-4116 156
4611-5714 1104
5872-6069 198
6157-6306 150
6660-7235 576
7970-2018 2590
Total length 5632, fraction of total sequence 65.94%

Reflect:
Paired box protein Pax-6 isoform X2. It controls the development of eyes and
other sensory organs. I am not surprised tto find it in a bacterial plasmid.
Humans might have put it in for cloning
