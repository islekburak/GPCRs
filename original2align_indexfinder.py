from Bio import SeqIO, AlignIO
import argparse, textwrap

parser=argparse.ArgumentParser(prog="original2align_indexfinder.py",
    usage="python3 %(prog)s [options] <path_of_file>",
    description=textwrap.dedent("""\
        authors:    ADEBALI LAB - https://github.com/CompGenomeLab
        contact:    https://adebalilab.org/contact/"""),
    add_help=True,
    formatter_class=argparse.RawTextHelpFormatter, 
    epilog=textwrap.dedent("""\

===========================================================================================================================================

This program helps you to detect alignment position of protein residues. You should enter original residue position to find alignment index (as -idx).

#   REQUIRED
    ========

> with "-org" flag    (--original)   ,   You should specify your original fasta file path.

> with "-aln" flag    (--alignment)     ,   You should specify your alignment file path.

> with "-idx" flag    (--originalindex)     ,   You should enter an integer that represents original index.

===========================================================================================================================================
"""))

parser.add_argument("-org","--original", metavar="<original.fasta file>", required=True, help="Write the path and the name of your input file (i.e. /home/Desktop/FZD4.fasta)")
parser.add_argument("-aln","--alignment", metavar="<alignment.fasta file>", required=True, help="Write the path and the name of your output file (i.e. /home/Desktop/FZD4_MSA.fasta)")
parser.add_argument("-idx","--originalindex", metavar="<original index>", required=True, help="Write only an integer (i.e. 212)")
args=parser.parse_args()

#getting input path
org=args.original
aln=args.alignment
idx=args.originalindex

alignment = AlignIO.read(aln, 'fasta')
original = SeqIO.parse(org, 'fasta')
index=int(idx) 


for original_record, alignment_record in zip(original, alignment):
    alignment_seq = str(alignment_record.seq)
    original_seq = str(original_record.seq)

    residue = original_seq[index]
    for i in range(index, len(alignment_seq)):
        if alignment_seq[i] == residue and alignment_seq[:i].replace('-', '') == original_seq[:index]:
            a=i
print(a)