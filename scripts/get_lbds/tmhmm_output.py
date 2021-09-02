import sys
from Bio import SeqIO

out_tmhmm=sys.argv[1]
fasta = sys.argv[2]

lbd={}
lbd_1={}

for ln, line in enumerate(open(out_tmhmm, "r")):
	#print(line)
	if line.startswith("#"):
		line = line.strip("\n").split(" ")
#		print(line)
		wp = line[1].split(":")[0]
		#print(wp)
		num = line[7]

		if num == "2":
			lbd[wp]={}
			lbd[wp]["s"]=[]
			lbd[wp]["e"]=[]		
		if num == "1":
			lbd_1[wp]={}
			lbd_1[wp]["s"]=[]
			lbd_1[wp]["e"]=[]

#num = line.split(":").[1][2]
	else: 
		line = line.strip("\n").split("\t")
		start = line[3].split()[0] 
		end = 	line[3].split()[1]
		#print(start, end)
		wp = line[0]
		wp = wp.split(":")[0]

		if wp in lbd.keys():
			lbd[wp]["s"].append(start)
			lbd[wp]["e"].append(end)
		if wp in lbd_1.keys():
			lbd_1[wp]["s"] = start
			lbd_1[wp]["e"] = end 
		#	print(lbd_1)

def load_seqs(fasta):
	seqs={}
	records = SeqIO.parse(fasta, "fasta")
	for record in records:
		tara = record.id.split(":")[0]
		seqs[tara]=record.seq
	return seqs

def write_fasta(output, name, seq):
	with open(output, "a+") as f:
		f.write(">"+name+"\n")
		f.write(str(seq)+"\n")
		f.close()

#print(lbd)
seqs = load_seqs(fasta)
for wp in lbd:
	try:
		lbd_s = int(lbd[wp]["e"][0])
		lbd_e = int(lbd[wp]["s"][1]) + 1
		lbds= seqs[wp][lbd_s:lbd_e]
		if len(lbds) > 30:
			write_fasta("lbds_2tm.faa", wp, lbds)
			write_fasta("lbds_1tm_2tm.faa", wp, lbds)
                        #print(">" + wp)
			#print(lbds)
	except IndexError:
		next

for wp in lbd_1:
	try:
		lbd_s = 0
		lbd_e = int(lbd_1[wp]["s"]) + 1
		lbds= seqs[wp][lbd_s:lbd_e]
		lbds= seqs[wp][lbd_s:lbd_e]
		if len(lbds) > 30:
			write_fasta("lbds_1tm.faa", wp, lbds)
			write_fasta("lbds_1tm_2tm.faa", wp, lbds) #print(">" + wp)
			#print(lbds)
	except KeyError:
		next
