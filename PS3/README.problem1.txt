COMPSCI 260 - Problem Set 3, Problem 1
Due: Fri 14 Oct 2022, 5pm

Name: David Lu
NetID: zl303

Statement of collaboration and resources used (put None if you worked
entirely without collaboration or resources; otherwise cite carefully):
None
My solutions and comments for this problem are below.
-----------------------------------------------------
Plan:

a) C = (RL) / G

b) (i) Ignoring edge effect and assume G >> L
Probability = (1 - (L / (G - L + 1))) ^ R = (1 - L / G) ^ R
= (1 - C / R) ^ R
(ii) Expected Value = G (1 -  C / R) ^ R = G (1 - L / G) ^ (C(G / L))
= G * (e ^ (-C))

c) (i) Ignore all edge effects. For the last read in a contig, no other reads start in it.
Probability for a read to be the last read = (1 - L/G) ^ R
Number of contigs = R((1 - L/G) ^ R ) = R * (e ^ (-C))
(ii) Expected Length = (G - G * (e ^ (-C)))/ R * (e ^ (-C))

Develop:

d) As is established in the planning section, it is reasonable to ignore
edge effect when G is large enough. Since G is indeed large in the simulation,
it is sensible to simulate the edges as they are.

Apply:

e) Report
-----------------------------------------------------
All floating point results truncated to the 2 decimal place

Simulation 1
The empirical coverage: 5.33
The number of nucleotides not covered by any read: 14974
The number of contigs: 184
The average length of these contigs: 16222.97


Simulation 2
The empirical coverage: 5.33
The number of nucleotides not covered by any read: 13524
The number of contigs: 182
The average length of these contigs: 16409.21


Simulation 3
The empirical coverage: 5.33
The number of nucleotides not covered by any read: 14195
The number of contigs: 177
The average length of these contigs: 16868.95


Simulation 4
The empirical coverage: 5.33
The number of nucleotides not covered by any read: 13370
The number of contigs: 179
The average length of these contigs: 16685.08


Simulation 5
The empirical coverage: 5.33
The number of nucleotides not covered by any read: 12013
The number of contigs: 182
The average length of these contigs: 16417.51


Simulation 6
The empirical coverage: 5.33
The number of nucleotides not covered by any read: 14376
The number of contigs: 189
The average length of these contigs: 15796.95


Simulation 7
The empirical coverage: 5.33
The number of nucleotides not covered by any read: 14510
The number of contigs: 192
The average length of these contigs: 15549.43


Simulation 8
The empirical coverage: 5.33
The number of nucleotides not covered by any read: 13507
The number of contigs: 205
The average length of these contigs: 14568.26


Simulation 9
The empirical coverage: 5.33
The number of nucleotides not covered by any read: 15426
The number of contigs: 194
The average length of these contigs: 15384.40


Simulation 10
The empirical coverage: 5.33
The number of nucleotides not covered by any read: 15080
The number of contigs: 207
The average length of these contigs: 14419.90


Simulation 11
The empirical coverage: 5.33
The number of nucleotides not covered by any read: 15268
The number of contigs: 192
The average length of these contigs: 15545.48


Simulation 12
The empirical coverage: 5.33
The number of nucleotides not covered by any read: 16534
The number of contigs: 207
The average length of these contigs: 14412.88


Simulation 13
The empirical coverage: 5.33
The number of nucleotides not covered by any read: 14927
The number of contigs: 205
The average length of these contigs: 14561.33


Simulation 14
The empirical coverage: 5.33
The number of nucleotides not covered by any read: 15500
The number of contigs: 190
The average length of these contigs: 15707.89


Simulation 15
The empirical coverage: 5.33
The number of nucleotides not covered by any read: 12195
The number of contigs: 169
The average length of these contigs: 17679.32


Simulation 16
The empirical coverage: 5.33
The number of nucleotides not covered by any read: 12755
The number of contigs: 186
The average length of these contigs: 16060.46


Simulation 17
The empirical coverage: 5.33
The number of nucleotides not covered by any read: 13045
The number of contigs: 204
The average length of these contigs: 14641.94


Simulation 18
The empirical coverage: 5.33
The number of nucleotides not covered by any read: 12367
The number of contigs: 180
The average length of these contigs: 16597.96


Simulation 19
The empirical coverage: 5.33
The number of nucleotides not covered by any read: 13526
The number of contigs: 169
The average length of these contigs: 17671.44


Simulation 20
The empirical coverage: 5.33
The number of nucleotides not covered by any read: 11942
The number of contigs: 165
The average length of these contigs: 18109.44


Average
The empirical coverage: 5.33
The number of nucleotides not covered by any read: 13951.70
The number of contigs: 187.90
The average length of these contigs: 15965.54
-----------------------------------------------------

f)
Using (a - c) we get
Coverage: 5.33
The expected number of nucleotides not covered by any read: 14532.21
The expected number of contigs: 193.76
The expected length of these contigs: 15408.07
Average coverage is the exact same because it only changes with R, L, G. The rest are close.

Reflect:

g) 1659253.11 are expected to remain unsequeced. 45000000 reads need to be generated.

h) 2*(45000000)(45000000-1) = 4.05*10^(15) comparisons

i) ((2*(45000000)(45000000-1))/(40 * (10^6)))/(3600*24*365) = 3.21 years

j) About 24888.80 contigs will be produced. Average length of contigs is
1741.38. Average length of unsequeced region is 66.66.

k) The numbers seem reasonable. The length of time it takes to assemble the contigs is shocking.