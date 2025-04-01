input = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
str = ""
import re
for line in input:
    if re.search(r'gene:(\S+)\s', line):
        if re.search('TATA', str):
            #str = 'CGCGCGCGCGCGCGCGGCGCATATTATATATATAT'
            print(gene_name[0])
            print(str)
            gene_name = re.findall(r'gene:(\S+)\s', line)
            str = ''
        else:
            gene_name = re.findall(r'gene:(\S+)\s', line)
            str = ''
    else:
        str += line.strip()
