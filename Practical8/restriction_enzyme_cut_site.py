# goal: to find the position of the first nucleotide in the cut sequence that matches the recognized sequence
# procedure:
# 1. set the initial sequence
# 2. test whether all the inputs are within "A", "G", "C", "T"
# 3. if it is a valid sequence, then find in the cut sequence the existence of recognized sequence
# 4. if so, return the position and the nucleotide

# import the re and initialize the sequence
import re

def site(cut_seq, recog_seq):

    """ find out if all the inputs are "A", "G", "C", "T" """

    if not re.search(r'^[AGCT]+$', cut_seq):
        print("the cut sequence is not valid")
        exit()
    if not re.search(r'^[AGCT]+$', recog_seq):
        print("the recognized sequence is not valid")
        exit()

    """ tell if the cut_seq contains the recog_seq sequence and return the position """

    list1 = []
    if re.findall(rf"{recog_seq}", cut_seq):
        for i in range(len(cut_seq)-len(recog_seq)+1):
            test_str = cut_seq[i:i+len(recog_seq)]
            if test_str == recog_seq:
                list1.append(i+1)       
        return list1

# this is an example of using the function
print(site(cut_seq = "ACGTCGTGACTCGTATCGATC", recog_seq = "TCGT"))


