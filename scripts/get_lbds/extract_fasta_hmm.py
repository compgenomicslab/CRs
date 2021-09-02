import sys
import Bio
from Bio import SeqIO

seq2dom_info = sys.argv[1]
fasta_in = sys.argv[2]

def write_fasta(seq_id, seq, output):
	with open(output, "a+") as out:
		out.write(">"+seq_id+"\n")
		out.write(seq+"\n")
		out.close()


seq2dom = {}

for ln, line in enumerate(open(seq2dom_info)):
	line = line[:-1].split("\t")
	if not line[0] in seq2dom.keys():
		seq2dom[line[0]]={}
	if not line[1] in seq2dom[line[0]].keys():
		n = 0
	else:
		n +=1
		line[1]=str(line[1])+"."+str(n)
	seq2dom[line[0]][line[1]]={}
	seq2dom[line[0]][line[1]]["s"]=line[6]
	seq2dom[line[0]][line[1]]["e"]=line[7]
#print(seq2dom)

name2seq={}
seq_order=[]
for seq_record in SeqIO.parse(str(sys.argv[2]), "fasta"):
	name2seq[seq_record.id]=seq_record.seq
	seq_order.append(seq_record.id)
	
for i in seq_order:
	try:
		for dom in seq2dom[i]:
			seq=str(name2seq[i][int(seq2dom[i][dom]["s"])-1:int(seq2dom[i][dom]["e"])-1])
			write_fasta(i+"."+dom, seq, "all_domains.faa")
			if dom.split(".")[0] == "MCPsignal":
				write_fasta(i+"."+dom, seq, "MCPsignal.faa")
			if dom.split(".")[0] != "MCPsignal" and dom.split(".")[0] != "HAMP" and dom.split(".")[0] != "HAMP_N3":
				write_fasta(i+"."+dom, seq, "lbds_hmm.faa")

	except KeyError:
		write_fasta(i,str(name2seq[i]),"nodomains.faa")

#		print(">"+dom+"\t"+i)i
#		print(dom)
#		print(name2seq[i][int(seq2dom[i][dom]["s"]):int(seq2dom[i][dom]["e"])])

