COMPSCI 260 - Problem Set 2, Problem 3
Due: Fri 30 Sept 2022, 5pm

Name: David Lu
NetID: zl303

Statement of collaboration and resources used (put None if you worked
entirely without collaboration or resources; otherwise cite carefully): 
None
My solutions and comments for this problem are below.
-----------------------------------------------------

Plan1:
a) 8 in total. Squares with peddles in them are marked with one, empty square are
marked as zero, we can enumerate the patterns as below:
1010
1001
0101
1000
0100
0010
0001
0000

b) We don't need to worry about running out of pebbles because the grid can only fit 2n pebbles
at most judging by the result of (a)
For each k we calculate the maximum value of the total pattern given the valid pattern
on the last row, denoted as Tk[p] for convenience. "p" goes from 0 to 7, each representing
a valid pattern on the kth row. To facilitate the updating of Tk[p], we need to calculate
the value for the kth row given pattern p. We are denoting it as Rk[p]. Tk[p] It is calculated
and updated in the following fashion:
For the base case k = 1, T1[p] = R1[p]
For k > 1, let p1, p2... pi be the compatible patterns with p. Tk[p] = max(T(k-1)[p1], T(k-1)[p2]... T(k-1)[pi])
The updating process takes O(1) time given fixed number of valid patterns each row.
The eventual result we are looking for is max(Tn[0]..Tn[7]). Tn[p] is obtained after we cycle through
the rows once. The eventual step and other things take O(1) time. Therefore, the algorithm takes O(n) time
when n is the number of rows in the file.

Apply1:
d) 10708

Reflect1:
e)
1 3000 3 2000
100 2 4 555
4000 4 2000 4

The optimal pattern for the row before our row and that of the row after our row has no common
compatible none zero pattern and the value of both are larger that the largest achievable value of our row
may cause pattern of the row to be set to zero.