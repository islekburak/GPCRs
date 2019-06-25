import ftplib,os,re,sys

ftp = ftplib.FTP("ftp.uniprot.org")
ftp.login()
ftp.cwd("pub/databases/uniprot/current_release/knowledgebase/reference_proteomes/Eukaryota/")

filenames=ftp.nlst("*[0-9].*fasta.gz")

for filename in filenames:
    local_filename = os.path.join('islekburak@10.39.60.250 : cta/users/islekburak/codes/new/', filename)
    file = open(local_filename, 'wb')
    ftp.retrbinary('RETR '+ filename, file.write)
    file.close()
ftp.quit()

#names=re.compile("\d.fasta.gz$")
#filelist = pattern.findall("LIST")
"""
import os
from ftplib import FTP
import re

ftp = FTP("ftp.uniprot.org", "ANONYMOUS", "PASSWORD")
#ftp.login()
#ftp.retrlines("LIST")
 
ftp.cwd("pub/databases/uniprot/current_release/knowledgebase/reference_proteomes/Eukaryota/")

def grabFile():
	filename=*[0-9].*fasta.gz
	localfile=open(filename, 'wb')
	ftp.retrbinary("RETR" + filename, localfile, localfile.write)
	ftp.quit()
	localfile.close()
def placeFile():
	filename=*[0-9].*fasta.gz
	ftp.storbinary("STOR "+filename, open(filename, 'rb'))
	ftp.quit()

data = []
ftp.dir(data.append)
ftp.quit()
"""
