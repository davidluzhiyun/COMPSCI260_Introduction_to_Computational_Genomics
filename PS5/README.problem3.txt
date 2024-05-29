COMPSCI 260 - Problem Set 5, Problem 3
Due: Fri 11 Nov 2022, 5pm

Name: David Lu
NetID: zl303

Statement of collaboration and resources used (put None if you worked
entirely without collaboration or resources; otherwise cite carefully):
https://en.wikipedia.org/wiki/Human_coronavirus_229E
https://en.wikipedia.org/wiki/Human_coronavirus_OC43
https://blast.ncbi.nlm.nih.gov/
My solutions and comments for this problem are below.
-----------------------------------------------------
Apply1:
a)
Report:
-----------------------------------------------------
	       2       3       4       5       6       7
1	  0.6669  0.0024  0.0008  0.7154  0.0000  0.0047
2	          0.6661  0.6669  0.7231  0.6669  0.6672
3	                  0.0031  0.7154  0.0024  0.0071
4	                          0.7154  0.0008  0.0055
5	                                  0.7154  0.7170
6	                                          0.0047
-----------------------------------------------------

b)
Student 1 and 6 could potentially have identical spike protein sequences, but I can't be sure based solely on the table.
It is because compute dist() only looks at type I columns and with ignore any insertion/deletion between the two
sequences.

c)
The distance is not ultrametric but is additive. Therefore, we can apply the NJ algorithm but not UPGMA

Apply2:
e)
-----------------------------------------------------
Newick representation of the phylogenetic tree:
(6:0.0000000,(1:-0.0000000,(4:0.0006876,(3:0.0017311,(7:0.0032891,(2:0.3371325,5:0.3860156):0.3272632):0.0011244):0.0005929):0.0000980):0);
-----------------------------------------------------

g)
Student  Accession   Virus name                                       Common name of virus
1        UAW54870.1  Severe acute respiratory syndrome coronavirus 2  SARS-CoV-2
2        AOL02453.1  Human coronavirus OC43                           common cold
3        UFA80410.1  Severe acute respiratory syndrome coronavirus 2  SARS-CoV-2
4        BCN86353.1  Severe acute respiratory syndrome coronavirus 2  SARS-CoV-2
5        APT69856.1  Human coronavirus 229E                           common cold
6        UAW54870.1  Severe acute respiratory syndrome coronavirus 2  SARS-CoV-2
7        QVN38512.1  Severe acute respiratory syndrome coronavirus 2  SARS-CoV-2

h)
Student 2 and 5 have common cold caused by two different types of viruses. The rest have COVID-19. One the tree, this
is reflected by the fact that 2 and 5 are far away from each other and the rest of students and the rest cluster
together almost on one point comparing to 2 and 5.

i)
Report:
-----------------------------------------------------
Two SARS-CoV-2 genome sequences that are most similar:
Student 1 and Student 6
Match(es): 1273
Mismatch(es): 0
Gap(s): 0

Two SARS-CoV-2 genome sequences that are most different:
Student 3 and Student 7
Match(es): 1261
Mismatch(es): 9
Gap(s): 3

Two genome sequences that are most different overall:
Student 2 and Student 5
Match(es): 299
Mismatch(es): 781
Gap(s): 369
-----------------------------------------------------
Student 1 and 6 indeed have the same sequence. The difference between different strains of SARS-CoV-2 is much smaller
than that between SARS-CoV-2 and other viruses could be.

j) It is likely that Student 6 got COVID-19 from Student 1 or vice versa. It is also likely that they both contracted
COVID-19 from the same source

k) Student 7 has likely contracted the Alpha variant. I drew the conclusion from the two deletions near the beginning
of the spike protein and the six mismatches from the sample from Student 1.
Student 3's SARS-CoV-2 spike protein has fewer mutations than any of the variants listed. I can't only assume it is
either Epsilon variant or one of the other variants that came before Alpha.