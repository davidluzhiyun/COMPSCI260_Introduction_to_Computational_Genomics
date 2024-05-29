COMPSCI 260 - Problem Set 3, Problem 2
Due: Fri 14 Oct 2022, 5pm

Name: David Lu
NetID: zl303

Statement of collaboration and resources used (put None if you worked
entirely without collaboration or resources; otherwise cite carefully): 
https://my.clevelandclinic.org/health/drugs/22650-acidophilus#:~:text=Acidophilus%20(lactobacillus%20acidophilus)%20is%20a,good%20bacteria%20in%20your%20body.
http://researcherslinks.com/current-issues/Impacts-Lactobacillus-acidophilus-Fermentation-Product-Digestibility-Immune/20/1/5010/html
https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4148456/
https://www.nature.com/articles/s41598-022-12721-4
https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6912755/
https://atlasbiomed.com/blog/prevotella-bacteria-guide-for-health/
https://www.nature.com/articles/ismej20124
https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3863721/

My solutions and comments for this problem are below.
-----------------------------------------------------
Plan1:

a)Lactobacillus acidophilus:
Lactobacillus acidophilus is a bacteria naturally found in the GI system and
other parts of the human body. Similar to Bifidobacterium longum, it is believed
to prevent growth of pathogenic organisms via production of lactic acid.

Peptoniphilus timonensis:
While not much can be found about the specific species. Bacteria of the genus Peptoniphilus
are commensals of the human gut, doing no harm no good. However, in some events Peptoniphilus
are known to spill into other parts of the body such as the pelvis or blood as part of mixed
polymicrobial infections.


Prevotella copri:
Prevotella copri are commensals of the human gut. Prevotella copri is the most common among
Prevotella in the human GI track with estimates indicating 40% prevalence in the wider human
population and relative abundances that exceed 50% in some individuals1. This species is more
prevalent in non-Western populations likely due to its association with high fibre low fat diets.
While itself not a pathogen, an increase in Prevotella copri might signal other problems. It might
play a row in the human immune system.

Ruminococcus bromii:
Ruminococcus bromii is a keystone species essential for the ability to digest particulate substrates
such as dietary fiber and resistant starch (RS) in the human colon. They naturally inhabit the human
GI tract.

Vibrio cholerae:
Vibrio cholerae is a species naturally live in brackish or saltwater. Some strains cause the deadly de
disease cholera when infecting the small intestine of human.

Apply1:
d) Report:
-----------------------------------------------------
patient1:
Prevalence:
Bacteroides ovatus: 0.19507022528110118
Bacteroides thetaiotaomicron: 0.16405906126205433
Bifidobacterium longum: 0.04751710615821696
Eubacterium rectale: 0.030010803889400185
Lactobacillus acidophilus: 0.06652394862150374
Peptoniphilus timonensis: 0.13154735704853748
Prevotella copri: 0.08753151134408386
Roseburia intestinalis: 0.14455203873394423
Ruminococcus bromii: 0.08152935056620383
Vibrio cholerae: 0.051658597094954184

patient2:
Prevalence:
Bacteroides ovatus: 0.065
Bacteroides thetaiotaomicron: 0.0375
Bifidobacterium longum: 0.0515
Eubacterium rectale: 0.0405
Lactobacillus acidophilus: 0.013
Peptoniphilus timonensis: 0.0765
Prevotella copri: 0.1295
Roseburia intestinalis: 0.0435
Ruminococcus bromii: 0.0465
Vibrio cholerae: 0.4965

patient3:
Prevalence:
Bacteroides ovatus: 0.2145
Bacteroides thetaiotaomicron: 0.1545
Bifidobacterium longum: 0.061
Eubacterium rectale: 0.0435
Lactobacillus acidophilus: 0.0585
Peptoniphilus timonensis: 0.161
Prevotella copri: 0.0985
Roseburia intestinalis: 0.13
Ruminococcus bromii: 0.078
Vibrio cholerae: 0.0005
-----------------------------------------------------

Reflect1:

e) Patient 2 has an unusually high prevalence of Vibrio cholerae. Patient 2 also has
low prevalence of Bacteroides, Lactobacillus acidophilus. Patient 1 also has elevated
levels of Vibrio cholerae.

Apply2:
g) Report:
-----------------------------------------------------
Longest zeros for patient1 (Vibrio cholerae): 5015-5079
Patient 2's vector doesn't have internal strings of zero
-----------------------------------------------------

Reflect2:
h) Report:
-----------------------------------------------------
longest missing sequence patient1:
TACCGGCCAGGTGCAACTTTTCAAGTAGAAGTACCAGGTAGTCAACATATAGATTCACAA
CCTTT
-----------------------------------------------------
BLAST results show high similarity with Vibrio cholerae enterotoxin subunit B (ctxB) gene of several
strains. This verified my previous hypothesis. I will inform patient 1 and 2 they have contracted cholera
and patient 2 has contracted a symptomatic strain. I will have them undergo corresponding treatment.