COMPSCI 260 - Problem Set 2, Problem 2
Due: Fri 30 Sept 2022, 5pm

Name: David Lu
NetID: zl303

Statement of collaboration and resources used (put None if you worked
entirely without collaboration or resources; otherwise cite carefully): 
https://learnpython.com/blog/print-table-in-python/
My solutions and comments for this problem are below.
-----------------------------------------------------
Develop1:
a)(i) It will take Theta(n^3) if n is the length of the list.
(ii) The outer cycle goes through each element as the starting element.
The inner cycle cycles through each element after the starting element
(inclusive) as the ending. When calculating the list's sum, the program
either takes the value of the starting element or add the new ending
element to the sum of the previous sublist. It takes Theta(n^2) time.

b) Let n denote the list length. Compare the max sum for sublists of the
left side of the list, the max sum for sublists of the right side of the
list and the max sum for sublists crossing the middle element. The former
two are calculated with recursive funtion calls. The final one is calculated
by from the center to the left and to the right respectively, which takes
Theta(n) time. The comparison, the base case and other steps take Theta(1).
Therefore we have T(n) = T(n/2) + Theta(n), where T(n) is the time taken for worst case.
T(n) = Theta(n) + 2(Theta(n/2)) + 4(Theta(n/4)) + .... + n(Theta(1))
     = lognTheta(n)
     = Theta(nlogn)

c) MAX_INCLUDING_HERE will be updated to be the larger between its previous value plus the
current element and the current element.
MAX_SO_FAR will be updated to the largest historical value of MAX_INCLUDING_HERE.
The update for MAX_INCLUDING_HERE works because: If the new sublist for MAX_INCLUDING_HERE
contains previous element, the previous elements must be from the previous MAX_INCLUDING_HERE
or else the sublist can't be continuous and the largest. If the previous
MAX_INCLUDING_HERE is negative, then the new MAX_INCLUDING_HERE wil simply be the
current element.
MAX_SO_FAR works because the sublist with the largest sum must end somewhere and be the
largest sum for sublists ending there.
The comparison, adding, and assignment together take Theta(1) for each iteration. Since the
algorithm cycles through the given list once, it takes Theta(n) time in total.

Apply1:
d)
     brute force runtime divide & conquer runtime  linear runtime
10^2            0.000706                 0.000411        0.000048
10^3            0.051192                 0.003402        0.000348
10^4            5.186803                 0.037364        0.003648
10^5          407.052587                 0.239935        0.021492
10^6                 N/A                 2.712608        0.218832
10^7                 N/A                29.441222        2.257118
10^8                 N/A                      N/A       22.754005

Extra Challenge: We can generate a 10^8 length random list beforehand and run
the methods on sublists of the pre-generated list.

Reflect1:
e)
     brute force runtime divide & conquer runtime  linear runtime
10^6           ~4*(10^4)                 2.712608        0.218832
10^7           ~4*(10^6)                29.441222        2.257118
10^8           ~4*(10^8)                     ~310       22.754005
10^9          ~4*(10^10)                    ~3300            ~220

f) Everytime the input length increase 10-fold, the brute force method runtime
increase about 100-fold, linear method runtime increase about 10-fold. In theory
the divide & conquer method should approximately increase first by a constant
then 10-fold, but this isn't obvious in the observed result.