import subprocess
import os
fasta_files_for_blastp_db_path = "/cta/users/islekburak/proteomes_for_class_F/"
fasta_files_for_blast_db= os.listdir(fasta_files_for_blastp_db_path)
for file in fasta_files_for_blast_db:
    if "with_tax_info" not in file:
        continue
    bash = "makeblastdb -in " + fasta_files_for_blastp_db_path + file +" -parse_seqids -dbtype prot -out /cta/users/aylinbircan/blastdb_single_isoform/blastdb_for_class_F/ " + file.split("_")[0]
    process = subprocess.calls(bash, shell=True)
