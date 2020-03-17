- [Abstract](#Abstract)
<!-- toc -->

Abstract
========
GPCRs are reported as highly related with few physiological pathway
components -such as hormones and neurotransmitters-, regulation of
social graces, regulation of the inflammatory responses and responsible
for vision, olfaction and taste mechanisms \[1, 2\]. GPCRs' helices have
back and forth loops that are connected by flexible linkers at the EC
and IC ends, therefore they have defined as 7-transmembrane (7TM)
proteins for their 7 helices structures and localization through the
cell membrane. Now there are various structures of 7TM proteins that
have been solved, approximately 850 of 7TM proteins are defined and they
classified into five subgroups by GRAFS classification roughly \[3\].
They classified with the features while they have different states,
active to inactive forms in a complex with a G-proteins. In this study,
our purpose is to understand the evolutionary history, functions,
interactions, and significance of GPCRs using different genomic tools
*in silico*.

Accordingly, we have focused on the F class of these GPCRs. Hence we performed BLAST using human sequences for Frizzled/SMO family (11 were obtained from Uniprot-KB database) via high-performance computing. The results of BLAST are evaluated and the protein sequences are clustered by sequence similarities to create a phylogenetic tree. After getting orhtolog information for human Frizzled receptors, we intended to create a
domain pattern for differential diagnosis of Frizzled GPCRs. Thus it
helps to determine functional equivalence to the sets of orthologs of
GPCRs. Then we will perform phylogenetic profiling of the categorized
subfamilies. With the predictions using computer-based genomic tools and
algorithms, we will be able to build an MSA database classified by
subfamilies in the future.

**Key Words:** GPCRs; Frizzled; High-Performance Computing

The present work was supported by the Research Fund of European
Molecular Biology Organisation (EMBO). Project No. xxxxx

# 1. INTRODUCTION & PURPOSE

They classified with the features while they have different states, active to inactive forms in a complex with a G-proteins.

With this project, we intend to establish a method that helps to determine functional equivalence to the sets of orthologs of GPCRs. Then we will perform phylogenetic profiling of the categorized subfamilies. With the predictions that we will have using computer-based genomic tools and algorithms, we will be able to build an  MSA database classified by subfamilies. It will be easily accessed by users and be informative for functions, sequence and structural behaviors of GPCRs.

MSA and Blast commonly used tools used for protein alignments to understand the evolutionary history of target gene’s orthologs and paralogs by evaluating with the phylogenetic tree. The prediction of amino acid substitutions, can change with which homologous sequences are selected to analyze.  Automated tools may have an incorrect approaches to interpreting the conservation and divergency by skipping the variations that occurred in homologous proteins and resulting the lost of ancestral evolutionary constraints as they changed their functions. Because of their unique divergence profile, GPCRs have not been successfully dissected into subfamily specific phylogenetic trees by the automated tools. Therefore, identifying the set of proteins conserving the ancestral function, and distinguished them from diverged homologs are essential for accurate evaluation of the conservation status of amino acids. 

In this project, our purpose is to understand the evolutionary history, functions, interactions, and significance of GPCRs using different genomic tools in silico. For that firstly we have focused on F class of these 7TM proteins, to understand them well. We firstly purpose defining orthologous groups in class F GPCRs by identifying proteins in the course of evolution with assigning common ancestral points to create phylogenetic profiling. Besides, in light of the knowledge of their structural behavior, we will be able to consider new approaches to discover new computer-aided drugs to cure disorders or pathological defects in the molecular homeostasis resulting from the changes in the activation mechanisms of GPCRs.

# 2. GENERAL INFORMATION

## 2.1. GPCRs and their structures
GPCRs are the largest family of membrane proteins and reported as highly
related with few physiological pathways; such as immune system
regulation mechanisms including nervous system transmissions (regarding
vision, taste, smell, etc.), regulation of social graces, regulation of
the the inflammatory response, and the development of some types of
carcinogenic processes \[2\]. GPCRs play key roles in a wide range of
functions for humans and they are sustained as crucial components in
many diseases as previously shown \[4-6\].

GPCRs are only seen in Eukaryotes\[7\] and localized among the
intercellular membrane, and generally, have seven a-helices that
starting with their N-terminus. These structures travel across the cell
membrane from the extracellular region to intracellular, and vice versa,
by seven times. The helices have back and forth loops that are connected
by flexible linkers at the EC and IC ends. In general, they are defined
as 7-transmembrane (7TM) proteins for their seven membrane-spanning
α-helical segments and localization through the cell membrane (**Figure
1**). This architecture has been generally conserved over the course of
evolution and especially extracellular regions help to bind signal
molecules from the outside of the cell. However even simple eukaryotes
like yeasts have GPCRs to control basic mechanisms as maintain glucose
levels and sense mating factors, multicellular organisms use GPCRs
considerably in more functions.

## 2.2. The activation mechanism of GPCRs

As their name suggests, GPCRs can interact with G proteins that have a
key role in the activation of GDP, when they stimulated with various
signals. They can trigger some signaling pathways through the initiation
of cascades via their EC regions at N-terminus, when they bind to signal
molecules from the outside environment of cells \[8\].

The G proteins that associate with GPCRs have a structure
of heterotrimeric construction, unlike the other single subunit G
proteins such as Ras signaling protein. Heterotrimeric G proteins have
three different subunits that are called alfa, beta, and gamma. Beta and
gamma units are generally seen as dimer structure and they are bound to
the cell membrane by lipid anchors (**Figure 1**).

With the binding of ligand to GPCRs EC loops, the G protein alpha
subunit triggered with the conformational differentiation of GPCR, and
convert to an active form that can trigger second messengers in cell. In
this rearrangement process, GTP replaces the GDP bound to the alpha
subunit of GPCRs through the agonistic way, thus two different
sub-structures occur such as GTP-bound alpha subunit and a beta-gamma
dimer (*i.e*. in humans 16 α-subunits, 5 β-subunits, and 12 different
γ-subunits showed in previous studies)\[9\]. When the GTP is hydrolyzed
back to GDP, the G protein alpha subunit reassociates with other
separated subunits and turn off to inactivated form. This regulation
mechanism act as switch on-off cycle and that is why GPCRs may be
thought of as GEF-like proteins. The activated α-subunit and β-γ dimers
can interact with other proteins that are used in the process of
triggering cascades inside the cell.

| ![](/home/islekburak/Downloads/EMBO-REPORT/results/GPCR.png)
|:--:|
| **Figure:** *Structures and activation mechanism of 7TM domains* |
| In stimulated cells, when the agonist bind on EC loops of GPCRs GTP transforms to GDP with dehydration. The GPCRs (light green helices) bound subunits of G proteins (alpha: orange circle, beta & gamma: purple circles) dissociate upon receptor stimulation by a ligand from ECM. G alpha subunit then triggers various cascades in the cell \[8\]. |

## 2.3. Inner cell second messengers to activate various cascades
Activation of a single G protein can affect the production second messemgers such as cyclic AMP, diacylglycerol, and inositol 1, 4, 5-triphosphate.  Membrane associated adenylyl cyclase is the common target of G proteins and they stimulated with the GTP bound alpha subunit, results the synthesis of cAMP that involved in responses to sensory input, hormones, and nerve transmission in humans.

Membrane associated enzyme phospholipase C is the another target of activated G proteins. It catalyze the synthesis of DAG and IP3 which have crucial roles in human bodily processes.

## 2.4. Classification of GPCRs

Atwood and Findlay made a classification for GPCRs using their sequence
homologies and functionalities, that has six different subdivision (A to
F) \[10\]. Later that, phylogenetic analyzes the human-provided the
GRAFS classification and approximately 850⁠ of 7TM proteins are defined
and they classified into five subgroups  \[3\]. Now there are more than
100 ligand-mediated X-ray structures of 7TM proteins have been solved,
and specified as 25 different structures for every four group four
classes (A to F) roughly.


Class A (Rhodopsin) | Class B (Secretin) | Class B<sub>2</sub> (Adhesion) | Class C (Glutamate) | Class F (Frizzled/SMO)
|:---------|----------|---------|---------|----------|
 It has 13 subgroups and 683 members | They evolved from the Adhesion family of GPCRs | It has 33 members in humans | It has 22 members in humans| It has 11 members in humans with SMO
 Characterized by short N-termini and interactions with a broad variety of ligands | Characterized by a large N-terminal extracellular domain and seven transmembrane helices | Characterized with the long N-termini which contains lethorea of multiple domains | Characterized with the EC domain act as the endogenous LBD that contains a Venus flytrap (VFT) module and a CRD| Characterized with the long cysteine-rich N-termini (CRD)
 Known with 7tm_1 domain (UniPot accession: PF00001) | Known with Dicty_Car domain (UniPot accession: PF05462) | Known with the 7tm_3 domain (UniPot accession: PF00003) | Known with the 7tm_2 domain (UniPot accession: PF00002) | Known with the Fz, Frizzled and SMO_Human domains (UniPot accession: PF01392, PF01534 and Q99835)

.caption[**Table:** *Characteristics of GPCRs*]

### 2.4.1. Class F GPCRs (Frizzled/SMO Family)

They are characterized with the long cysteine-rich N-termini. They are known with the Fz, Frizzled and SMO_Human domains (UniPot accession: PF01392, PF01534 and ,Q99835)

MATERIALS & METHODS
===================

Obtaining proteomes
-------------------

We downloaded the 7TM-Frizzled domains (10 different *Frizzled* and 1
*Smoothened* domain for human) from Uniprot-KB Database
(<http://www.uniprot.org>) to search them against to entire set of
available complete eukaryotic proteomes (n=932) that we downloaded from
the same database using FTP and we stored them in HPC with the format of
FASTA. We were interested in an only transmembrane part of the
sequences. Thus we trimmed the proteome sequences of 11 domains from
their ECM regions.

Python codes that have written for the different processes are reachable
in Github (<https://github.com/islekburak/GPCRs>).

Sequence retrieval, mining, and removal
---------------------------------------

GPCRs from eukaryotic lineages were mined using HMM searches performed
using HMMER3 (<http://hmmer.janelia.org/>). We retrieved only the
sequences which received the Pfam domains *Frizzled* (PF01534), *Fz*
(PF01392), *Smo\_Human*(Q99835). The sequences with a 7TM domain
predicted to have fewer than six or more than nine transmembrane
segments in TMHMM tool (<http://www.cbs.dtu.dk/services/TMHMM/>) were
excluded for further analysis in order to reduce the number of
incomplete sequences.

Alignments and phylogenetic analysis
------------------------------------

The selected GPCR candidates were aligned using MAFFT version xxx
(MAFFT, <http://mafft.cbrc.jp/alignment/server/>) using the E-INS\_I
version (optimal for sequences with conserved motifs and carrying
multiple domains) with default parameters.

Domain search
-------------

The N-terminal domains for the identified Frizzled family members were
identified with Pfam search and also verified using RPS-Blast with a
cutoff e-value of 0.01 against to Conserved Domain Database (CDD)
version xxx position-specific scoring matrixes (PSSMs).

| ![](/home/islekburak/Downloads/EMBO-REPORT/results/SS2.png)
|:--:|
| **Figure:** *Workflow for the identification of Frizzled Proteins* |

Creating the dataset with the results of analyzes
-------------------------------------------------

We concatenated all the results of analyzes within the same file to do
further analysis. The parameters that we stored for all domain hits can
be seen in **Table 1.**



Online Databases
----------------

The online databases that were used in this study are given in **Table
2**.

[]{#_Ref22157336 .anchor}Table : Online Databases

+-------------------------+-------------------------+---------------+
| **Database**            | **Information**         | **Reference** |
+=========================+=========================+===============+
| **Pfam**                |                         |               |
|                         |                         |               |
| **(h                    |                         |               |
| ttps://pfam.xfam.org)** |                         |               |
+-------------------------+-------------------------+---------------+
| **UniProtKB**           |                         |               |
|                         |                         |               |
| **(htt                  |                         |               |
| ps://www.uniprot.org)** |                         |               |
+-------------------------+-------------------------+---------------+
| **PubMed -NCBI**        | It is a database that   |               |
|                         | comprises more than 30  |               |
| **(https://www.ncb      | million citations for   |               |
| i.nlm.nih.gov/pubmed)** | biomedical literature   |               |
|                         | from MEDLINE, life      |               |
|                         | science journals, and   |               |
|                         | online books.           |               |
+-------------------------+-------------------------+---------------+

### 2.4.2. {#section .list-paragraph}

Tools and Programming Languages
-------------------------------

The tools and programming languages that were used in this study are
given in **Table 3**.

[]{#_Ref22157581 .anchor}Table : Tools and Programming Languages

+----------------+----------------+----------------+---------------+
| **The          | **The          | *              | **Reference** |
| Language**     | packages**     | *Information** |               |
+================+================+================+===============+
| **Python 3**   | Pandas         | Python         |               |
|                |                | programlama    |               |
|                |                | dili için      |               |
|                |                | yazılmış*,*    |               |
|                |                | açık kaynak    |               |
|                |                | kodlu, veri    |               |
|                |                | yapılarının    |               |
|                |                | yüksek         |               |
|                |                | performanslı   |               |
|                |                | analizini      |               |
|                |                | kolaylaştıran  |               |
|                |                | BSD - lisanslı |               |
|                |                | bir            |               |
|                |                | kütüphanedir.  |               |
+----------------+----------------+----------------+---------------+
|                | NumPy & SciPy  | Matemeatik,    |               |
|                |                | bilim ve       |               |
|                |                | mühendislik    |               |
|                |                | hesaplamaları  |               |
|                |                | için CPython   |               |
|                |                | ile yazılmış   |               |
|                |                | bir dildir.    |               |
+----------------+----------------+----------------+---------------+
| **Aquerium**   |                |                |               |
|                |                |                |               |
| *              |                |                |               |
| *(Architecture |                |                |               |
| Querying       |                |                |               |
| Podium)**      |                |                |               |
|                |                |                |               |
| **(http:       |                |                |               |
| //aquerium.ade |                |                |               |
| balilab.org)** |                |                |               |
+----------------+----------------+----------------+---------------+
| **CDVist**     |                |                |               |
|                |                |                |               |
| **(https       |                |                |               |
| ://cdvist.adeb |                |                |               |
| alilab.org/)** |                |                |               |
+----------------+----------------+----------------+---------------+

RESULTS
=======

The *Frizzled* Receptor Family
------------------------------

### 2.4.3. Blast for human proteomes

We did some rearrangements in the sequences of these domains. We cut the
partial sequences of these domains that are located in ECM. After that,
we BLAST all (n=11) the frizzled partial domains against to complete
proteome sequences. Eventually, now we have some results about these
sequences and their hit values (e-values) by using BLAST in HPC. The
results are shown below (Figure 3).

![](media/image3.png){width="5.602777777777778in"
height="3.0104166666666665in"}

The sequences of Frizzled domains that were downloaded from UniProt
database look like as shown below.

![](media/image4.png){width="4.645833333333333in"
height="4.479166666666667in"}

[]{#_Toc22366811 .anchor}Figure : Fasta files that downloaded from
UniProt Database

![](media/image5.png){width="2.9555555555555557in"
height="2.9409722222222223in"}To split the targeted sequence from the
whole sequence of Frizzled domains, we write a Python code like that:

By the way, we determine the targeted sequences which are located in
ICM, as a range of amino acid sequences.

![](media/image6.png){width="2.4993055555555554in"
height="2.5131944444444443in"}

![](media/image7.png){width="5.324305555555555in"
height="2.8208333333333333in"}After that, we cut the extra amino acids
from these complete sequences. Eventually, we have a result as shown
below.

![](media/image8.png){width="3.321527777777778in"
height="2.9458333333333333in"} In the next step we blast these partial
sequences against to complete proteome sequences obtained from whole
eukaryotes. And we obtain results as shown in below:

On the next step, we will create a .hmm file by using HMMER3 for these
selected sequences and their hits. And then we want to create domain
architectures to analyze them effectively.

### 2.4.4. ![](media/image9.png){width="5.904861111111111in" height="2.8354166666666667in"}HMMER3 for *Frizzled* Family Receptor

![](media/image10.png){width="5.904861111111111in"
height="2.8354166666666667in"}

![](media/image11.png){width="5.904861111111111in"
height="2.8354166666666667in"}vfebgr

![](media/image12.png){width="5.904861111111111in"
height="2.8354166666666667in"}4frgt

![](media/image13.png){width="5.904861111111111in"
height="2.8354166666666667in"}defrevf

![](media/image14.png){width="5.904861111111111in"
height="2.8354166666666667in"}dfrevg

![](media/image15.png){width="5.904861111111111in"
height="2.8354166666666667in"}def

![](media/image16.png){width="5.904861111111111in"
height="2.8354166666666667in"}frgtb

![](media/image17.png){width="5.904861111111111in"
height="2.8354166666666667in"}adcsvfg

![](media/image18.png){width="5.904861111111111in"
height="2.8354166666666667in"}dfg

![](media/image19.png){width="5.904861111111111in"
height="2.8354166666666667in"}asdsv

![](media/image13.png){width="5.904861111111111in"
height="2.8354166666666667in"}Asdfs

DISCUSSION
==========

REFERENCES {#references .list-paragraph}
==========

1\. Rosenbaum, D.M., S.G. Rasmussen, and B.K. Kobilka, *The structure
and function of G-protein-coupled receptors.* Nature, 2009.
**459**(7245): p. 356-63.2. Wu, F., et al., *Structure and Function of
Peptide-Binding G Protein-Coupled Receptors.* J Mol Biol, 2017.
**429**(17): p. 2726-2745.3. Wootten, D., et al., *Mechanisms of
signalling and biased agonism in G protein-coupled receptors.* Nat Rev
Mol Cell Biol, 2018. **19**(10): p. 638-653.4. Hilger, D., M. Masureel,
and B.K. Kobilka, *Structure and dynamics of GPCR signaling complexes.*
Nat Struct Mol Biol, 2018. **25**(1): p. 4-12.5. Munk, C., et al., *An
online resource for GPCR structure determination and analysis.* Nat
Methods, 2019. **16**(2): p. 151-162.6. Thal, D.M., et al., *Recent
advances in the determination of G protein-coupled receptor structures.*
Curr Opin Struct Biol, 2018. **51**: p. 28-34.7. Krishnan, A., et al.,
*The origin of GPCRs: identification of mammalian like Rhodopsin,
Adhesion, Glutamate and Frizzled GPCRs in fungi.* PLoS One, 2012.
**7**(1): p. e29817.8. Li, J., et al., *The Molecule Pages database.*
Nature, 2002. **420**(6916): p. 716-7.9. Krishnan, A., et al.,
*Evolutionary hierarchy of vertebrate-like heterotrimeric G protein
families.* Mol Phylogenet Evol, 2015. **91**: p. 27-40.10. Attwood, T.K.
and J.B. Findlay, *Fingerprinting G-protein-coupled receptors.* Protein
Eng, 1994. **7**(2): p. 195-203.11. Smith, J.S., R.J. Lefkowitz, and S.
Rajagopal, *Biased signalling: from simple switches to allosteric
microprocessors.* Nat Rev Drug Discov, 2018. **17**(4): p. 243-260.12.
Milligan, G., R.J. Ward, and S. Marsango, *GPCR homo-oligomerization.*
Curr Opin Cell Biol, 2019. **57**: p. 40-47.13. Gurevich, V.V. and E.V.
Gurevich, *GPCRs and Signal Transducers: Interaction Stoichiometry.*
Trends Pharmacol Sci, 2018. **39**(7): p. 672-684.14. Eichel, K. and M.
von Zastrow, *Subcellular Organization of GPCR Signaling.* Trends
Pharmacol Sci, 2018. **39**(2): p. 200-208.
