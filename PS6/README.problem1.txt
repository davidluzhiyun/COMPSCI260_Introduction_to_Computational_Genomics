COMPSCI 260 - Problem Set 6, Problem 1
Due: Wed 23 November 2022, 5pm

Name: David Lu
NetID: zl303

Statement of collaboration and resources used (put None if you worked
entirely without collaboration or resources; otherwise cite carefully): 
None
My solutions and comments for this problem are below.
-----------------------------------------------------
a) Probability that Murray actually has the disease, given that he tested positive
P = ((1/40000)*(99.7%))/((1/40000)*(99.7%) + (1-1/40000)*(1-99.7%))
  = 0.82%

b) While the test is 99.7% accurate, the disease itself is extremely rare. This means the probability of having the
disease even when given someone has tested positive is still very low. The test accuracy need to be much higher, such
that (1-accuracy) is at a order of magnitude lower than that of 1/40000 to observe a smaller false discovery rate.

c) Yes, because we do not know about the environmental factors that cause the disease and the environment Murray grew
up in.