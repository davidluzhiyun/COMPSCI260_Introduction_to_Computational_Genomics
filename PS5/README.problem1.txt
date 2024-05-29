COMPSCI 260 - Problem Set 5, Problem 1
Due: Fri 11 Nov 2022, 5pm

Name: David Lu
NetID: zl303

Statement of collaboration and resources used (put None if you worked
entirely without collaboration or resources; otherwise cite carefully): 
https://www.linkedin.com/pulse/breaking-ties-k-nn-classification-nicholas-pylypiw
My solutions and comments for this problem are below.
-----------------------------------------------------
Plan:
a)
Name   Gene expression profile  Class when k = 1  Class when k = 3
Alice  (2, 3)                   ◦                 ◦                 ◦ confident
Bobby  (10, 12)                 ◦                 +                 ◦ not confident
Cindy  (8, 10)                  +                 +                 + confident
Donny  (4, 7)                   +                 ◦                 + not confident
Ellen  (8, 7)                   Undecided         ◦                 ◦ not confident

Apply:
c)
Report:
-----------------------------------------------------
k = 5. Predicting class for 10 new patients. 'R' for responsive to treatment, 'N' for non-responsive.
Patient    Class
Patient 1  R
Patient 2  N
Patient 3  R
Patient 4  R
Patient 5  R
Patient 6  N
Patient 7  N
Patient 8  N
Patient 9  R
Patient 10  R
-----------------------------------------------------
