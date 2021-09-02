import sys
import Bio
from Bio import SeqIO

fasta_all = sys.argv[1]
fasta_incomplete = sys.argv[2]

already = []
for seq_record in SeqIO.parse(fasta_incomplete, "fasta"):
	already.append(seq_record.id.split(".")[2])
	print(">"+str(seq_record.id))
	print(str(seq_record.seq))
for seq_record in SeqIO.parse(fasta_all, "fasta"):
	if not seq_record.id.split(".")[2] in already:
		print(">"+str(seq_record.id+".UNKNOWN"))
		print(str(seq_record.seq))
