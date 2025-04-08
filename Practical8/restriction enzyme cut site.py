import re
cut_sequence = "ACGTCGTGACTCGATCGATC"
recognized_sequence = "TCGT"
def site(cut_sequence, recognized_sequence):
    flag = False
    for i in cut_sequence:
        if i == "A" or i == "T" or i == "G" or i == "C":
            flag = False
        else:
            flag = True
            seq_error = "error: the DNA sequence is not valid"
            return seq_error

    if flag == False:
        if re.findall(rf"{recognized_sequence}", cut_sequence):
            index = 1
            for i in cut_sequence:
                if i == recognized_sequence[0]:
                    return index, recognized_sequence[0]
                else:
                    index += 1

print(site(cut_sequence, recognized_sequence))
