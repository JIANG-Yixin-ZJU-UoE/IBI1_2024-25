# goal: use the input sequence to find the gene that contains TATA, output the gene name and instances of TATA
# procedures:
# 1. ask the user to input one of GTAG、GCAG、ATAC
# 2. according to the input, find the sequence that contains the input
# 3. judge if the sequence contains TATA
# 4. if so, store the sequence in a fa file, count the instances of TATA and print the gene name

import re # import the re to use later
combination = input("please choose one from the three sequence: GTAG, GCAG, ATAC: ") # ask the user to input
# open the file and initialize the list, str, gene name and TATA count
list = ['GTAG', 'GCAG', 'ATAC']
raw_file = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
str = ""
gene_name = ""
TATA_count = 0

for i in range(0,3):
    if combination == list[i]:
        out_file = open(f'{list[i]}_spliced_genes.fa', 'w') # create according file
        for line in raw_file:
            if re.search(r'gene:(\S+)\s', line): # judge if the line contains the gene name
                if re.search(rf'{list[i][0:2]}.+{list[i][2:4]}', str): # judge if the last sequence contains donor/acceptor
                    # count the instances of TATAWAW
                    instance_list = re.findall(r'TATA[AT]A[AT]', str) # find all the TATA boxes
                    TATA_count = len(instance_list) # count the number of TATA instances
                    out_file = open(f'{list[i]}_spliced_genes.fa', 'a') # open the according file
                    out_file.write('>' + gene_name + f'   sequence TATAWAW appears {TATA_count} times' '\n') # write the gene name and the TATA count
                    out_file.write(str + '\n') # write the sequence
                    gene_name = re.findall(r'gene:(\S+)\s', line)[0] # define the gene name as the next gene
                    str = '' # reinitialize the str
                else:
                    gene_name = re.findall(r'gene:(\S+)\s', line)[0] # define the gene name as the next gene
                    str = '' # reinitialize the str
            else:
                str += line.strip() # add the line into the str



