COMPSCI 260 - Problem Set 2, Problem 1
Due: Fri 30 Sept 2022, 5pm

Name: David Lu
NetID: zl303

Statement of collaboration and resources used (put None if you worked
entirely without collaboration or resources; otherwise cite carefully): 
None
My solutions and comments for this problem are below.
-----------------------------------------------------
Plan1:
a) (n-m+1)/(4^(m))

Develop1:
b) Cycle through the (n-m+1) possible starting points and compare the
next m nucleotides with the read. The worst case run time is Theta(nm).

Reflect1:
c)Suppose we look at the worst cas for the algorithms.
The original takes Theta(knm). The new method takes Theta((km+n)logn). When km >n,
the new method takes Theta(kmlogn), which is worth it. When km < n, the latter
method takes Theta(nlogn), which is worth it when km > logn. In all, the
preprocessing method is worth it when km > logn.


