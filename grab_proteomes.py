import ftplib,os,re,sys

ftp = ftplib.FTP("ftp.uniprot.org")
ftp.login()
ftp.cwd("pub/databases/uniprot/current_release/knowledgebase/reference_proteomes/Eukaryota/")

filenames=ftp.nlst("*[0-9].*fasta.gz")

for filename in filenames:
    local= os.path.join("islekburak@10.39.60.250:/cta/users/islekburak/codes/new/",filename)
    local_filename= "'" + local + "'"
    file=open(local_filename,"wb")
    ftp.retrbinary("RETR" + " " +filename, file.write)
    file.close()
ftp.quit()
