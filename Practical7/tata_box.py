# goal: to find and report all genes and its sequences containing TATA
# procedure:
# 1. open the file and initialize a str to store the sequence and a list to store the gene name
# 2. iterate lines in the file to judge if the line contain the gene name
# 3. if so, find out if the last sequence contains TATA; if not, add the line into the str
# 4. if the sequence contains TATA, create a file and store the gene name and the sequence into the file, reinitialize the list and the str
# 5. if not, just reinitialize the list and the str

input = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r') # read the original file
str = "" # initialize a str and a list
gene_name = []
import re # import the re to use later
for line in input: # iterate the line in the file
    line = line.strip() # link all lines together
    if re.search(r'gene:(\S+)\s', line): # judge if the line contains the gene name
        if re.search(r'TATA[AT]A[AT]', str): # judge if the last gene sequence contains TATA
            # print('>' + gene_name[0]) 
            # print(str)
            out_file = open('tata_genes.fa', 'a') # add contents in the file
            out_file.write('>' + gene_name[0] + '\n') # write the gene name
            out_file.write(str + '\n') # write the sequence of the last gene
            gene_name = re.findall(r'gene:(\S+)\s', line) # define the gene name as the next gene
            str = '' # reinitialize the str
        else:
            gene_name = re.findall(r'gene:(\S+)\s', line) # define the gene name as the next gene
            str = '' # reinitialize the str
    else:
        str += line.strip() # add the line into the str


