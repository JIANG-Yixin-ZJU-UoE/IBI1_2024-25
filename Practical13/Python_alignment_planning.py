# Goal: to calculate the alignment score and identity percentage of human&mouse, human&random, and mouse&random sequences
# Procedure:
# 1. import the necessary libraries
# 2. obtain the BLOSUM62 substitution matrix
# 3. get the sequences of human, mouse, and random genes from Uniprot
# 4. calculate the alignment score and identity percentage of human&mouse, human&random, and mouse&random sequences


# import the necessary libraries
from Bio.Align import substitution_matrices
blosum62 = substitution_matrices.load("BLOSUM62")

seq_human = "MLSRAVCGTSRQLAPVLGYLGSRQKHSLPDLPYDYGALEPHINAQIMQLHHSKHHAAYVNNLNVTEEKYQEALAKGDVTAQIALQPALKFNGGGHINHSIFWTNLSPNGGGEPKGELLEAIKRDFGSFDKFKEKLTAASVGVQGSGWGWLGFNKERGHLQIAACPNQDPLQGTTGLIPLLGIDVWEHAYYLQYKNVRPDYLKAIWNVINWENVTERYMACKK"
seq_mouse = "MLCRAACSTGRRLGPVAGAAGSRHKHSLPDLPYDYGALEPHINAQIMQLHHSKHHAAYVNNLNATEEKYHEALAKGDVTTQVALQPALKFNGGGHINHTIFWTNLSPKGGGEPKGELLEAIKRDFGSFEKFKEKLTAVSVGVQGSGWGWLGFNKEQGRLQIAACSNQDPLQGTTGLIPLLGIDVWEHAYYLQYKNVRPDYLKAIWNVINWENVTERYTACKK"
seq_random = "CISTFVLVAYAKNEFYMPLQIFMAPPRCWKAVFFYDCVDHPMSGIGTDHHHVMNQNIHRYWYPTENGANRHKWDLISEAVNHWHERFFNQEEQECQMVSPDMTEWGCFDVGRKSMPKPGEDMCTMNSSTYRKFNMNHKLWYALCPVARYKPITDHQARGLHGHLHSSNHRNSKIEGADQWWWCLLKWWSDDLAYRRWGMDNNCVMLDKCYIGQMKEPYYCLI"

# compare the alignment of human and mouse genes
human_mouse_score = 0
human_mouse_identity = 0
for i in range(len(seq_human)):
    human_mouse_score += blosum62[seq_human[i], seq_mouse[i]]
    if seq_human[i] == seq_mouse[i]:
        human_mouse_identity += 1
identity_percentage1 = human_mouse_identity / len(seq_human)
print(f"the alignment score is: {human_mouse_score}")
print(f"the identity percentage is: {identity_percentage1:.2%}")

# compare the alignment of human and random genes
human_random_score = 0
human_random_identity = 0
for i in range(len(seq_human)):
    human_random_score += blosum62[seq_human[i], seq_random[i]]
    if seq_human[i] == seq_random[i]:
        human_random_identity += 1
identity_percentage2 = human_random_identity / len(seq_human)
print(f"the alignment score is: {human_random_score}")
print(f"the identity percentage is: {identity_percentage2:.2%}")

# compare the alignment of mouse and random genes
mouse_random_score = 0
mouse_random_identity = 0
for i in range(len(seq_mouse)):
    mouse_random_score += blosum62[seq_mouse[i], seq_random[i]]
    if seq_mouse[i] == seq_random[i]:
        mouse_random_identity += 1
identity_percentage3 = mouse_random_identity / len(seq_mouse)
print(f"the alignment score is: {mouse_random_score}")
print(f"the identity percentage is: {identity_percentage3:.2%}")

print("the human and mouse sequences are most closely related")