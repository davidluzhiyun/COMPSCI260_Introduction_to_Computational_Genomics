COMPSCI 260 - Problem Set 6, Problem 3
Due: Wed 23 November 2022, 5pm

Name: David Lu
NetID: zl303

Statement of collaboration and resources used (put None if you worked
entirely without collaboration or resources; otherwise cite carefully): 
https://miguendes.me/python-compare-lists
My solutions and comments for this problem are below.
-----------------------------------------------------
Plan:
a)
WWWW
P = 0.5 * 0.97 * 0.97 * 0.97 = 0.4563365

WWWS
P = 0.5 * 0.97 * 0.97 * 0.03 = 0.0141135

WWSW
P = 0.5 * 0.97 * 0.03 * 0.12 = 0.001746

WWSS
P = 0.5 * 0.97 * 0.03 * 0.88 = 0.012804

WSWW
P = 0.5 * 0.03 * 0.12 * 0.97 = 0.001746

WSWS
P = 0.5 * 0.03 * 0.12 * 0.03 = 0.000054

WSSW
P = 0.5 * 0.03 * 0.88 * 0.12 = 0.001584

WSSS
P = 0.5 * 0.03 * 0.88 * 0.88 = 0.011616

SWWW
P = 0.5 * 0.12 * 0.97 * 0.97 = 0.056454

SWWS
P = 0.5 * 0.12 * 0.97 * 0.03 = 0.001746

SWSW
P = 0.5 * 0.12 * 0.03 * 0.12 = 0.000216

SWSS
P = 0.5 * 0.12 * 0.03 * 0.88 = 0.001584

SSWW
P = 0.5 * 0.88 * 0.12 * 0.97 = 0.051216

SSWS
P = 0.5 * 0.88 * 0.12 * 0.03 = 0.001584

SSSW
P = 0.5 * 0.88 * 0.88 * 0.12 = 0.046464

SSSS
P = 0.5 * 0.88 * 0.88 * 0.88 = 0.340736

b)
P(Π = WWSS, X = TCGA) = 0.012804 * 0.3 * 0.2 * 0.35 * 0.15 = 0.0000403326
No, the latter is P(Π = WWSS|X = TCGA) = P(Π = WWSS, X = TCGA) / P(X = TCGA)
Since P(X = TCGA) < 1, the two probabilities aren't equal.

c)
P(Π = WSSW, X = TCGA) = 0.001584 * 0.3 * 0.35 *  0.35 * 0.3 = 0.0000174636
P(Π = WSSW, X = TCGA) < P(Π = WWSS, X = TCGA)
P(Π = WSSW, X = TCGA) / P(X = TCGA) < P(Π = WWSS, X = TCGA) / P(X = TCGA)
P(Π = WSSW|X = TCGA) < P(Π = WWSS|X = TCGA)
While the emission probabilities are in favor of P(Π = WSSW|X = TCGA),
the transmission probabilities are greatly against it by making P(Π = WSSW)
far lower than P(Π = WWSS). This lead to the result P(Π = WSSW|X = TCGA) <
P(Π = WWSS|X = TCGA)

d)
WWWW
Because probability of the path WWWW is the highest and the effect of emission
probability on the conditional probability is trivial comparing to the effect of
the transmission probabilities.

e)
Around 33 for W and 8 for S.
The expected length the HMM will remain in one state before transition is the
reciprocal of the probability of transition out of the state.

Apply:
h)
Report:
-----------------------------------------------------
Count of different state sequences corresponding to observed sequence TCGA:
WWWW:  248
WWSW:  2
WSSS:  17
SSSS:  42
WWSS:  10
SSSW:  13
WWWS:  2
SSWW:  2
WSSW:  1
SWWW:  2
WSWW:  1
-----------------------------------------------------
Result consistent in terms of size relationship but inconsistent in terms of value. According to (c) WWSS
should have around 2 times the count of WSSW, instead it is around 10 times in the empirical result

i)
Report:
-----------------------------------------------------
Average length the system remains in a state:
W:  34.12282192945177
S:  8.3796768707483
-----------------------------------------------------

Reflect:
j)
"WWWW" prevailed just as predicted

k)
They align with the predictions very well