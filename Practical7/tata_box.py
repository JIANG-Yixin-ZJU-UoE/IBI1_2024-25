input = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r') 
str = ""
gene_name = []
import re
for line in input:
    line = line.strip()
    if re.search(r'gene:(\S+)\s', line):
        if re.search(r'TATA[AT]A[AT]', str):
            # print('>' + gene_name[0])
            # print(str)
            out_file = open('tata_genes.fa', 'a')
            out_file.write('>' + gene_name[0] + '\n')
            out_file.write(str + '\n')
            gene_name = re.findall(r'gene:(\S+)\s', line)
            str = ''
        else:
            gene_name = re.findall(r'gene:(\S+)\s', line)
            str = ''
    else:
        str += line.strip()


