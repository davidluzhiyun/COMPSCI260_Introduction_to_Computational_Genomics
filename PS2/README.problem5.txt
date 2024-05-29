COMPSCI 260 - Problem Set 2, Problem 5 (Extra Challenge)
Due: Fri 30 Sept 2022, 5pm

Name:
NetID:

Statement of collaboration and resources used (put None if you worked
entirely without collaboration or resources; otherwise cite carefully):
None
My solutions and comments for this problem are below.
-----------------------------------------------------

Go to the basement, split all wires into two groups and connect all wires in
one of the  groups, label the groups. Go to the roof, select one wire end and test
connectivity with the wire. If none is connected with the wire, change until you find an end
of a wire in the connected group This way we can know which group are wires the basement
ends from. Label the groups, then split each group into two subgroups. Pick one
subgroup each from the previously connected group and the previously unconnected group,
connect all the ends in the two subgroups together. Go to the basement and conduct the same
test as before. Using previous labels, we have split the roof ends and basement ends into
four groups, where the corresponding end for each basement end in a group must be in the
corresponding roof end group. Repeat the procedure for each group.
Base cases: For groups with 4 wires in them, the above procedure will be able to find the end
pairs for each individual wire.
For groups with 3 wires in them. The procedure is similar. After the first test at the roof,
you are able to identify a wire's ends and a group of two. Connect the roof end of the identified
wire and one roof end of the group of two. You are then able to identify all three wires when
you take readings at the basement.
Since we are only considering the time/effort from climbing the stairs. Let n be the number of wires,
the total effort/time is Theta(logn)