import re
cut_sequence = "ACGTCGTGACTCGTATCGATC"
recog_seq = "TCGT"
def site(cut_sequence, recog_seq):
    flag = False
    for i in cut_sequence:
        if i == "A" or i == "T" or i == "G" or i == "C":
            flag = False
        else:
            flag = True
            seq_error = "error: the DNA sequence is not valid"
            return seq_error

    if flag == False:
        if re.findall(rf"{recog_seq}", cut_sequence):
            index = 1
            for i in range(len(cut_sequence)-3):
                test_str = cut_sequence[i:i+len(recog_seq)]
                if test_str == recog_seq:
                    print(index, recog_seq[0])
                    break                 
                else:
                    index += 1

print(site(cut_sequence, recog_seq))
