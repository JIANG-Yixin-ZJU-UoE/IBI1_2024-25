# goal: find the largest intron in a sequence and report the length
# procedure:
# 1. import the re
# 2. input the sequence
# 3. use search and greedy matching to find the largest intron
# 4. print out the largest intron and count its length

import re
seq = 'ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA'
large_in = re.search(r'GT.+AG', seq)
print(f"the largest intron is: {large_in.group()}, the length is: {len(large_in.group())}")

