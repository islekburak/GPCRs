from Bio import SeqIO, AlignIO
import argparse, textwrap

parser=argparse.ArgumentParser(prog="align2original_indexfinder.py",
    usage="python3 %(prog)s [options] <path_of_file>",
    description=textwrap.dedent("""\
        authors:    ADEBALI LAB - https://github.com/CompGenomeLab
        contact:    https://adebalilab.org/contact/"""),
    add_help=True,
    formatter_class=argparse.RawTextHelpFormatter, 
    epilog=textwrap.dedent("""\

===========================================================================================================================================

This program helps you to detect original position of protein residues. You should enter the residue position of alignment file (as -idx).

#   REQUIRED
    ========

> with "-org" flag    (--original)   ,   You should specify your original fasta file path.

> with "-aln" flag    (--alignment)     ,   You should specify your alignment file path.

> with "-idx" flag    (--alignindex)     ,   You should enter an integer that represents alignment index.

===========================================================================================================================================
"""))

parser.add_argument("-org","--original", metavar="<original.fasta file>", required=True, help="Write the path and the name of your input file (i.e. /home/Desktop/FZD4.fasta)")
parser.add_argument("-aln","--alignment", metavar="<alignment.fasta file>", required=True, help="Write the path and the name of your output file (i.e. /home/Desktop/FZD4_MSA.fasta)")
parser.add_argument("-idx","--alignindex", metavar="<alignment index>", required=True, help="Write only an integer (i.e. 369)")
args=parser.parse_args()

#getting input path
org=args.original
aln=args.alignment
idx=args.alignindex

alignment = AlignIO.read(aln, 'fasta')
original = SeqIO.parse(org, 'fasta')
index=int(idx) 
for original_record, alignment_record in zip(original, alignment):
    alignment_seq = str(alignment_record.seq)
    original_seq = str(original_record.seq)

    gaps = alignment_seq[:index].count('-')
    original_index = len(alignment_seq[:index]) - gaps
    assert alignment_seq[index] ==  original_seq[original_index]
    #yield ("The conserved residue {} at location {} in the alignment can be found at location {} in {}.".format(alignment_seq[index],index, original_index, original_record.id.split('|')[-1])
print(original_index)
