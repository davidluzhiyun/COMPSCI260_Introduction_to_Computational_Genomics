COMPSCI 260 - Problem Set 2, Problem 4
Due: Fri 30 Sept 2022, 5pm

Name: David Lu
NetID: zl303

Statement of collaboration and resources used (put None if you worked
entirely without collaboration or resources; otherwise cite carefully):
None
My solutions and comments for this problem are below.
-----------------------------------------------------
a) The algorithm is first forced to choose A1 for its small length. This
makes A3 and A4 unavailable. Between A5 and A2, the algorithm will choose
A2 for its smaller length. This makes A5 unavailable and terminates the
program. The solution selected 2 activities instead of 3. The latter is
achieved when A3,A4,A5 is selected. The output of the algorithm is therefore
suboptimal
b) Assume in tie cases the program doesn't crash and will give a result from
among the tie options. The algorithm will first choose A2, nullifying A4 and
A5. Then It will choose one from A1, A6, A7 or A8, nullifying the rest of this
stack of activities. Next it will do the same for A3, A9, A10, A11, A12 and
terminate. This results in three activities, suboptimal comparing to chosing
A1, A4, A5, A3