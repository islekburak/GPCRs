import subprocess,os

query_path = "/cta/users/islekburak/proteomes_for_class_F/"
query_files = os.listdir(query_path)

subject_path = "/cta/users/islekburak/blastdb_for_class_F/"
subject_files = os.listdir(subject_path)


bash = "blastp -query " + query_path + query_files + " -db " + subject_path + subject_files + " -outfmt 0 -out " + temp_out_file.name
process = subprocess.calls(bash, shell=True)
    
