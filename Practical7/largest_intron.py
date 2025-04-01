import re
seq = 'ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA'
large_in = re.findall(r'GT.+AG', seq)
print(f'the largest intron is {large_in}, the length is {len(large_in[0])}')

